import socket
from ..testenv import testenv


@testenv
def gmail():
    yield True, "imap.gmail.com", 993, None


@testenv
def gmail_fail():
    for (_, _, _, _, (host, port)) in socket.getaddrinfo("imap.gmail.com", 993):
        yield False, host, port, None
        break


gmail_tests = [
    gmail(),
    gmail_fail()
]


all_tests = gmail_tests
