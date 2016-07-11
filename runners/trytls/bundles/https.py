import ssl
import sys
import socket
import contextlib
import multiprocessing
from ..utils import tmpfiles
from ..gencert import gencert
from ..testenv import testenv, constant

try:
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
except ImportError:
    from http.server import HTTPServer, BaseHTTPRequestHandler


def badssl(ok_expected, name):
    return constant(ok_expected, name + ".badssl.com", 443)


@testenv
def badssl_onlymyca(ok_expected, name):
    _, _, cadata = gencert("localhost")
    with tmpfiles(cadata) as cafile:
        yield ok_expected, name + ".badssl.com", 443, cafile


@contextlib.contextmanager
def http_server(certdata, keydata, host="localhost", port=0):
    class Server(HTTPServer):
        ALLOWED_EXCEPTIONS = (socket.error,)

        def handle_error(self, request, client_address):
            exc_type, _, _ = sys.exc_info()
            if isinstance(exc_type, type) and issubclass(exc_type, self.ALLOWED_EXCEPTIONS):
                return
            HTTPServer.handle_error(self, request, client_address)

    class Handler(BaseHTTPRequestHandler):
        def setup(self):
            with tmpfiles(certdata, keydata) as (certfile, keyfile):
                self.request = ssl.wrap_socket(
                    self.request,
                    server_side=True,
                    certfile=certfile,
                    keyfile=keyfile
                )
            return BaseHTTPRequestHandler.setup(self)

        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-Type", "0")
            self.end_headers()

        def log_message(self, format, *args):
            pass

    def serve(connection, certdata, keydata, host, port):
        server = Server((host, port), Handler)
        connection.send((host, server.server_port))
        server.handle_request()

    reader, writer = multiprocessing.Pipe(duplex=False)
    process = multiprocessing.Process(
        target=serve,
        args=[writer, certdata, keydata, host, port]
    )
    process.start()
    try:
        host, port = reader.recv()
        yield host, port
    finally:
        process.terminate()
        process.join()


@testenv
def local(ok_expected, cn):
    certdata, keydata, cadata = gencert(cn)

    with http_server(certdata, keydata) as (host, port):
        with tmpfiles(cadata) as cafile:
            yield ok_expected, host, port, cafile


badssl_tests = [
    badssl(False, "expired"),  # not with an obsolete cert
    badssl(False, "wrong.host"),  # not with a wrong name
    badssl(False, "self-signed"),  # not just one's own claims
    badssl(True, "sha256"),  # future proof sha
    badssl(True, "1000-sans"),  # massive alternative names
    badssl(True, "10000-sans"),  # massive alternative names
    badssl(False, "incomplete-chain"),  # should have full proof of chain to trusted CA
    badssl(False, "superfish"),  # super fishy CA
    badssl(False, "edellroot"),  # rotten roots CA
    badssl(False, "dsdtestprovider")  # unproviding CA
]


ssllabs_tests = [
    constant(False, "www.ssllabs.com", 10443),
    constant(False, "www.ssllabs.com", 10444),
    constant(False, "www.ssllabs.com", 10445)
]


local_tests = [
    local(True, "localhost"),
    local(False, "nothing")
]


badssl_only_my_ca = [
    badssl_onlymyca(False, "sha256")
]


all_tests = badssl_tests + badssl_only_my_ca + ssllabs_tests + local_tests
