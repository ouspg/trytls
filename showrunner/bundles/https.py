import ssl
import functools
from ..testenv import badssl, local as _local


def https_callback(conn, certfile, keyfile):
    s = ssl.wrap_socket(conn, server_side=True, certfile=certfile, keyfile=keyfile)
    s.sendall(b"HTTP/1.0 200 OK\r\nContent-Length: 0\r\n\r\n")


local = functools.partial(_local, callback=https_callback)


badssl_tests = [
    badssl(False, "expired"),  # not with an obsolete cert
    badssl(False, "wrong.host"),  # not with a wrong name
    badssl(False, "self-signed"),  # not just one's own claims
    badssl(True, "sha256"),  # future proof sha
    badssl(True, "1000-sans"),  # massive alternative names
    badssl(True, "10000-sans"),  # massive alternative names
    badssl(False, "incomplete-chain"),  # should have full proof of chain to trusted CA
    badssl(False, "pinning-test"),  # why???
    badssl(False, "superfish"),  # super fishy CA
    badssl(False, "edellroot"),  # rotten roots CA
    badssl(False, "dsdtestprovider")  # unproviding CA
]


local_tests = [
    local(True, "localhost"),
    local(False, "nothing")
]


all_tests = badssl_tests + local_tests
