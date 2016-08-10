# TryTLS testing with Alpine Edge

````console
# cat /etc/alpine-release
3.1.4
```

## Python 2

```console
# python --version
Python 2.7.12
```

### python-requests

```console
# trytls https python python-requests/run.py 
platform: Linux
runner: trytls 0.2.0 (CPython 2.7.12, OpenSSL 1.0.1t)
stub: python 'python-requests/run.py'
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
 PASS valid localhost certificate [accept localhost:34592]
      output: /usr/lib/python2.7/site-packages/requests/packages/urllib3/connection.py:303: SubjectAltNameWarning: Certificate for localhost has no `subjectAltName`, falling back to check for a `commonName` for now. This feature is being removed by major browsers and deprecated by RFC 2818. (See https://github.com/shazow/urllib3/issues/497 for details.)  SubjectAltNameWarning
 PASS invalid localhost certificate [reject localhost:35232]
      output: /usr/lib/python2.7/site-packages/requests/packages/urllib3/connection.py:303: SubjectAltNameWarning: Certificate for localhost has no `subjectAltName`, falling back to check for a `commonName` for now. This feature is being removed by major browsers and deprecated by RFC 2818. (See https://github.com/shazow/urllib3/issues/497 for details.)  SubjectAltNameWarning
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

### python-urllib2

```console
# trytls https python python-urllib2/run.py 
platform: Linux
runner: trytls 0.2.0 (CPython 2.7.12, OpenSSL 1.0.1t)
stub: python 'python-urllib2/run.py'
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
 PASS valid localhost certificate [accept localhost:46338]
 PASS invalid localhost certificate [reject localhost:35071]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

# Go

```console
# go version
go version go1.3.3 linux/amd64
```

```console
# trytls https go-nethttp/run
platform: Linux
runner: trytls 0.2.0 (CPython 2.7.12, OpenSSL 1.0.1t)
stub: 'go-nethttp/run'
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
 SKIP valid localhost certificate [accept localhost:34100]
 SKIP invalid localhost certificate [reject localhost:38563]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

# Java

```console
# java -version
java version "1.7.0_75"
OpenJDK Runtime Environment (IcedTea 2.5.4) (Alpine 7.75.2.5.4-r0)
OpenJDK 64-Bit Server VM (build 24.75-b04, mixed mode)
```

Java stubs give error and ugly exception with OpenJDK 7 in Alpine 3.1 apparently because Java's trust store is not populated correctly.

References:

 * http://stackoverflow.com/q/4764611/361823
 * http://stackoverflow.com/q/6784463/361823

## java-https

```console
# trytls https java -classpath java-https Run
platform: Linux
runner: trytls 0.2.0 (CPython 2.7.12, OpenSSL 1.0.1t)
stub: java '-classpath' 'java-https' Run
ERROR support for TLS server name indication (SNI) [accept badssl.com:443]
      reason: stub exited with return code 3
      output: javax.net.ssl.SSLException: java.lang.RuntimeException: Unexpected error: java.security.InvalidAlgorithmParameterException: t
he trustAnchors parameter must be non-empty
ERROR expired certificate [reject expired.badssl.com:443]
      reason: stub exited with return code 3
      output: javax.net.ssl.SSLException: java.lang.RuntimeException: Unexpected error: java.security.InvalidAlgorithmParameterException: t
he trustAnchors parameter must be non-empty
ERROR wrong hostname in certificate [reject wrong.host.badssl.com:443]
      reason: stub exited with return code 3
      output: javax.net.ssl.SSLException: java.lang.RuntimeException: Unexpected error: java.security.InvalidAlgorithmParameterException: t
he trustAnchors parameter must be non-empty
ERROR self-signed certificate [reject self-signed.badssl.com:443]
      reason: stub exited with return code 3
      output: javax.net.ssl.SSLException: java.lang.RuntimeException: Unexpected error: java.security.InvalidAlgorithmParameterException: t
he trustAnchors parameter must be non-empty
ERROR SHA-256 signature [accept sha256.badssl.com:443]
      reason: stub exited with return code 3
      output: javax.net.ssl.SSLException: java.lang.RuntimeException: Unexpected error: java.security.InvalidAlgorithmParameterException: t
he trustAnchors parameter must be non-empty
ERROR 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
      reason: stub exited with return code 3
      output: javax.net.ssl.SSLException: java.lang.RuntimeException: Unexpected error: java.security.InvalidAlgorithmParameterException: t
he trustAnchors parameter must be non-empty
ERROR incomplete chain of trust [reject incomplete-chain.badssl.com:443]
      reason: stub exited with return code 3
      output: javax.net.ssl.SSLException: java.lang.RuntimeException: Unexpected error: java.security.InvalidAlgorithmParameterException: t
he trustAnchors parameter must be non-empty
ERROR Superfish CA [reject superfish.badssl.com:443]
      reason: stub exited with return code 3
      output: javax.net.ssl.SSLException: java.lang.RuntimeException: Unexpected error: java.security.InvalidAlgorithmParameterException: t
he trustAnchors parameter must be non-empty
ERROR eDellRoot CA [reject edellroot.badssl.com:443]
      reason: stub exited with return code 3
      output: javax.net.ssl.SSLException: java.lang.RuntimeException: Unexpected error: java.security.InvalidAlgorithmParameterException: t
he trustAnchors parameter must be non-empty
ERROR DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
      reason: stub exited with return code 3
      output: javax.net.ssl.SSLException: java.lang.RuntimeException: Unexpected error: java.security.InvalidAlgorithmParameterException: t
he trustAnchors parameter must be non-empty
ERROR protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
      reason: stub exited with return code 3
      output: javax.net.ssl.SSLException: Received fatal alert: protocol_version
ERROR protect against the FREAK attack [reject www.ssllabs.com:10444]
      reason: stub exited with return code 3
      output: javax.net.ssl.SSLException: java.lang.RuntimeException: Unexpected error: java.security.InvalidAlgorithmParameterException: t
he trustAnchors parameter must be non-empty
ERROR protect against the Logjam attack [reject www.ssllabs.com:10445]
      reason: stub exited with return code 3
      output: javax.net.ssl.SSLException: java.lang.RuntimeException: Unexpected error: java.security.InvalidAlgorithmParameterException: t
he trustAnchors parameter must be non-empty
ERROR protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
      reason: stub exited with return code 3
      output: javax.net.ssl.SSLException: java.lang.RuntimeException: Unexpected error: java.security.InvalidAlgorithmParameterException: t
he trustAnchors parameter must be non-empty
ERROR protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
      reason: stub exited with return code 3
      output: javax.net.ssl.SSLException: java.lang.RuntimeException: Unexpected error: java.security.InvalidAlgorithmParameterException: t
he trustAnchors parameter must be non-empty
 SKIP valid localhost certificate [accept localhost:35064]
 SKIP invalid localhost certificate [reject localhost:37171]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

# PHP 5

```console
# php --version
PHP 5.6.24 (cli) (built: Jul 27 2016 07:30:07) 
Copyright (c) 1997-2016 The PHP Group
Zend Engine v2.6.0, Copyright (c) 1998-2016 Zend Technologies
```

```console
# trytls https php php-file-get-contents/run.php 
platform: Linux
runner: trytls 0.2.0 (CPython 2.7.12, OpenSSL 1.0.1t)
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
 SKIP valid localhost certificate [accept localhost:42775]
 SKIP invalid localhost certificate [reject localhost:37863]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```
