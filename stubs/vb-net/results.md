```
Mono JIT compiler version 4.5.2
Visual Basic.Net Compiler version 0.0.0.5943 (Mono 4.0.1 - tarball)

Do not use old compilers if it is not required for some reason.
For example Mono JIT compiler version 4.2.1 which is the currently (7.20.2016) default version 
when installed using apt-get FAILS the expired certificate test.

```

```

platform: Linux (Ubuntu 16.04)
runner: trytls 0.1.0 (CPython 2.7.12, OpenSSL 1.0.2g-fips)
stub: VB-Net 'Run.exe'
 PASS expired certificate [reject expired.badssl.com:443]
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 FAIL 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 PASS Superfish CA [reject superfish.badssl.com:443]
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
 PASS protect against an OS X vulnerability [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 SKIP valid localhost certificate [accept localhost:36162]
 SKIP invalid localhost certificate [reject localhost:44585]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
 
```

```

platform: Linux (Ubuntu 16.04)
runner: simplerunner
stub: VB-Net 'Run.exe'

[VB-Net][ PASS ][ACCEPT][ Valid cert ][google.com]

[VB-Net][ PASS ][REJECT][ dh480                         ][dh480.badssl.com]
[VB-Net][ PASS ][REJECT][ dsdtestprovider               ][dsdtestprovider.badssl.com]
[VB-Net][ PASS ][REJECT][ edellroot                     ][edellroot.badssl.com]
[VB-Net][ PASS ][REJECT][ expired                       ][expired.badssl.com]
[VB-Net][ PASS ][REJECT][ self-signed                   ][self-signed.badssl.com]
[VB-Net][ PASS ][REJECT][ superfish                     ][superfish.badssl.com]
[VB-Net][ PASS ][REJECT][ untrusted-root                ][untrusted-root.badssl.com]
[VB-Net][ PASS ][REJECT][ wrong host                    ][wrong.host.badssl.com]
[VB-Net][ PASS ][ACCEPT][ sha-256                       ][sha256.badssl.com]
[VB-Net][ PASS ][ACCEPT][ supports SNI                  ][badssl.com]
[VB-Net][ OK?  ][ UNSUPPORTED  ][ disable ca-bundles            ][badssl.com]
[VB-Net][ OK?  ][REJECT][ dh1024                        ][dh1024.badssl.com]
[VB-Net][ OK?  ][REJECT][ dh-small-subgroup             ][dh-small-subgroup.badssl.com]
[VB-Net][ OK?  ][REJECT][ incomplete-chain              ][incomplete-chain.badssl.com]
[VB-Net][ OK?  ][REJECT][ mozilla-intermediate          ][mozilla-intermidiate.badssl.com]
[VB-Net][ OK?  ][REJECT][ mozilla-modern                ][mozilla-modern.badssl.com]
[VB-Net][ OK?  ][REJECT][ subdomain.preloaded-hsts      ][subdomain.preloaded-hsts.badssl.com]
[VB-Net][ OK?  ][ACCEPT][ cbc                           ][cbc.badssl.com]
[VB-Net][ OK?  ][ACCEPT][ hsts                          ][hsts.badssl.com]
[VB-Net][ OK?  ][ACCEPT][ mixed                         ][mixed.badssl.com]
[VB-Net][ OK?  ][ACCEPT][ mixed-favicon                 ][mixed-favicon.badssl.com]
[VB-Net][ OK?  ][ACCEPT][ mixed-script                  ][mixed-script.badssl.com]
[VB-Net][ OK?  ][ACCEPT][ mozilla-old                   ][mozilla-old.badssl.com]
[VB-Net][ OK?  ][ACCEPT][ pinning-test                  ][pinning-test.badssl.com]
[VB-Net][ OK?  ][ACCEPT][ preloaded-hsts                ][preloaded-hsts.badssl.com]
[VB-Net][ OK?  ][ACCEPT][ rc4                           ][rc4.badssl.com]
[VB-Net][ OK?  ][ACCEPT][ rsa8192                       ][rsa8192.badssl.com]
[VB-Net][ OK?  ][ACCEPT][ sha1-2016                     ][sha1-2016.badssl.com]
[VB-Net][ OK?  ][ACCEPT][ sha1-2017                     ][sha1-2017.badssl.com]
[VB-Net][ OK?  ][ACCEPT][ upgrade                       ][upgrade.badssl.com]
[VB-Net][ OK?  ][ACCEPT][ very                          ][very.badssl.com]
[VB-Net][ FAIL ][REJECT][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
[VB-Net][ FAIL ][REJECT][ 1000-sans                     ][1000-sans.badssl.com]
[VB-Net][ FAIL ][REJECT][ dh2048                        ][dh2048.badssl.com]

[VB-Net][ PASS ][REJECT][ OS X vulnerability  ][www.ssllabs.com]
[VB-Net][ PASS ][REJECT][ Freak               ][www.ssllabs.com]
[VB-Net][ PASS ][REJECT][ Logjam              ][www.ssllabs.com]

```
