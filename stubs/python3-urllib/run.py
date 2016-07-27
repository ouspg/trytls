import sys
import ssl
import urllib.error
import urllib.request

if len(sys.argv) < 3 or len(sys.argv) > 4:
    exit("Usage: %s <HOST> <PORT> [CA_FILE]" % sys.argv[0])

host = sys.argv[1]
port = sys.argv[2]
cafile = sys.argv[3] if len(sys.argv) > 3 else None

try:
    urllib.request.urlopen("https://" + host + ":" + port, cafile=cafile)
except ssl.CertificateError:
    print("REJECT")
except urllib.error.URLError as exc:
    if not isinstance(exc.reason, ssl.SSLError):
        raise
    print("REJECT")
else:
    print("ACCEPT")
