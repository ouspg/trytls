import sys
import ssl
import urllib.error
import urllib.request

host = sys.argv[1]
port = sys.argv[2]
cafile = sys.argv[3] if len(sys.argv) > 3 else None

try:
    urllib.request.urlopen("https://" + host + ":" + port, cafile=cafile)
except ssl.CertificateError:
    print("VERIFY FAILURE")
except urllib.error.URLError as exc:
    if not isinstance(exc.reason, ssl.SSLError):
        raise
    print("VERIFY FAILURE")
else:
    print("VERIFY SUCCESS")
