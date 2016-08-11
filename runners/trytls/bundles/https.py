from __future__ import print_function, unicode_literals

import re
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


BADTLS_CA_DATA = """
-----BEGIN CERTIFICATE-----
MIIDlTCCAn+gAwIBAgIIVvpPzLyqk+0wCwYJKoZIhvcNAQELMGoxaDAJBgNVBAYT
AlVTMBQGA1UECAwNTWFzc2FjaHVzZXR0czAOBgNVBAcMB05ld2J1cnkwFgYDVQQK
DA9CYWQgVExTIExpbWl0ZWQwHQYDVQQDDBZCYWQgVExTIExpbWl0ZWQgUlNBIENB
MB4XDTE2MDEwMTAwMDAwMFoXDTI2MDEwMTAwMDAwMFowajFoMAkGA1UEBhMCVVMw
FAYDVQQIDA1NYXNzYWNodXNldHRzMA4GA1UEBwwHTmV3YnVyeTAWBgNVBAoMD0Jh
ZCBUTFMgTGltaXRlZDAdBgNVBAMMFkJhZCBUTFMgTGltaXRlZCBSU0EgQ0EwggEi
MA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDSHu3OR1RS0D2xLKGK2Ts5eLoO
/P+IXst5WPdaD9UwGI8edfAy3U8wcMFDoXNhBQM+ZW69Z5uOZVxs704+j5cgCEAT
LbtyIrF2X8BixXFzrJFd+kpojURheyxML20GbZsznJgKzYvGqFqWa/1lYwy/v0SP
RNGPEkjFXb/tItDwrDxcuDzY6zjNlW5MwqvS11P1H8eg0idUrANY2MzT8+oyH3Sn
JLCsmulnmj1b6IZZDN4i8rKXEbH14jIsANHIgTqvS+kJf3Z1PqHAOUqVGlO3SDZd
KIqZ8olS6ty9/pco6cxvX2Te9m1z5f1fSrdxAtx7lHM3pdvs9DhML+8FAewDAgMB
AAGjQzBBMA8GA1UdEwEB/wQFMAMBAf8wHQYDVR0OBBYEFGEbxkZbhgwiZRAMx7Vs
VCRXl/tkMA8GA1UdDwEB/wQFAwMHBgAwCwYJKoZIhvcNAQELA4IBAQBKv0TJoRhd
wg7dPOFDVuKaLtuVzXEeUWfsA86iW4wjXFO/npI+1exSBX92MhsWk5Gjn9dO/Hq4
EZ1pMJ8hFdrOXoEHlvhnZSavtoy25ZvEoxJ9XWYPqWCmwdfB3xhT4hoEaIlu5Azf
Fw/QV5oFV8SYgwClQ+fTStxdW7CBKEX55KPUn4FOOXV5TfbLOJj3w/1V2pBTKn2f
2safgWyIpNw7OyvYVICdW5/NvD+VTBp+4PfWkTfRD5LEAxqvaGXupBaI2qGYVibJ
WQ77yy6bOvcJh4heqtIJuYg5F3vhvSGo4i5Bkx+daRKFzFwsoiexgRNTdlPCEGsQ
15WBlk3X/9bt
-----END CERTIFICATE-----
"""


def _split_address(address):
    """
    Return (host, port) split from a string in form of "host:port".
    The host part is returned as a string, port as int.

    >>> host, port = _split_address("host.example.com:10000")
    >>> print(host, port)
    host.example.com 10000
    >>> isinstance(host, type(""))
    True
    >>> isinstance(port, int)
    True

    Raise ValueError for values that are not valid "host:port" strings.

    >>> _split_address("host.example.com")
    Traceback (most recent call last):
        ...
    ValueError: invalid address 'host.example.com'

    >>> _split_address(":10000")
    Traceback (most recent call last):
        ...
    ValueError: invalid address ':10000'

    In addition to being an integer the port value should be between 1-65535,
    inclusive.

    >>> _split_address("host:0")
    Traceback (most recent call last):
        ...
    ValueError: invalid port 0

    >>> _split_address("host:65536")
    Traceback (most recent call last):
        ...
    ValueError: invalid port 65536
    """

    match = re.match(r"^(\S+):(\d+)$", address)
    if not match:
        raise ValueError("invalid address '{}'".format(address))

    host, port = match.groups()
    port = int(port)
    if not (1 <= port <= 65535):
        raise ValueError("invalid port {}".format(port))

    return host, port


@testenv
def badtls(accept, address, description=None):
    host, port = _split_address(address)

    if description is None:
        first, _, _ = host.partition(".")
        description = first.replace("-", " ")

    with tmpfiles(BADTLS_CA_DATA) as cafile:
        yield Test(
            accept=accept,
            description=description,
            host=host,
            port=port,
            cafile=cafile
        )


@testenv
def badssl(accept, name, description):
    yield Test(
        accept=accept,
        description=description,
        host=name + ".badssl.com",
        port=443
    )


@testenv
def badssl_sni(description):
    yield Test(
        accept=True,
        description=description,
        host="badssl.com",
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


@testenv
def freakattack(host, description):
    yield Test(
        accept=False,
        description=description,
        host=host,
        port=443
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


@testenv
def miscellaneous(accept, name, description):
    yield Test(
        accept=accept,
        description=description,
        host=name,
        port=443
    )


badssl_tests = [
    badssl_sni(description="support for TLS server name indication (SNI)"),
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
    ssllabs(False, 10443, "protect against Apple's TLS vulnerability CVE-2014-1266"),
    ssllabs(False, 10444, "protect against the FREAK attack"),
    ssllabs(False, 10445, "protect against the Logjam attack")
]

freakattack_tests = [
    freakattack("cve.freakattack.com", "protect against FREAK attack (test server 1)"),
    freakattack("cve2.freakattack.com", "protect against FREAK attack (test server 2)"),
]

badtls_tests = [
    badtls(True, "domain-match.badtls.io:10000"),
    badtls(True, "wildcard-match.badtls.io:10001"),
    badtls(True, "san-match.badtls.io:10002"),
    badtls(True, "dh1024.badtls.io:10005"),
    badtls(False, "expired-1963.badtls.io:11000"),
    badtls(False, "future.badtls.io:11001"),
    badtls(False, "domain-mismatch.badtls.io:11002"),
    badtls(False, "san-mismatch.badtls.io:11003"),
    badtls(False, "weak-sig.badtls.io:11004"),
    badtls(False, "bad-key-usage.badtls.io:11005"),
    badtls(False, "expired.badtls.io:11006"),
    badtls(False, "wildcard.mismatch.badtls.io:11007", "wildcard mismatch"),
    badtls(False, "rc4.badtls.io:11008"),
    badtls(False, "rc4-md5.badtls.io:11009")
]

local_tests = [
    local(True, "localhost", "valid localhost certificate"),
    local(False, "nothing", "invalid localhost certificate"),
    badssl_onlymyca("use only the given CA bundle, not system's")
]

miscellaneous_tests = [
    miscellaneous(False, "sslv3.dshield.org", "protection against POODLE attack"),
    miscellaneous(False, "badcert-edell.tlsfun.de", "eDellRoot CA #2")
]

all_tests = badtls_tests + badssl_tests + ssllabs_tests + freakattack_tests + local_tests + miscellaneous_tests
