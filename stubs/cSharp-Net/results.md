```
Mono JIT compiler version 4.5.2
Mono C# compiler version 4.5.2.0

Do not use old compilers if it is not required for some reason.
For example Mono JIT compiler version 4.2.1 which is the currently (7.20.2016) default version 
when installed using apt-get FAILS the expired certificate test.

```

```

platform: Linux (Ubuntu 16.04)
runner: trytls 0.1.0 (CPython 2.7.12, OpenSSL 1.0.2g-fips)
stub: cSharp-Net 'Run.exe'
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
stub: cSharp-Net 'run.exe'

[C#-Net][ PASS ][VERIFY SUCCESS][ Valid cert ][google.com]

[C#-Net][ PASS ][VERIFY FAILURE][ dh480                         ][dh480.badssl.com]
[C#-Net][ PASS ][VERIFY FAILURE][ dsdtestprovider               ][dsdtestprovider.badssl.com]
[C#-Net][ PASS ][VERIFY FAILURE][ edellroot                     ][edellroot.badssl.com]
[C#-Net][ PASS ][VERIFY FAILURE][ expired                       ][expired.badssl.com]
[C#-Net][ PASS ][VERIFY FAILURE][ self-signed                   ][self-signed.badssl.com]
[C#-Net][ PASS ][VERIFY FAILURE][ superfish                     ][superfish.badssl.com]
[C#-Net][ PASS ][VERIFY FAILURE][ untrusted-root                ][untrusted-root.badssl.com]
[C#-Net][ PASS ][VERIFY FAILURE][ wrong host                    ][wrong.host.badssl.com]
[C#-Net][ PASS ][VERIFY SUCCESS][ sha-256                       ][sha256.badssl.com]
[C#-Net][ PASS ][VERIFY SUCCESS][ supports SNI                  ][badssl.com]
[C#-Net][ OK?  ][ UNSUPPORTED  ][ disable ca-bundles            ][badssl.com]
[C#-Net][ OK?  ][VERIFY FAILURE][ dh1024                        ][dh1024.badssl.com]
[C#-Net][ OK?  ][VERIFY FAILURE][ dh-small-subgroup             ][dh-small-subgroup.badssl.com]
[C#-Net][ OK?  ][VERIFY FAILURE][ incomplete-chain              ][incomplete-chain.badssl.com]
[C#-Net][ OK?  ][VERIFY FAILURE][ mozilla-intermediate          ][mozilla-intermidiate.badssl.com]
[C#-Net][ OK?  ][VERIFY FAILURE][ mozilla-modern                ][mozilla-modern.badssl.com]
[C#-Net][ OK?  ][VERIFY FAILURE][ subdomain.preloaded-hsts      ][subdomain.preloaded-hsts.badssl.com]
[C#-Net][ OK?  ][VERIFY SUCCESS][ cbc                           ][cbc.badssl.com]
[C#-Net][ OK?  ][VERIFY SUCCESS][ hsts                          ][hsts.badssl.com]
[C#-Net][ OK?  ][VERIFY SUCCESS][ mixed                         ][mixed.badssl.com]
[C#-Net][ OK?  ][VERIFY SUCCESS][ mixed-favicon                 ][mixed-favicon.badssl.com]
[C#-Net][ OK?  ][VERIFY SUCCESS][ mixed-script                  ][mixed-script.badssl.com]
[C#-Net][ OK?  ][VERIFY SUCCESS][ mozilla-old                   ][mozilla-old.badssl.com]
[C#-Net][ OK?  ][VERIFY SUCCESS][ pinning-test                  ][pinning-test.badssl.com]
[C#-Net][ OK?  ][VERIFY SUCCESS][ preloaded-hsts                ][preloaded-hsts.badssl.com]
[C#-Net][ OK?  ][VERIFY SUCCESS][ rc4                           ][rc4.badssl.com]
[C#-Net][ OK?  ][VERIFY SUCCESS][ rsa8192                       ][rsa8192.badssl.com]
[C#-Net][ OK?  ][VERIFY SUCCESS][ sha1-2016                     ][sha1-2016.badssl.com]
[C#-Net][ OK?  ][VERIFY SUCCESS][ sha1-2017                     ][sha1-2017.badssl.com]
[C#-Net][ OK?  ][VERIFY SUCCESS][ upgrade                       ][upgrade.badssl.com]
[C#-Net][ OK?  ][VERIFY SUCCESS][ very                          ][very.badssl.com]
[C#-Net][ FAIL ][VERIFY FAILURE][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
[C#-Net][ FAIL ][VERIFY FAILURE][ 1000-sans                     ][1000-sans.badssl.com]
[C#-Net][ FAIL ][VERIFY FAILURE][ dh2048                        ][dh2048.badssl.com]

[C#-Net][ PASS ][VERIFY FAILURE][ OS X vulnerability  ][www.ssllabs.com]
[C#-Net][ PASS ][VERIFY FAILURE][ Freak               ][www.ssllabs.com]
[C#-Net][ PASS ][VERIFY FAILURE][ Logjam              ][www.ssllabs.com]

```
