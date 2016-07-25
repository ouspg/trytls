
# Requirements

This stub has been tested with:
 * Python 2.7.12
 * [requests-library](http://docs.python-requests.org/en/master/) v.2.10

# Examples

```sh
$ python stubs/python-requests/run.py sha256.badssl.com 443
VERIFY ACCEPT

python stubs/python-requests/run.py expired.badssl.com 443
VERIFY REJECT

$ python stubs/python-requests/run.py sha256.badssl.com 443 <path>/pki/certs/theonlycertitrust.crt
VERIFY REJECT
```

# Credits

Based on python3-urllib -stub.
