import sys
import idiokit
from idiokit import socket, ssl

@idiokit.stream
def client(host, port):
    sock = socket.Socket()
    yield sock.connect((host, port))

    ssl_sock = yield ssl.wrap_socket(sock, require_cert=True)
    cert = yield ssl_sock.getpeercert()
    ssl.match_hostname(cert, host)


host = sys.argv[1]
port = sys.argv[2]

try:
    idiokit.main_loop(client(host, int(port)))
    print "VERIFY SUCCESS"
except idiokit.ssl.SSLError:
    print "VERIFY FAILURE"
