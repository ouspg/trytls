import sys
import requests


host = sys.argv[1]
port = sys.argv[2]
cafile = sys.argv[3] if len(sys.argv) > 3 else False

try:
    r = requests.get("https://" + host + ":" + port, cert=cafile)
except requests.exceptions.SSLError as err:
    #    print err
    print ("VERIFY FAILURE")
else:
    print("VERIFY SUCCESS")
