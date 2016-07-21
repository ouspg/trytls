```
platform: Linux (Ubuntu 16.04)
runner: trytls 0.1.0 (CPython 2.7.11+, OpenSSL 1.0.2g-fips)
stub: 'lua5.1' 'stubs/lua5.1-luasec/run.lua'
 PASS expired certificate [reject expired.badssl.com:443]
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 PASS Superfish CA [reject superfish.badssl.com:443]
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
 PASS protect against an OS X vulnerability [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS valid localhost certificate [accept localhost:36096]
 PASS invalid localhost certificate [reject localhost:32880]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```
