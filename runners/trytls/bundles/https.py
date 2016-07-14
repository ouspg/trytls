import ssl
import sys
import socket
import contextlib
import multiprocessing
from ..utils import tmpfiles
from ..gencert import gencert
from ..testenv import testenv, Test

try:
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
except ImportError:
    from http.server import HTTPServer, BaseHTTPRequestHandler


@testenv
def badssl(accept, name, description):
    yield Test(
        accept=accept,
        description=description,
        host=name + ".badssl.com",
        port=443
    )


@testenv
def badssl_onlymyca(description):
    _, _, cadata = gencert("localhost")

    with tmpfiles(cadata) as cafile:
        yield Test(
            accept=False,
            description=description,
            host="sha256.badssl.com",
            port=443,
            cafile=cafile
        )


@testenv
def ssllabs(accept, port, description):
    yield Test(
        accept=accept,
        description=description,
        host="www.ssllabs.com",
        port=port
    )


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
def local(accept, cn, description):
    certdata, keydata, cadata = gencert(cn)

    with http_server(certdata, keydata) as (host, port):
        with tmpfiles(cadata) as cafile:
            yield Test(
                accept=accept,
                description=description,
                host=host,
                port=port,
                cafile=cafile
            )


badssl_tests = [
    badssl(False, "expired", "expired certificate"),
    badssl(False, "wrong.host", "wrong hostname in certificate"),
    badssl(False, "self-signed", "self-signed certificate"),
    badssl(True, "sha256", "SHA-256 signature"),
    badssl(True, "1000-sans", "1000 subjectAltNames"),
    badssl(False, "incomplete-chain", "incomplete chain of trust"),
    badssl(False, "superfish", "Superfish CA"),
    badssl(False, "edellroot", "eDellRoot CA"),
    badssl(False, "dsdtestprovider", "DSDTestProvider CA")
]


ssllabs_tests = [
    ssllabs(False, 10443, "protect against an OS X vulnerability"),
    ssllabs(False, 10444, "protect against the FREAK attack"),
    ssllabs(False, 10445, "protect against the Logjam attack")
]


local_tests = [
    local(True, "localhost", "valid localhost certificate"),
    local(False, "nothing", "invalid localhost certificate"),
    badssl_onlymyca("use only the given CA bundle, not system's")
]


all_tests = badssl_tests + ssllabs_tests + local_tests
