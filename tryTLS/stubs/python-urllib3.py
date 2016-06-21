import urllib3
import sys

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',  # Force certificate check.
    ca_certs='/etc/ssl/certs/ca-bundle.crt'
)

if len(sys.argv) < 2:
    exit("Usage: %s <URL>" % sys.argv[0])
try:
    r = http.request('GET', sys.argv[1])
except Exception as e:
    exit("%s" % e)
else:
    exit(0)
