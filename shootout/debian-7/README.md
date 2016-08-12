# TryTLS testing with Debian 7

```console

# cat /etc/debian_version
7.11

```

## Python 2

The stub will be executed with python2.7, as that launches the version provided
by the distribution. python3.5 was manually installed for executing the
TryTLS runner itself (not the stub).

```console
# python --version
Python 2.7.3
```

### python-requests

```console

# trytls https python2.7 trytls-0.2.1/stubs/python-requests/run.py
platform: Linux
runner: trytls 0.2.1 (CPython 3.5.2, OpenSSL 1.0.1e)
stub: python2.7 trytls-0.2.1/stubs/python-requests/run.py
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
 PASS valid localhost certificate [accept localhost:43220]
 PASS invalid localhost certificate [reject localhost:42208]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]

```

### python-urllib2

```console

# trytls https python2.7 trytls-0.2.1/stubs/python-urllib2/run.py
platform: Linux
runner: trytls 0.2.1 (CPython 3.5.2, OpenSSL 1.0.1e)
stub: python2.7 trytls-0.2.1/stubs/python-urllib2/run.py
ERROR support for TLS server name indication (SNI) [accept badssl.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "trytls-0.2.1/stubs/python-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR expired certificate [reject expired.badssl.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "trytls-0.2.1/stubs/python-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR wrong hostname in certificate [reject wrong.host.badssl.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "trytls-0.2.1/stubs/python-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR self-signed certificate [reject self-signed.badssl.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "trytls-0.2.1/stubs/python-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR SHA-256 signature [accept sha256.badssl.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "trytls-0.2.1/stubs/python-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "trytls-0.2.1/stubs/python-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR incomplete chain of trust [reject incomplete-chain.badssl.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "trytls-0.2.1/stubs/python-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR Superfish CA [reject superfish.badssl.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "trytls-0.2.1/stubs/python-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR eDellRoot CA [reject edellroot.badssl.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "trytls-0.2.1/stubs/python-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "trytls-0.2.1/stubs/python-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "trytls-0.2.1/stubs/python-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR protect against the FREAK attack [reject www.ssllabs.com:10444]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "trytls-0.2.1/stubs/python-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR protect against the Logjam attack [reject www.ssllabs.com:10445]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "trytls-0.2.1/stubs/python-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "trytls-0.2.1/stubs/python-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "trytls-0.2.1/stubs/python-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR valid localhost certificate [accept localhost:42209]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "trytls-0.2.1/stubs/python-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR invalid localhost certificate [reject localhost:33918]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "trytls-0.2.1/stubs/python-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR use only the given CA bundle, not system's [reject sha256.badssl.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "trytls-0.2.1/stubs/python-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'

```

## Python 3

The stub will be executed with python3.2, as that launches the version provided
by the distribution. python3.5 was manually installed for executing the
TryTLS runner itself (not the stub).

```console

# python3.2 --version
Python 3.2.3

```

<!-- markdownlint-disable MD024 -->

### python-requests

<!-- markdownlint-enable MD024 -->

```console

# trytls https python3.2 trytls-0.2.1/stubs/python-requests/run.py
platform: Linux
runner: trytls 0.2.1 (CPython 3.5.2, OpenSSL 1.0.1e)
stub: python3.2 trytls-0.2.1/stubs/python-requests/run.py
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
 PASS valid localhost certificate [accept localhost:37934]
 PASS invalid localhost certificate [reject localhost:38880]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]

```

### python-urllib

```console

# trytls https python3.2 trytls-0.2.1/stubs/python3-urllib/run.py
platform: Linux
runner: trytls 0.2.1 (CPython 3.5.2, OpenSSL 1.0.1e)
stub: python3.2 trytls-0.2.1/stubs/python3-urllib/run.py
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
 PASS valid localhost certificate [accept localhost:33483]
 PASS invalid localhost certificate [reject localhost:38129]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]

```

## Java

```console
java -version
java version "1.7.0_111"
OpenJDK Runtime Environment (IcedTea 2.6.7) (7u111-2.6.7-1~deb7u1)
OpenJDK 64-Bit Server VM (build 24.111-b01, mixed mode)

```

### java-https

```console

# trytls https java -classpath trytls-0.2.1/stubs/java-https/ Run
platform: Linux
runner: trytls 0.2.1 (CPython 3.5.2, OpenSSL 1.0.1e)
stub: java -classpath trytls-0.2.1/stubs/java-https/ Run
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
 SKIP valid localhost certificate [accept localhost:42281]
 SKIP invalid localhost certificate [reject localhost:33223]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]

```

### java-net

```console

# trytls https java -classpath trytls-0.2.1/stubs/java-net/ Run
platform: Linux
runner: trytls 0.2.1 (CPython 3.5.2, OpenSSL 1.0.1e)
stub: java -classpath trytls-0.2.1/stubs/java-net/ Run
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
 SKIP valid localhost certificate [accept localhost:46042]
 SKIP invalid localhost certificate [reject localhost:37856]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]

```

## Go

```console

# go version
go version go1.0.2

```

### go-nethttp

```console

# trytls https go run trytls-0.2.1/stubs/go-nethttp/run.go
platform: Linux
runner: trytls 0.2.1 (CPython 3.5.2, OpenSSL 1.0.1e)
stub: go run trytls-0.2.1/stubs/go-nethttp/run.go
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
ERROR protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
      reason: stub exited with return code 1
      output: Get https://www.ssllabs.com:10443: remote error: protocol version not supported
              exit status 1
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 SKIP valid localhost certificate [accept localhost:35707]
 SKIP invalid localhost certificate [reject localhost:44504]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]

```

## PHP

```console
php -v
PHP 5.4.45-0+deb7u4 (cli) (built: Jun 29 2016 14:51:18)
Copyright (c) 1997-2014 The PHP Group
Zend Engine v2.4.0, Copyright (c) 1998-2014 Zend Technologies

```

### php-file-get-contents

```console
# trytls https php trytls-0.2.1/stubs/php-file-get-contents/run.php
platform: Linux
runner: trytls 0.2.1 (CPython 3.5.2, OpenSSL 1.0.1e)
stub: php trytls-0.2.1/stubs/php-file-get-contents/run.php
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
 SKIP valid localhost certificate [accept localhost:44513]
 SKIP invalid localhost certificate [reject localhost:35630]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]

```
