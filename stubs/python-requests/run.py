import requests
import sys

if len(sys.argv) < 3:
    exit("Usage: %s <HOST> <PORT> [CA_FILE]" % sys.argv[0])

cert = sys.argv[3] if len(sys.argv) > 3 else True


try:
    r = requests.get("https://{}:{}".format(sys.argv[1], sys.argv[2]), verify=cert)
    print("VERIFY SUCCESS")
except requests.exceptions.SSLError:
    print("VERIFY FAILURE")
else:
    pass
