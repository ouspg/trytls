import urllib3
import sys

if len(sys.argv) < 2:
    exit("Usage: %s <URL> <PORT> [CA_FILE]" % sys.argv[0])

cert = None
if len(sys.argv) >= 3:
    cert = sys.argv[3]

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',  # Force certificate check.
    ca_certs=cert
)

try:
    r = http.request('GET', "https://{}:{}".format(sys.argv[1], sys.argv[2]))
except Exception as e:
    print("VERIFY FAILURE")
else:
    print("VERIFY SUCCESS")
