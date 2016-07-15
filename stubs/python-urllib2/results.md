```
platform: OS X 10.11.5
runner: trytls 0.1.0 (CPython 2.7.10, OpenSSL 0.9.8zh)
stub: python 'stubs/python-urllib2/run.py'
 PASS expired certificate [reject expired.badssl.com:443]
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 FAIL incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 PASS Superfish CA [reject superfish.badssl.com:443]
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
 PASS protect against an OS X vulnerability [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 FAIL protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS valid localhost certificate [accept localhost:54584]
 PASS invalid localhost certificate [reject localhost:54588]
 FAIL use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```
