import sys
import requests

host = sys.argv[1]
port = sys.argv[2]
verify = sys.argv[3] if len(sys.argv) > 3 else True

try:
    r = requests.get("https://" + host + ":" + port, verify=verify)
except requests.exceptions.SSLError as err:
    print ("VERIFY REJECT")
else:
    print("VERIFY ACCEPT")
