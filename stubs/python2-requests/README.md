
# Requirements

This stub has been tested with:
 * Python 2.7.12
 * [requests-library](http://docs.python-requests.org/en/master/) v.2.10

# Examples

```sh
$ python stubs/python2-requests/run.py sha256.badssl.com 443
ACCEPT

python stubs/python2-requests/run.py expired.badssl.com 443
REJECT

$ python stubs/python2-requests/run.py sha256.badssl.com 443 <path>/pki/certs/theonlycertitrust.crt
REJECT
```

# Credits

Based on python3-urllib -stub.
