```
Mono JIT compiler version 4.5.2
F# Compiler for F# 4.1

Do not use old compilers if it is not required for some reason.
For example Mono JIT compiler version 4.2.1 which is the currently (7.20.2016) default version
when installed using apt-get FAILS the expired certificate test.

```

```

platform: Linux (Ubuntu 16.04)
runner: trytls 0.1.0 (CPython 2.7.12, OpenSSL 1.0.2g-fips)
stub: FSharp-Net 'Run.exe'
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
stub: FSharp-Net 'Run.exe'

[F#-Net][ PASS ][VERIFY ACCEPT][ Valid cert ][google.com]

[F#-Net][ PASS ][VERIFY REJECT][ dh480                         ][dh480.badssl.com]
[F#-Net][ PASS ][VERIFY REJECT][ dsdtestprovider               ][dsdtestprovider.badssl.com]
[F#-Net][ PASS ][VERIFY REJECT][ edellroot                     ][edellroot.badssl.com]
[F#-Net][ PASS ][VERIFY REJECT][ expired                       ][expired.badssl.com]
[F#-Net][ PASS ][VERIFY REJECT][ self-signed                   ][self-signed.badssl.com]
[F#-Net][ PASS ][VERIFY REJECT][ superfish                     ][superfish.badssl.com]
[F#-Net][ PASS ][VERIFY REJECT][ untrusted-root                ][untrusted-root.badssl.com]
[F#-Net][ PASS ][VERIFY REJECT][ wrong host                    ][wrong.host.badssl.com]
[F#-Net][ PASS ][VERIFY ACCEPT][ sha-256                       ][sha256.badssl.com]
[F#-Net][ PASS ][VERIFY ACCEPT][ supports SNI                  ][badssl.com]
[F#-Net][ OK?  ][ UNSUPPORTED  ][ disable ca-bundles            ][badssl.com]
[F#-Net][ OK?  ][VERIFY REJECT][ dh1024                        ][dh1024.badssl.com]
[F#-Net][ OK?  ][VERIFY REJECT][ dh-small-subgroup             ][dh-small-subgroup.badssl.com]
[F#-Net][ OK?  ][VERIFY REJECT][ incomplete-chain              ][incomplete-chain.badssl.com]
[F#-Net][ OK?  ][VERIFY REJECT][ mozilla-intermediate          ][mozilla-intermidiate.badssl.com]
[F#-Net][ OK?  ][VERIFY REJECT][ mozilla-modern                ][mozilla-modern.badssl.com]
[F#-Net][ OK?  ][VERIFY REJECT][ subdomain.preloaded-hsts      ][subdomain.preloaded-hsts.badssl.com]
[F#-Net][ OK?  ][VERIFY ACCEPT][ cbc                           ][cbc.badssl.com]
[F#-Net][ OK?  ][VERIFY ACCEPT][ hsts                          ][hsts.badssl.com]
[F#-Net][ OK?  ][VERIFY ACCEPT][ mixed                         ][mixed.badssl.com]
[F#-Net][ OK?  ][VERIFY ACCEPT][ mixed-favicon                 ][mixed-favicon.badssl.com]
[F#-Net][ OK?  ][VERIFY ACCEPT][ mixed-script                  ][mixed-script.badssl.com]
[F#-Net][ OK?  ][VERIFY ACCEPT][ mozilla-old                   ][mozilla-old.badssl.com]
[F#-Net][ OK?  ][VERIFY ACCEPT][ pinning-test                  ][pinning-test.badssl.com]
[F#-Net][ OK?  ][VERIFY ACCEPT][ preloaded-hsts                ][preloaded-hsts.badssl.com]
[F#-Net][ OK?  ][VERIFY ACCEPT][ rc4                           ][rc4.badssl.com]
[F#-Net][ OK?  ][VERIFY ACCEPT][ rsa8192                       ][rsa8192.badssl.com]
[F#-Net][ OK?  ][VERIFY ACCEPT][ sha1-2016                     ][sha1-2016.badssl.com]
[F#-Net][ OK?  ][VERIFY ACCEPT][ sha1-2017                     ][sha1-2017.badssl.com]
[F#-Net][ OK?  ][VERIFY ACCEPT][ upgrade                       ][upgrade.badssl.com]
[F#-Net][ OK?  ][VERIFY ACCEPT][ very                          ][very.badssl.com]
[F#-Net][ FAIL ][VERIFY REJECT][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
[F#-Net][ FAIL ][VERIFY REJECT][ 1000-sans                     ][1000-sans.badssl.com]
[F#-Net][ FAIL ][VERIFY REJECT][ dh2048                        ][dh2048.badssl.com]

[F#-Net][ PASS ][VERIFY REJECT][ OS X vulnerability  ][www.ssllabs.com]
[F#-Net][ PASS ][VERIFY REJECT][ Freak               ][www.ssllabs.com]
[F#-Net][ PASS ][VERIFY REJECT][ Logjam              ][www.ssllabs.com]

```
