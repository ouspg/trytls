import sys
import idiokit
from idiokit import socket, ssl

@idiokit.stream
def client(host, port, cafile):
    sock = socket.Socket()
    yield sock.connect((host, port))

    if cafile:
        ssl_sock = yield ssl.wrap_socket(sock, require_cert=True, ca_certs=cafile)
    else:
        ssl_sock = yield ssl.wrap_socket(sock, require_cert=True)
    cert = yield ssl_sock.getpeercert()
    ssl.match_hostname(cert, host)

if len(sys.argv) < 3 or len(sys.argv) > 4:
    exit("Usage: %s <HOST> <PORT> [CA_FILE]" % sys.argv[0])

host = sys.argv[1]
port = sys.argv[2]
cafile = sys.argv[3] if len(sys.argv) > 3 else None

try:
    idiokit.main_loop(client(host, int(port), cafile))
    print "ACCEPT"
except idiokit.ssl.SSLError:
    print "REJECT"
else:
    pass
