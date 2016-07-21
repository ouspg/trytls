```
ouspg01:trytls mamietti$ trytls https python stubs/python-urllib3/run.py
platform: OS X 10.11.5
runner: trytls 0.1.0 (CPython 2.7.10, OpenSSL 0.9.8zh)
stub: python 'stubs/python-urllib3/run.py'
 PASS expired certificate [reject expired.badssl.com:443]
      output: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:590)
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
      output: hostname 'wrong.host.badssl.com' doesn't match either of '*.badssl.com', 'badssl.com'
 PASS self-signed certificate [reject self-signed.badssl.com:443]
      output: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:590)
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 FAIL incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 PASS Superfish CA [reject superfish.badssl.com:443]
      output: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:590)
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
      output: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:590)
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
      output: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:590)
 PASS protect against an OS X vulnerability [reject www.ssllabs.com:10443]
      output: [SSL: TLSV1_ALERT_PROTOCOL_VERSION] tlsv1 alert protocol version (_ssl.c:590)
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
      output: [SSL: UNEXPECTED_MESSAGE] unexpected message (_ssl.c:590)
 FAIL protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS valid localhost certificate [accept localhost:63256]
      output: /Users/mamietti/Library/Python/2.7/lib/python/site-packages/urllib3/connection.py:303: SubjectAltNameWarning: Certificate for localhost has no `subjectAltName`, falling back to check for a `commonName` for now. This feature is being removed by major browsers and deprecated by RFC 2818. (See https://github.com/shazow/urllib3/issues/497 for details.)  SubjectAltNameWarning
 PASS invalid localhost certificate [reject localhost:63261]
      output: /Users/mamietti/Library/Python/2.7/lib/python/site-packages/urllib3/connection.py:303: SubjectAltNameWarning: Certificate for localhost has no `subjectAltName`, falling back to check for a `commonName` for now. This feature is being removed by major browsers and deprecated by RFC 2818. (See https://github.com/shazow/urllib3/issues/497 for details.)  SubjectAltNameWarninghostname 'localhost' doesn't match u'nothing'
 FAIL use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```
---
```
platform: Linux (Ubuntu 16.04)
runner: trytls 0.1.0 (CPython 2.7.11+, OpenSSL 1.0.2g-fips)
stub: python 'stubs/python-urllib3/run.py'
 PASS expired certificate [reject expired.badssl.com:443]
      output: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:590)
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
      output: hostname 'wrong.host.badssl.com' doesn't match either of '*.badssl.com', 'badssl.com'
 PASS self-signed certificate [reject self-signed.badssl.com:443]
      output: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:590)
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
      output: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:590)
 PASS Superfish CA [reject superfish.badssl.com:443]
      output: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:590)
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
      output: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:590)
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
      output: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:590)
 PASS protect against an OS X vulnerability [reject www.ssllabs.com:10443]
      output: [SSL: BAD_SIGNATURE] bad signature (_ssl.c:590)
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
      output: [SSL: UNEXPECTED_MESSAGE] unexpected message (_ssl.c:590)
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
      output: [SSL: SSL_NEGATIVE_LENGTH] dh key too small (_ssl.c:590)
 PASS valid localhost certificate [accept localhost:42490]
      output: /usr/lib/python2.7/dist-packages/urllib3/connection.py:266: SubjectAltNameWarning: Certificate for localhost has no `subjectAltName`, falling back to check for a `commonName` for now. This feature is being removed by major browsers and deprecated by RFC 2818. (See https://github.com/shazow/urllib3/issues/497 for details.)  SubjectAltNameWarning
 PASS invalid localhost certificate [reject localhost:41925]
      output: /usr/lib/python2.7/dist-packages/urllib3/connection.py:266: SubjectAltNameWarning: Certificate for localhost has no `subjectAltName`, falling back to check for a `commonName` for now. This feature is being removed by major browsers and deprecated by RFC 2818. (See https://github.com/shazow/urllib3/issues/497 for details.)  SubjectAltNameWarninghostname 'localhost' doesn't match u'nothing'
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
      output: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:590)
```
