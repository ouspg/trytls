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

[C#-Net][ PASS ][VERIFY ACCEPT][ Valid cert ][google.com]

[C#-Net][ PASS ][VERIFY REJECT][ dh480                         ][dh480.badssl.com]
[C#-Net][ PASS ][VERIFY REJECT][ dsdtestprovider               ][dsdtestprovider.badssl.com]
[C#-Net][ PASS ][VERIFY REJECT][ edellroot                     ][edellroot.badssl.com]
[C#-Net][ PASS ][VERIFY REJECT][ expired                       ][expired.badssl.com]
[C#-Net][ PASS ][VERIFY REJECT][ self-signed                   ][self-signed.badssl.com]
[C#-Net][ PASS ][VERIFY REJECT][ superfish                     ][superfish.badssl.com]
[C#-Net][ PASS ][VERIFY REJECT][ untrusted-root                ][untrusted-root.badssl.com]
[C#-Net][ PASS ][VERIFY REJECT][ wrong host                    ][wrong.host.badssl.com]
[C#-Net][ PASS ][VERIFY ACCEPT][ sha-256                       ][sha256.badssl.com]
[C#-Net][ PASS ][VERIFY ACCEPT][ supports SNI                  ][badssl.com]
[C#-Net][ OK?  ][ UNSUPPORTED  ][ disable ca-bundles            ][badssl.com]
[C#-Net][ OK?  ][VERIFY REJECT][ dh1024                        ][dh1024.badssl.com]
[C#-Net][ OK?  ][VERIFY REJECT][ dh-small-subgroup             ][dh-small-subgroup.badssl.com]
[C#-Net][ OK?  ][VERIFY REJECT][ incomplete-chain              ][incomplete-chain.badssl.com]
[C#-Net][ OK?  ][VERIFY REJECT][ mozilla-intermediate          ][mozilla-intermidiate.badssl.com]
[C#-Net][ OK?  ][VERIFY REJECT][ mozilla-modern                ][mozilla-modern.badssl.com]
[C#-Net][ OK?  ][VERIFY REJECT][ subdomain.preloaded-hsts      ][subdomain.preloaded-hsts.badssl.com]
[C#-Net][ OK?  ][VERIFY ACCEPT][ cbc                           ][cbc.badssl.com]
[C#-Net][ OK?  ][VERIFY ACCEPT][ hsts                          ][hsts.badssl.com]
[C#-Net][ OK?  ][VERIFY ACCEPT][ mixed                         ][mixed.badssl.com]
[C#-Net][ OK?  ][VERIFY ACCEPT][ mixed-favicon                 ][mixed-favicon.badssl.com]
[C#-Net][ OK?  ][VERIFY ACCEPT][ mixed-script                  ][mixed-script.badssl.com]
[C#-Net][ OK?  ][VERIFY ACCEPT][ mozilla-old                   ][mozilla-old.badssl.com]
[C#-Net][ OK?  ][VERIFY ACCEPT][ pinning-test                  ][pinning-test.badssl.com]
[C#-Net][ OK?  ][VERIFY ACCEPT][ preloaded-hsts                ][preloaded-hsts.badssl.com]
[C#-Net][ OK?  ][VERIFY ACCEPT][ rc4                           ][rc4.badssl.com]
[C#-Net][ OK?  ][VERIFY ACCEPT][ rsa8192                       ][rsa8192.badssl.com]
[C#-Net][ OK?  ][VERIFY ACCEPT][ sha1-2016                     ][sha1-2016.badssl.com]
[C#-Net][ OK?  ][VERIFY ACCEPT][ sha1-2017                     ][sha1-2017.badssl.com]
[C#-Net][ OK?  ][VERIFY ACCEPT][ upgrade                       ][upgrade.badssl.com]
[C#-Net][ OK?  ][VERIFY ACCEPT][ very                          ][very.badssl.com]
[C#-Net][ FAIL ][VERIFY REJECT][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
[C#-Net][ FAIL ][VERIFY REJECT][ 1000-sans                     ][1000-sans.badssl.com]
[C#-Net][ FAIL ][VERIFY REJECT][ dh2048                        ][dh2048.badssl.com]

[C#-Net][ PASS ][VERIFY REJECT][ OS X vulnerability  ][www.ssllabs.com]
[C#-Net][ PASS ][VERIFY REJECT][ Freak               ][www.ssllabs.com]
[C#-Net][ PASS ][VERIFY REJECT][ Logjam              ][www.ssllabs.com]

```
