import ssl
import functools
from ..testenv import constant, badssl, badssl_onlymyca, local as _local


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
