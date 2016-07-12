# OS X OpenSSL Verification Surprises

TryTLS is a tool which checks if programming languages and libraries
verify TLS certificates correctly. While developing the tool, we found an unexpected behaviour. Apple's patch to their OpenSSL, apparently made [back in 2011](https://daniel.haxx.se/blog/2011/11/05/apples-modified-ca-cert-handling-and-curl/), leads into a situation, where the
user of OpenSSL gets more CA's than she bargained for. If certificate check fails with user provided CA, Apple's OpenSSL
*gives failed verifications a second chance using the system keyring as trust store.*


This issue has been
[reported](https://hynek.me/articles/apple-openssl-verification-surprises/)
already 2014-03-03 by [Hynek Schlawack](https://hynek.me/).
[CVE-2014-2234](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-2234)
describes the vulnerability exists on *A certain Apple patch for OpenSSL in Apple OS X 10.9.2*.
However, we have reproduced it in OS X 10.11.5 (15F34) 2016-06-12.







The badssl_onlymyca fails:
```
trytls https /System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7 stubs/python-urllib2/run.py
 ...
x FAIL badssl_onlymyca(False, 'sha256')
 ...

```

## Tested Versions

### Python & Urllib
```
$ /System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7
Python 2.7.10 (default, Oct 23 2015, 19:19:21)
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import urllib2
>>> urllib2
<module 'urllib2' from '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib2.pyc'>
```

### OpenSSL

```
$ /usr/bin/openssl version
OpenSSL 0.9.8zh 14 Jan 2016
```

### OS X
```
10.11.5 (15F34)
```

# Tests
## No CA cert bundle defined - Succeeds as expected
```

$ /System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7 stubs/python-urllib2/run.py sha256.badssl.com 443
VERIFY SUCCESS
```

## CA cert bundle used - Succeeds unexpectedly
```
$ /System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7 stubs/python-urllib2/run.py sha256.badssl.com 443 pki/certs/theonlycertitrust.crt
VERIFY SUCCESS
```

## Apple's TEA-patch Disabled - Fails as expected

```
/System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7 stubs/python-urllib2/run.py sha256.badssl.com 443
VERIFY SUCCESS
evilon:trytls jani$ env OPENSSL_X509_TEA_DISABLE=1 /System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7 stubs/python-urllib2/run.py sha256.badssl.com 443
VERIFY FAILURE
```
