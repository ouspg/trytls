```
platform: Linux (Ubuntu 16.04)
runner: trytls 0.1.0 (CPython 2.7.11+, OpenSSL 1.0.2g-fips)
stub: 'lua5.1' 'stubs/lua5.1-luasec/run.lua'
 PASS expired certificate [reject expired.badssl.com:443]
      output: certificate verify failed
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
      output: wrong hostname
 PASS self-signed certificate [reject self-signed.badssl.com:443]
      output: certificate verify failed
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
      output: certificate verify failed
 PASS Superfish CA [reject superfish.badssl.com:443]
      output: certificate verify failed
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
      output: certificate verify failed
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
      output: certificate verify failed
 PASS protect against an OS X vulnerability [reject www.ssllabs.com:10443]
      output: bad signature
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
      output: unexpected message
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
      output: dh key too small
 PASS valid localhost certificate [accept localhost:40469]
 PASS invalid localhost certificate [reject localhost:33341]
      output: wrong hostname
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
      output: certificate verify failed
```
