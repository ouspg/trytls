platform: OS X 10.11.5
runner: trytls 0.0.8 (CPython 2.7.10, OpenSSL 0.9.8zh)
stub: go run 'stubs/go-nethttp/run.go'
 PASS expired certificate [reject expired.badssl.com:443]
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 PASS Superfish CA [reject superfish.badssl.com:443]
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
ERROR protect against an OS X vulnerability [reject www.ssllabs.com:10443]
      reason: stub exited with return code 1
      output: Get https://www.ssllabs.com:10443: crypto/rsa: verification error
              exit status 1
ERROR protect against the FREAK attack [reject www.ssllabs.com:10444]
      reason: stub exited with return code 1
      output: Get https://www.ssllabs.com:10444: tls: unexpected ServerKeyExchange
              exit status 1
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 SKIP valid localhost certificate [accept localhost:54944]
 SKIP invalid localhost certificate [reject localhost:54949]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
