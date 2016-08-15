# TryTLS testing with OpenBSD -current

```console
$ uname -a
OpenBSD tlstestii.panoulu.local 6.0 GENERIC.MP#2337 amd64

$ date
Wed Aug 10 05:05:35 UTC 2016
```

## PHP 5.5

```console
# php-5.5 --version
PHP 5.5.37 (cli) (built: Aug  6 2016 02:35:07)
Copyright (c) 1997-2015 The PHP Group
Zend Engine v2.5.0, Copyright (c) 1998-2015 Zend Technologies
    with Suhosin v0.9.38, Copyright (c) 2007-2015, by SektionEins GmbH
```

```console
# diff php-5.5.ini.2016-08-09 php-5.5.ini
801c801
< allow_url_fopen = Off
---
> allow_url_fopen = On
```

```console
$ trytls https php-5.5 run.php
platform: OpenBSD
runner: trytls 0.2.1 (CPython 2.7.12, LibreSSL 2.5.0)
stub: 'php-5.5' 'run.php'
 FAIL support for TLS server name indication (SNI) [accept badssl.com:443]
 PASS expired certificate [reject expired.badssl.com:443]
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
 FAIL SHA-256 signature [accept sha256.badssl.com:443]
 FAIL 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 PASS Superfish CA [reject superfish.badssl.com:443]
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 SKIP valid localhost certificate [accept localhost:23300]
 SKIP invalid localhost certificate [reject localhost:15485]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## PHP 5.6

```console
$ php-5.6 --version
PHP 5.6.23 (cli) (built: Aug  5 2016 14:56:12)
Copyright (c) 1997-2016 The PHP Group
Zend Engine v2.6.0, Copyright (c) 1998-2016 Zend Technologies
    with Suhosin v0.9.38, Copyright (c) 2007-2015, by SektionEins GmbH
```

```console
# diff php-5.6.ini.2016-08-09 php-5.6.ini
818c818
< allow_url_fopen = Off
---
> allow_url_fopen = On
```

```console
$ trytls https php-5.6 run.php
platform: OpenBSD
runner: trytls 0.2.1 (CPython 2.7.12, LibreSSL 2.5.0)
stub: 'php-5.6' 'run.php'
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
 SKIP valid localhost certificate [accept localhost:32471]
 SKIP invalid localhost certificate [reject localhost:23024]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## PHP 7.0

```console
$ php-7.0 --version
PHP 7.0.8 (cli) (built: Aug  6 2016 02:10:12) ( NTS )
Copyright (c) 1997-2016 The PHP Group
Zend Engine v3.0.0, Copyright (c) 1998-2016 Zend Technologies
```

```console
# diff php-7.0.ini.2016-08-09 php-7.0.ini
807c807
< allow_url_fopen = Off
---
> allow_url_fopen = On
```

```console
$ trytls https php-7.0 run.php
platform: OpenBSD
runner: trytls 0.2.1 (CPython 2.7.12, LibreSSL 2.5.0)
stub: 'php-7.0' 'run.php'
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
 SKIP valid localhost certificate [accept localhost:34892]
 SKIP invalid localhost certificate [reject localhost:37112]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## Go

```console
$ go version
go version go1.6.3 openbsd/amd64
```

```console
$ trytls https ./run
platform: OpenBSD
runner: trytls 0.2.1 (CPython 2.7.12, LibreSSL 2.5.0)
stub: './run'
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
 SKIP valid localhost certificate [accept localhost:8009]
 SKIP invalid localhost certificate [reject localhost:30059]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## Python 2

```console
$ python2.7 --version
Python 2.7.12
```

### python-urllib2

```console
$ trytls https python2.7 stubs/python-urllib2/run.py
platform: OpenBSD
runner: trytls 0.2.1 (CPython 2.7.12, LibreSSL 2.5.0)
stub: 'python2.7' 'stubs/python-urllib2/run.py'
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
 PASS valid localhost certificate [accept localhost:19525]
 PASS invalid localhost certificate [reject localhost:42864]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## Python 3.4

```console
$ python3.4 --version
Python 3.4.5
```

### python3-urllib

```console
$ trytls https python3.4 stubs/python3-urllib/run.py
platform: OpenBSD
runner: trytls 0.2.1 (CPython 2.7.12, LibreSSL 2.5.0)
stub: 'python3.4' 'stubs/python3-urllib/run.py'
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
 PASS valid localhost certificate [accept localhost:32160]
 PASS invalid localhost certificate [reject localhost:28691]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## Python 3.5

```console
$ python3.5 --version
Python 3.5.2
```

```console
$ trytls https python3.5 stubs/python3-urllib/run.py
platform: OpenBSD
runner: trytls 0.2.1 (CPython 2.7.12, LibreSSL 2.5.0)
stub: 'python3.5' 'stubs/python3-urllib/run.py'
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
 PASS valid localhost certificate [accept localhost:15142]
 PASS invalid localhost certificate [reject localhost:14643]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```
