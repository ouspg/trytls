import sys
import ssl
import imaplib

host = sys.argv[1]
port = int(sys.argv[2])
cafile = sys.argv[3] if len(sys.argv) > 3 else None

if cafile is None:
    ssl_context = ssl.create_default_context()
else:
    ssl_context = ssl.create_default_context(cafile=cafile)

try:
    imaplib.IMAP4_SSL(host, port, ssl_context=ssl_context)
except (ssl.SSLError, ssl.CertificateError):
    print("FAIL")
else:
    print("OK")
