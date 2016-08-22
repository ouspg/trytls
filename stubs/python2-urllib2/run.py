import sys
import ssl
import urllib2

if len(sys.argv) < 3 or len(sys.argv) > 4:
    exit("Usage: %s <HOST> <PORT> [CA_FILE]" % sys.argv[0])

host = sys.argv[1]
port = sys.argv[2]
cafile = sys.argv[3] if len(sys.argv) > 3 else None

# Python 2.7.9 added the cafile argument support to urllib2.urlopen. Some
# distributions have also backported the support to nominally earlier versions
# so a basic version number check won't be sufficient.
# As a workaround pass in the cafile argument only if needed, and prepare to
# catch the TypeError if the used urllib2.urlopen doesn't support cafile yet.
kwargs = {} if cafile is None else {"cafile": cafile}
try:
    urllib2.urlopen("https://" + host + ":" + port, **kwargs)
except TypeError:
    if not kwargs:
        raise
    print "UNSUPPORTED"
except getattr(ssl, "CertificateError", ()):
    print("REJECT")
except urllib2.URLError as exc:
    if not isinstance(exc.reason, ssl.SSLError):
        raise
    print("REJECT")
else:
    print("ACCEPT")
