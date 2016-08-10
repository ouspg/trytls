# TryTLS testing with Debian latest

## Python

### python-requests

```console

trytls https python trytls/stubs/python-requests/run.py
platform: Linux (debian 8.5)
runner: trytls 0.2.0 (CPython 2.7.9, OpenSSL 1.0.1t)
stub: python 'trytls/stubs/python-requests/run.py'
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 PASS expired certificate [reject expired.badssl.com:443]
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 PASS Superfish CA [reject superfish.badssl.com:443]
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 PASS valid localhost certificate [accept localhost:38277]
 PASS invalid localhost certificate [reject localhost:40414]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]

 ```

### python-urllib2

```console

trytls https python trytls/stubs/python-urllib2/run.py
platform: Linux (debian 8.5)
runner: trytls 0.2.0 (CPython 2.7.9, OpenSSL 1.0.1t)
stub: python 'trytls/stubs/python-urllib2/run.py'
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 PASS expired certificate [reject expired.badssl.com:443]
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 PASS Superfish CA [reject superfish.badssl.com:443]
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 PASS valid localhost certificate [accept localhost:36311]
 PASS invalid localhost certificate [reject localhost:36999]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]

```

## Python3

```console

python3 --version
Python 3.4.2

```

### python-requests

```console

trytls https python3 trytls/stubs/python-requests/run.py
platform: Linux (debian 8.5)
runner: trytls 0.2.0 (CPython 2.7.9, OpenSSL 1.0.1t)
stub: python3 'trytls/stubs/python-requests/run.py'
PASS support for TLS server name indication (SNI) [accept badssl.com:443]
PASS expired certificate [reject expired.badssl.com:443]
PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
PASS self-signed certificate [reject self-signed.badssl.com:443]
PASS SHA-256 signature [accept sha256.badssl.com:443]
PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
PASS Superfish CA [reject superfish.badssl.com:443]
PASS eDellRoot CA [reject edellroot.badssl.com:443]
PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
PASS valid localhost certificate [accept localhost:39471]
PASS invalid localhost certificate [reject localhost:43028]
PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]

```

### python3-urllib

<pre>
debian-latest_1  | Debian GNU/Linux 8.5
debian-latest_1  | Python 3.4.2
debian-latest_1  | [python3-urllib:run.py][ PASS ][ACCEPT][ supports SNI                  ][badssl.com]
debian-latest_1  | [python3-urllib:run.py][ FAIL ][ACCEPT][ expired                       ][expired.badssl.com]
debian-latest_1  | [python3-urllib:run.py][ FAIL ][ACCEPT][ wrong host                    ][wrong.host.badssl.com]
debian-latest_1  | [python3-urllib:run.py][ FAIL ][ACCEPT][ self-signed                   ][self-signed.badssl.com]
debian-latest_1  | [python3-urllib:run.py][ PASS ][ACCEPT][ sha-256                       ][sha256.badssl.com]
debian-latest_1  | [python3-urllib:run.py][ PASS ][ACCEPT][ 1000-sans                     ][1000-sans.badssl.com]
debian-latest_1  | [python3-urllib:run.py][ FAIL ][REJECT][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
debian-latest_1  | [python3-urllib:run.py][ FAIL ][ACCEPT][ incomplete-chain              ][incomplete-chain.badssl.com]
debian-latest_1  | [python3-urllib:run.py][ OK?  ][ACCEPT][ pinning-test                  ][pinning-test.badssl.com]
debian-latest_1  | [python3-urllib:run.py][ FAIL ][ACCEPT][ superfish                     ][superfish.badssl.com]
debian-latest_1  | [python3-urllib:run.py][ FAIL ][ACCEPT][ edellroot                     ][edellroot.badssl.com]
debian-latest_1  | [python3-urllib:run.py][ FAIL ][ACCEPT][ dsdtestprovider               ][dsdtestprovider.badssl.com]
debian-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ disable ca-bundles            ][badssl.com]
debian-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ OS X vulnerability ][www.ssllabs.com]
debian-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ Freak              ][www.ssllabs.com]
debian-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ Logjam             ][www.ssllabs.com]
</pre>

## PHP

```console

php -v
PHP 5.6.24-0+deb8u1 (cli) (built: Jul 26 2016 08:17:07)
Copyright (c) 1997-2016 The PHP Group
Zend Engine v2.6.0, Copyright (c) 1998-2016 Zend Technologies
   with Zend OPcache v7.0.6-dev, Copyright (c) 1999-2016, by Zend Technologies

```console

trytls https php trytls/stubs/php-file-get-contents/run.php
platform: Linux (debian 8.5)
runner: trytls 0.2.0 (CPython 2.7.9, OpenSSL 1.0.1t)
stub: php 'trytls/stubs/php-file-get-contents/run.php'
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 PASS expired certificate [reject expired.badssl.com:443]
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 PASS Superfish CA [reject superfish.badssl.com:443]
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 SKIP valid localhost certificate [accept localhost:40666]
 SKIP invalid localhost certificate [reject localhost:38783]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]

```

## Java

```console

java -version
java version "1.7.0_111"
OpenJDK Runtime Environment (IcedTea 2.6.7) (7u111-2.6.7-1~deb8u1)
OpenJDK 64-Bit Server VM (build 24.111-b01, mixed mode)

```

```console
trytls https java -classpath trytls/stubs/java-https/ Run
platform: Linux (debian 8.5)
runner: trytls 0.2.1 (CPython 2.7.9, OpenSSL 1.0.1t)
stub: java '-classpath' 'trytls/stubs/java-https/' Run
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 PASS expired certificate [reject expired.badssl.com:443]
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 PASS Superfish CA [reject superfish.badssl.com:443]
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
ERROR protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
      reason: stub exited with return code 3
      output: javax.net.ssl.SSLException: Received fatal alert: protocol_version
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 SKIP valid localhost certificate [accept localhost:41259]
 SKIP invalid localhost certificate [reject localhost:45520]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]

 ```

## Go

```console

go version
go version go1.3.3 linux/amd64

```


```console

trytls https go run trytls/stubs/go-nethttp/run.go
platform: Linux (debian 8.5)
runner: trytls 0.2.1 (CPython 2.7.9, OpenSSL 1.0.1t)
stub: go run 'trytls/stubs/go-nethttp/run.go'
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 PASS expired certificate [reject expired.badssl.com:443]
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 PASS Superfish CA [reject superfish.badssl.com:443]
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 SKIP valid localhost certificate [accept localhost:39772]
 SKIP invalid localhost certificate [reject localhost:43771]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]

```
