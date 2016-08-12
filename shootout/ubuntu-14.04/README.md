# TryTLS testing with CentOS

We chose Ubuntu 12.04, 14.04 and 16.04 LTS releases for this TryTLS-shootout
based on the [CentOS End of Support Schedule](http://www.ubuntu.com/info/release-end-of-life).

```console
$ docker run -ti --rm ubuntu-14.04

# grep DISTRIB_DESCRIPTION /etc/lsb-release
DISTRIB_DESCRIPTION="Ubuntu 14.04.5 LTS"
```

<!-- markdownlint-disable MD013 -->

OS                 | python-requests | python-urllib2 | python3-urllib | go-nethttp | java-https | java-net | php-file-get-contents
------------------ | --------------- | -------------- | -------------- | ---------- | ---------- | -------- | ---------------------
Ubuntu 14.04.5 LTS | NO SNI          | ERROR          | FAIL           | NO SNI     | ERROR      | ERROR    | NO SNI

## python-requests

```console
# python --version
Python 2.7.6

# trytls https python python-requests/run.py
platform: Linux (Ubuntu 14.04)
runner: trytls 0.2.1 (CPython 2.7.6, OpenSSL 1.0.1f)
stub: python 'python-requests/run.py'
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
 PASS valid localhost certificate [accept localhost:53572]
 PASS invalid localhost certificate [reject localhost:47310]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## python-urllib2

```console
# python --version
Python 2.7.6

# trytls https python python-urllib2/run.py
platform: Linux (Ubuntu 14.04)
runner: trytls 0.2.1 (CPython 2.7.6, OpenSSL 1.0.1f)
stub: python 'python-urllib2/run.py'
ERROR support for TLS server name indication (SNI) [accept badssl.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
...
```

## python3-urllib

```console
# python3 --version
Python 3.4.3

# trytls https python3 python3-urllib/run.py
platform: Linux (Ubuntu 14.04)
runner: trytls 0.2.1 (CPython 2.7.6, OpenSSL 1.0.1f)
stub: python3 'python3-urllib/run.py'
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 FAIL expired certificate [reject expired.badssl.com:443]
 FAIL wrong hostname in certificate [reject wrong.host.badssl.com:443]
 FAIL self-signed certificate [reject self-signed.badssl.com:443]
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 FAIL incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 FAIL Superfish CA [reject superfish.badssl.com:443]
 FAIL eDellRoot CA [reject edellroot.badssl.com:443]
 FAIL DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 PASS valid localhost certificate [accept localhost:50577]
 PASS invalid localhost certificate [reject localhost:54284]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## go-nethttp

```console
# go version
go version go1.2.1 linux/amd64

# trytls https go-nethttp/run
platform: Linux (Ubuntu 14.04)
runner: trytls 0.2.1 (CPython 2.7.6, OpenSSL 1.0.1f)
stub: 'go-nethttp/run'
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
 SKIP valid localhost certificate [accept localhost:34611]
 SKIP invalid localhost certificate [reject localhost:50600]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## java-https

```console
# java -version
java version "1.7.0_101"
OpenJDK Runtime Environment (IcedTea 2.6.6) (7u101-2.6.6-0ubuntu0.14.04.1)
OpenJDK 64-Bit Server VM (build 24.95-b01, mixed mode)

# trytls https java -classpath java-https Run
platform: Linux (Ubuntu 14.04)
runner: trytls 0.2.1 (CPython 2.7.6, OpenSSL 1.0.1f)
stub: java '-classpath' 'java-https' Run
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
 SKIP valid localhost certificate [accept localhost:43872]
 SKIP invalid localhost certificate [reject localhost:60488]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## java-net

```console
# java -version
java version "1.7.0_101"
OpenJDK Runtime Environment (IcedTea 2.6.6) (7u101-2.6.6-0ubuntu0.14.04.1)
OpenJDK 64-Bit Server VM (build 24.95-b01, mixed mode)

# trytls https java -classpath java-net Run
platform: Linux (Ubuntu 14.04)
runner: trytls 0.2.1 (CPython 2.7.6, OpenSSL 1.0.1f)
stub: java '-classpath' 'java-net' Run
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
      reason: stub exited with return code 1
      output: javax.net.ssl.SSLException: Received fatal alert: protocol_version
                at sun.security.ssl.Alerts.getSSLException(Alerts.java:208)
                at sun.security.ssl.Alerts.getSSLException(Alerts.java:154)
                at sun.security.ssl.SSLSocketImpl.recvAlert(SSLSocketImpl.java:1991)
                at sun.security.ssl.SSLSocketImpl.readRecord(SSLSocketImpl.java:1098)
                at sun.security.ssl.SSLSocketImpl.performInitialHandshake(SSLSocketImpl.java:1344)
                at sun.security.ssl.SSLSocketImpl.startHandshake(SSLSocketImpl.java:1371)
                at sun.security.ssl.SSLSocketImpl.startHandshake(SSLSocketImpl.java:1355)
                at sun.net.www.protocol.https.HttpsClient.afterConnect(HttpsClient.java:559)
                at sun.net.www.protocol.https.AbstractDelegateHttpsURLConnection.connect(AbstractDelegateHttpsURLConnection.java:185)
                at sun.net.www.protocol.http.HttpURLConnection.getInputStream(HttpURLConnection.java:1302)
                at java.net.URLConnection.getContent(URLConnection.java:748)
                at sun.net.www.protocol.https.HttpsURLConnectionImpl.getContent(HttpsURLConnectionImpl.java:434)
                at java.net.URL.getContent(URL.java:1062)
                at Run.main(Run.java:21)
              Exception in thread "main" java.lang.NullPointerException
                at Run.main(Run.java:27)
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 SKIP valid localhost certificate [accept localhost:42122]
 SKIP invalid localhost certificate [reject localhost:46722]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## php-file-get-contents

```console
# php --version
PHP 5.5.9-1ubuntu4.19 (cli) (built: Jul 28 2016 19:31:33)
Copyright (c) 1997-2014 The PHP Group
Zend Engine v2.5.0, Copyright (c) 1998-2014 Zend Technologies
    with Zend OPcache v7.0.3, Copyright (c) 1999-2014, by Zend Technologies

# trytls https php php-file-get-contents/run.php
platform: Linux (Ubuntu 14.04)
runner: trytls 0.2.1 (CPython 2.7.6, OpenSSL 1.0.1f)
stub: php 'php-file-get-contents/run.php'
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
 SKIP valid localhost certificate [accept localhost:54380]
 SKIP invalid localhost certificate [reject localhost:45361]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

<!-- markdownlint-enable MD013 -->
