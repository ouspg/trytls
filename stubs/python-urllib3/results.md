platform: OS X 10.11.5
runner: trytls 0.0.8 (CPython 2.7.10, OpenSSL 0.9.8zh)
stub: python 'stubs/python-urllib3/run.py'
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
ERROR valid localhost certificate [accept localhost:54543]
      reason: unexpected output
      output: /Users/mamietti/Library/Python/2.7/lib/python/site-packages/urllib3/connection.py:303: SubjectAltNameWarning: Certificate for localhost has no `subjectAltName`, falling back to check for a `commonName` for now. This feature is being removed by major browsers and deprecated by RFC 2818. (See https://github.com/shazow/urllib3/issues/497 for details.)
                SubjectAltNameWarning
              VERIFY SUCCESS
ERROR invalid localhost certificate [reject localhost:54548]
      reason: unexpected output
      output: /Users/mamietti/Library/Python/2.7/lib/python/site-packages/urllib3/connection.py:303: SubjectAltNameWarning: Certificate for localhost has no `subjectAltName`, falling back to check for a `commonName` for now. This feature is being removed by major browsers and deprecated by RFC 2818. (See https://github.com/shazow/urllib3/issues/497 for details.)
                SubjectAltNameWarning
              VERIFY FAILURE
 FAIL use only the given CA bundle, not system's [reject sha256.badssl.com:443]
