import ssl
import functools
from ..testenv import badssl, local as _local


def https_callback(conn, certfile, keyfile):
    s = ssl.wrap_socket(conn, server_side=True, certfile=certfile, keyfile=keyfile)
    s.sendall(b"HTTP/1.0 200 OK\r\nContent-Length: 0\r\n\r\n")


local = functools.partial(_local, callback=https_callback)


badssl_tests = [
    badssl(True, "sha1-2016"),
    badssl(False, "expired")
]


local_tests = [
    local(True, "localhost"),
    local(False, "nothing")
]


all_tests = badssl_tests + local_tests
