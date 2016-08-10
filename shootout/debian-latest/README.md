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

```console

trytls https python3 trytls/stubs/python3-urllib/run.py 
platform: Linux (debian 8.5)
runner: trytls 0.2.1 (CPython 2.7.9, OpenSSL 1.0.1t)
stub: python3 'trytls/stubs/python3-urllib/run.py'
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
 PASS valid localhost certificate [accept localhost:43592]
 PASS invalid localhost certificate [reject localhost:36013]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]

```


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

### java-https

```console

trytls https java -classpath trytls/stubs/java-https/ Run
platform: Linux (debian 8.5)
runner: trytls 0.2.0 (CPython 2.7.9, OpenSSL 1.0.1t)
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
 SKIP valid localhost certificate [accept localhost:46829]
 SKIP invalid localhost certificate [reject localhost:34685]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
 
 ```
### java-net

```console
t trytls https java -classpath trytls/stubs/java-net/ Run
platform: Linux (debian 8.5)
runner: trytls 0.2.0 (CPython 2.7.9, OpenSSL 1.0.1t)
stub: java '-classpath' 'trytls/stubs/java-net/' Run
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
              	at sun.security.ssl.SSLSocketImpl.recvAlert(SSLSocketImpl.java:1989)
              	at sun.security.ssl.SSLSocketImpl.readRecord(SSLSocketImpl.java:1096)
              	at sun.security.ssl.SSLSocketImpl.performInitialHandshake(SSLSocketImpl.java:1342)
              	at sun.security.ssl.SSLSocketImpl.startHandshake(SSLSocketImpl.java:1369)
              	at sun.security.ssl.SSLSocketImpl.startHandshake(SSLSocketImpl.java:1353)
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
 SKIP valid localhost certificate [accept localhost:46857]
 SKIP invalid localhost certificate [reject localhost:33487]
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
