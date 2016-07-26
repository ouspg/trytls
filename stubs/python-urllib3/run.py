import urllib3
import sys
import certifi

if len(sys.argv) < 3 or len(sys.argv) > 4:
    exit("Usage: %s <URL> <PORT> [CA_FILE]" % sys.argv[0])

cert = sys.argv[3] if len(sys.argv) > 3 else certifi.where()

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',  # Force certificate check.
    ca_certs=cert
)

try:
    r = http.request('GET', "https://{}:{}".format(sys.argv[1], sys.argv[2]))
    print("VERIFY SUCCESS")
except (urllib3.exceptions.SSLError, urllib3.exceptions.SubjectAltNameWarning) as e:
    print e
    print("VERIFY FAILURE")
else:
    pass
