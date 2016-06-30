import subprocess

test = [
    "expired",
    "wrong.host",
    "self-signed",
    "sha256",
    "1000-sans",
    "10000-sans",
    "incomplete-chain",
    "rsa8192",
    "cbc",
    "rc4",
    "mozilla-old",
    "mozilla-intermediate",
    "mozilla-modern",
    "dh480",
    "dh1024",
    "dh2048",
    "dh-small-subgroup",
    "dh-composite",
    "hsts",
    "upgrade",
    "preloaded-hsts",
    "subdomain.preloaded-hsts",
    "http",
    "http-password",
    "pinning-test",
    "superfish",
    "edellroot",
    "dsdtestprovider"
]


for t in test:
    url = "https://%s.badssl.com/" % t
    try:
        subprocess.check_output(["/usr/bin/python", "python-urllib3.py", url],
                                stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print("FAIL: %s (%s)" % (url, e.output))
    else:
        print("PASS: %s" % url)
