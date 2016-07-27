# OS X OpenSSL verification surprises

When using native python shipped with OS X, the system default bundle will be
trusted even if instructed otherwise. This is troubling, as some organizations
do not want to trust the default bundles. Also, lately, the reputation of some
CAs have been [brought into question](https://news.ycombinator.com/item?id=11781915).


## Not a new issue

This issue has been
[reported](https://hynek.me/articles/apple-openssl-verification-surprises/)
already 2014-03-03 by [Hynek Schlawack](https://hynek.me/).
[CVE-2014-2234](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-2234)
describes the vulnerability exists on *A certain Apple patch for OpenSSL in
Apple OS X 10.9.2*. However, we have reproduced it in OS X 10.11.5 (15F34)
2016-06-12. The same behavior was observed with other python libraries
(e.g. [urllib3](https://pypi.python.org/pypi/urllib3), and
[requests](http://docs.python-requests.org/en/master/)) - as long as the
python shipped with OS X was used.

## How we found it

The issue was rediscovered with TryTLS. TryTLS is a tool which checks if programming
languages and libraries verify TLS certificates correctly. While developing the
tool, we found an unexpected behavior. Apple's patch to their OpenSSL, apparently
made [back in 2011](https://daniel.haxx.se/blog/2011/11/05/apples-modified-ca-cert-handling-and-curl/),  
gives the user of OpenSSL more CAs than she bargained for. If the certificate check
fails with  user provided CA, Apple's OpenSSL *gives failed verifications a
second chance using the system keyring as trust store.*


# Suggested workarounds
 * User: avoid running python code with native OS X python installation
 * Developer: consider warning users if OS X native python is used
    and non-ca-bundle is set by the user.

# Tested Versions

### Code used for testing

The tests were run using a [stub](https://github.com/ouspg/trytls/blob/43660507b45a59e01d7205df5ad98c704c8a555d/stubs/python-urllib2/run.py) developed for [TryTLS](https://github.com/ouspg/trytls/).

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

## Tests


## No CA cert bundle defined - succeeds as expected

```
$ /System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7 stubs/python-urllib2/run.py sha256.badssl.com 443
ACCEPT
```

## CA cert bundle defined - succeeds unexpectedly
```
$ /System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7 stubs/python-urllib2/run.py sha256.badssl.com 443 pki/certs/theonlycertitrust.crt
ACCEPT
```

## Apple's TEA-patch disabled - fails as expected

```
$ env OPENSSL_X509_TEA_DISABLE=1 /System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7 stubs/python-urllib2/run.py sha256.badssl.com 443
REJECT
```
## Running with brew-installed third party python interpreter - fails as expected

```
$ /usr/local/bin/python stubs/python-urllib2/run.py sha256.ssllabs.com 443 pki/certs/theonlycertitrust.crt
REJECT
```
