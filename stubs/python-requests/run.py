import sys
import requests

if len(sys.argv) < 3 or len(sys.argv) > 4:
    exit("Usage: %s <URL> <PORT> [CA_FILE]" % sys.argv[0])

host = sys.argv[1]
port = sys.argv[2]
verify = sys.argv[3] if len(sys.argv) > 3 else True

try:
    r = requests.get("https://" + host + ":" + port, verify=verify)
except requests.exceptions.SSLError as err:
    print ("VERIFY FAILURE")
else:
    print("VERIFY SUCCESS")
