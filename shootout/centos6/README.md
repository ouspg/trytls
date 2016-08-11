# TryTLS testing with CentOS

We chose centos5, centos6 and centos7 for this TryTLS-shootout
based on the [CentOS End of Support Schedule](https://en.wikipedia.org/wiki/CentOS#End-of-support_schedule).

```console
$ docker run -ti --rm centos6

# cat /etc/redhat-release
CentOS release 6.8 (Final)
```

<!-- markdownlint-disable MD013 -->

OS         | python-requests | python-urllib2 | python3-urllib | go-nethttp | java-https | java-net | php-file-get-contents
---------- | --------------- | -------------- | -------------- | ---------- | ---------- | -------- | ---------------------
CentOS 6.8 | NO SNI          | ERROR          | PASS           | PASS       | ERROR(1)   | ERROR(1) | NO SNI

## python-requests

```console
# scl enable rh-python34 bash # python 2 is too old to run TryTLS runner

# /usr/bin/python --version
Python 2.6.6

# trytls https /usr/bin/python python-requests/run.py
platform: Linux
runner: trytls 0.2.1 (CPython 3.4.2, OpenSSL 1.0.1e-fips)
stub: /usr/bin/python python-requests/run.py
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
 PASS valid localhost certificate [accept localhost:58923]
      output: /usr/lib/python2.6/site-packages/urllib3/connection.py:251: SecurityWarning: Certificate has no `subjectAltName`, falling back to check for a `commonName` for now. This feature is being removed by major browsers and deprecated by RFC 2818. (See https://github.com/shazow/urllib3/issues/497 for details.)  SecurityWarning
 PASS invalid localhost certificate [reject localhost:38470]
      output: /usr/lib/python2.6/site-packages/urllib3/connection.py:251: SecurityWarning: Certificate has no `subjectAltName`, falling back to check for a `commonName` for now. This feature is being removed by major browsers and deprecated by RFC 2818. (See https://github.com/shazow/urllib3/issues/497 for details.)  SecurityWarning
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## python-urllib2

```console
# scl enable rh-python34 bash # python 2 is too old to run TryTLS runner

# /usr/bin/python --version
Python 2.6.6

# trytls https /usr/bin/python python-urllib2/run.py
platform: Linux
runner: trytls 0.2.1 (CPython 3.4.2, OpenSSL 1.0.1e-fips)
stub: /usr/bin/python python-urllib2/run.py
ERROR support for TLS server name indication (SNI) [accept badssl.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
...
```

## python3-urllib

```console
# scl enable rh-python34 "python --version"
Python 3.4.2

# scl enable rh-python34 bash
# trytls https python python3-urllib/run.py
platform: Linux
runner: trytls 0.2.1 (CPython 3.4.2, OpenSSL 1.0.1e-fips)
stub: python python3-urllib/run.py
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
 PASS valid localhost certificate [accept localhost:39877]
 PASS invalid localhost certificate [reject localhost:59439]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## go-nethttp

```console
# scl enable rh-python34 bash # python 2 is too old to run TryTLS runner

# go version
go version go1.5.1 linux/amd64

# trytls https go-nethttp/run
platform: Linux
runner: trytls 0.2.1 (CPython 3.4.2, OpenSSL 1.0.1e-fips)
stub: go-nethttp/run
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
 SKIP valid localhost certificate [accept localhost:54174]
 SKIP invalid localhost certificate [reject localhost:46553]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## java-https

```console
# scl enable rh-python34 bash # python 2 is too old to run TryTLS runner

# java -version
java version "1.7.0_111"
OpenJDK Runtime Environment (rhel-2.6.7.2.el6_8-x86_64 u111-b01)
OpenJDK 64-Bit Server VM (build 24.111-b01, mixed mode)

# trytls https java -classpath java-https Run
platform: Linux
runner: trytls 0.2.1 (CPython 3.4.2, OpenSSL 1.0.1e-fips)
stub: java -classpath java-https Run
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
 SKIP valid localhost certificate [accept localhost:40711]
 SKIP invalid localhost certificate [reject localhost:53950]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## java-net

```console
# scl enable rh-python34 bash # python 2 is too old to run TryTLS runner

# java -version
java version "1.7.0_111"
OpenJDK Runtime Environment (rhel-2.6.7.2.el7_2-x86_64 u111-b01)
OpenJDK 64-Bit Server VM (build 24.111-b01, mixed mode)

# trytls https java -classpath java-net Run
platform: Linux
runner: trytls 0.2.1 (CPython 3.4.2, OpenSSL 1.0.1e-fips)
stub: java -classpath java-net Run
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
 SKIP valid localhost certificate [accept localhost:34017]
 SKIP invalid localhost certificate [reject localhost:53308]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## php-file-get-contents

```console
# scl enable rh-python34 bash # python 2 is too old to run TryTLS runner

# php --version
PHP 5.3.3 (cli) (built: May 10 2016 21:39:50)
Copyright (c) 1997-2010 The PHP Group
Zend Engine v2.3.0, Copyright (c) 1998-2010 Zend Technologies

# trytls https php php-file-get-contents/run.php
platform: Linux
runner: trytls 0.2.1 (CPython 3.4.2, OpenSSL 1.0.1e-fips)
stub: php php-file-get-contents/run.php
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
 SKIP valid localhost certificate [accept localhost:45056]
 SKIP invalid localhost certificate [reject localhost:38911]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

<!-- markdownlint-enable MD013 -->
