# TryTLS testing with Debian 8

```console
docker run -ti --rm debian8
```

```console
# cat /etc/debian_version
8.5
```

<!-- markdownlint-disable MD013 -->

OS         | python2-requests | python2-urllib2 | python3-urllib | go-nethttp | java-https | java-net | php-file-get-contents
---------- | ---------------- | --------------- | -------------- | ---------- | ---------- | -------- | ---------------------
Debian 8   | ?                | ?               | ?              | ?          | ?          | ?        | ?

## python2-requests

```console
# python --version
Python 2.7.9
```

```console
# trytls https python python2-requests/run.py
platform: Linux (debian 8.5)
runner: trytls 0.3.3 (CPython 2.7.9, OpenSSL 1.0.1t)
stub: python python2-requests/run.py
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 PASS protection against POODLE attack [reject sslv3.dshield.org:443]
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
 PASS expired certificate [reject expired.badssl.com:443]
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 PASS Superfish CA [reject superfish.badssl.com:443]
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
 PASS support for TLS server name indication (SNI) [accept tlsfun.de:443]
 PASS eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
 PASS valid certificate Common Name [accept domain-match.badtls.io:10000]
 PASS valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
 PASS support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
 PASS TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
 PASS certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
 PASS certificate validity starts in future [reject future.badtls.io:11001]
 PASS mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
 PASS Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
 PASS certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
 PASS expired certificate [reject expired.badtls.io:11006]
 PASS invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
 PASS denies use of RC4 ciphers (RFC7465) [reject rc4.badtls.io:11008]
 FAIL denies use of MD5 signature algorithm (RFC6151) [reject weak-sig.badtls.io:11004]
 PASS denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
 PASS valid localhost certificate [accept localhost:33958]
 PASS invalid localhost certificate [reject localhost:39729]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## python2-urllib2

```console
# python --version
Python 2.7.9
```

```console
# trytls https python python2-urllib2/run.py
platform: Linux (debian 8.5)
runner: trytls 0.3.3 (CPython 2.7.9, OpenSSL 1.0.1t)
stub: python python2-urllib2/run.py
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 PASS protection against POODLE attack [reject sslv3.dshield.org:443]
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
 PASS expired certificate [reject expired.badssl.com:443]
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 PASS Superfish CA [reject superfish.badssl.com:443]
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
 PASS support for TLS server name indication (SNI) [accept tlsfun.de:443]
 PASS eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
 PASS valid certificate Common Name [accept domain-match.badtls.io:10000]
 PASS valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
 PASS support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
 PASS TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
 PASS certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
 PASS certificate validity starts in future [reject future.badtls.io:11001]
 PASS mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
 PASS Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
 PASS certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
 PASS expired certificate [reject expired.badtls.io:11006]
 PASS invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
 FAIL denies use of RC4 ciphers (RFC7465) [reject rc4.badtls.io:11008]
 FAIL denies use of MD5 signature algorithm (RFC6151) [reject weak-sig.badtls.io:11004]
 PASS denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
 PASS valid localhost certificate [accept localhost:46523]
 PASS invalid localhost certificate [reject localhost:38737]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## python3-urllib

```console
# python3 --version
Python 3.4.2
```

```console
# trytls https python3 python3-urllib/run.py
platform: Linux (debian 8.5)
runner: trytls 0.3.3 (CPython 2.7.9, OpenSSL 1.0.1t)
stub: python3 python3-urllib/run.py
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 PASS protection against POODLE attack [reject sslv3.dshield.org:443]
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 FAIL self-signed certificate [reject self-signed.badssl.com:443]
 SKIP expired certificate [reject expired.badssl.com:443]
      reason: stub didn't reject a self-signed certificate
 SKIP wrong hostname in certificate [reject wrong.host.badssl.com:443]
      reason: stub didn't reject a self-signed certificate
 SKIP SHA-256 signature [accept sha256.badssl.com:443]
      reason: stub didn't reject a self-signed certificate
 SKIP 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
      reason: stub didn't reject a self-signed certificate
 SKIP incomplete chain of trust [reject incomplete-chain.badssl.com:443]
      reason: stub didn't reject a self-signed certificate
 SKIP Superfish CA [reject superfish.badssl.com:443]
      reason: stub didn't reject a self-signed certificate
 SKIP eDellRoot CA [reject edellroot.badssl.com:443]
      reason: stub didn't reject a self-signed certificate
 SKIP DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
      reason: stub didn't reject a self-signed certificate
 PASS support for TLS server name indication (SNI) [accept tlsfun.de:443]
 FAIL eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
 PASS valid certificate Common Name [accept domain-match.badtls.io:10000]
 PASS valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
 PASS support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
 PASS TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
 PASS certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
 PASS certificate validity starts in future [reject future.badtls.io:11001]
 PASS mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
 PASS Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
 PASS certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
 PASS expired certificate [reject expired.badtls.io:11006]
 PASS invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
 FAIL denies use of RC4 ciphers (RFC7465) [reject rc4.badtls.io:11008]
 FAIL denies use of MD5 signature algorithm (RFC6151) [reject weak-sig.badtls.io:11004]
 PASS denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
 PASS valid localhost certificate [accept localhost:34901]
 PASS invalid localhost certificate [reject localhost:39505]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## go-nethttp

```console
# go version
go version go1.3.3 linux/amd64
```

```console
# trytls https go-nethttp/run
platform: Linux (debian 8.5)
runner: trytls 0.3.3 (CPython 2.7.9, OpenSSL 1.0.1t)
stub: go-nethttp/run
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
      output: Get https://www.ssllabs.com:10443: crypto/rsa: verification error
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
      output: Get https://www.ssllabs.com:10444: tls: unexpected ServerKeyExchange
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
      output: Get https://www.ssllabs.com:10445: remote error: handshake failure
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
      output: Get https://cve.freakattack.com:443: tls: unexpected ServerKeyExchange
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
      output: Get https://cve2.freakattack.com:443: tls: unexpected ServerKeyExchange
 PASS protection against POODLE attack [reject sslv3.dshield.org:443]
      output: Get https://sslv3.dshield.org:443: tls: server selected unsupported protocol version 300
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
      output: Get https://self-signed.badssl.com:443: x509: certificate signed by unknown authority
 PASS expired certificate [reject expired.badssl.com:443]
      output: Get https://expired.badssl.com:443: x509: certificate has expired or is not yet valid
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
      output: Get https://wrong.host.badssl.com:443: x509: certificate is valid for *.badssl.com, badssl.com, not wrong.host.badssl.com
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
      output: Get https://incomplete-chain.badssl.com:443: x509: certificate signed by unknown authority
 PASS Superfish CA [reject superfish.badssl.com:443]
      output: Get https://superfish.badssl.com:443: x509: certificate signed by unknown authority
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
      output: Get https://edellroot.badssl.com:443: x509: certificate signed by unknown authority
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
      output: Get https://dsdtestprovider.badssl.com:443: x509: certificate signed by unknown authority
 PASS support for TLS server name indication (SNI) [accept tlsfun.de:443]
 PASS eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
      output: Get https://badcert-edell.tlsfun.de:443: x509: certificate signed by unknown authority
 SKIP valid certificate Common Name [accept domain-match.badtls.io:10000]
 SKIP valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
 SKIP support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
 SKIP TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
 SKIP certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
 SKIP certificate validity starts in future [reject future.badtls.io:11001]
 SKIP mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
 SKIP Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
 SKIP certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
 SKIP expired certificate [reject expired.badtls.io:11006]
 SKIP invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
 SKIP denies use of RC4 ciphers (RFC7465) [reject rc4.badtls.io:11008]
 SKIP denies use of MD5 signature algorithm (RFC6151) [reject weak-sig.badtls.io:11004]
 SKIP denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
 SKIP valid localhost certificate [accept localhost:39872]
 SKIP invalid localhost certificate [reject localhost:45488]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## java-https

```console
# java -version
java version "1.7.0_111"
OpenJDK Runtime Environment (IcedTea 2.6.7) (7u111-2.6.7-1~deb8u1)
OpenJDK 64-Bit Server VM (build 24.111-b01, mixed mode)
```

```console
# trytls https java -classpath java-https Run
platform: Linux (debian 8.5)
runner: trytls 0.3.3 (CPython 2.7.9, OpenSSL 1.0.1t)
stub: java -classpath java-https Run
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 PASS protection against POODLE attack [reject sslv3.dshield.org:443]
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
 PASS expired certificate [reject expired.badssl.com:443]
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 PASS Superfish CA [reject superfish.badssl.com:443]
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
 PASS support for TLS server name indication (SNI) [accept tlsfun.de:443]
 PASS eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
 SKIP valid certificate Common Name [accept domain-match.badtls.io:10000]
 SKIP valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
 SKIP support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
 SKIP TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
 SKIP certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
 SKIP certificate validity starts in future [reject future.badtls.io:11001]
 SKIP mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
 SKIP Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
 SKIP certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
 SKIP expired certificate [reject expired.badtls.io:11006]
 SKIP invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
 SKIP denies use of RC4 ciphers (RFC7465) [reject rc4.badtls.io:11008]
 SKIP denies use of MD5 signature algorithm (RFC6151) [reject weak-sig.badtls.io:11004]
 SKIP denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
 SKIP valid localhost certificate [accept localhost:37623]
 SKIP invalid localhost certificate [reject localhost:43280]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## java-net

```console
# java -version
java version "1.7.0_111"
OpenJDK Runtime Environment (IcedTea 2.6.7) (7u111-2.6.7-1~deb8u1)
OpenJDK 64-Bit Server VM (build 24.111-b01, mixed mode)
```

```console
# trytls https java -classpath java-net Run
platform: Linux (debian 8.5)
runner: trytls 0.3.3 (CPython 2.7.9, OpenSSL 1.0.1t)
stub: java -classpath java-net Run
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 PASS protection against POODLE attack [reject sslv3.dshield.org:443]
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
 PASS expired certificate [reject expired.badssl.com:443]
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 PASS Superfish CA [reject superfish.badssl.com:443]
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
 PASS support for TLS server name indication (SNI) [accept tlsfun.de:443]
 PASS eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
 SKIP valid certificate Common Name [accept domain-match.badtls.io:10000]
 SKIP valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
 SKIP support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
 SKIP TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
 SKIP certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
 SKIP certificate validity starts in future [reject future.badtls.io:11001]
 SKIP mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
 SKIP Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
 SKIP certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
 SKIP expired certificate [reject expired.badtls.io:11006]
 SKIP invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
 SKIP denies use of RC4 ciphers (RFC7465) [reject rc4.badtls.io:11008]
 SKIP denies use of MD5 signature algorithm (RFC6151) [reject weak-sig.badtls.io:11004]
 SKIP denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
 SKIP valid localhost certificate [accept localhost:35232]
 SKIP invalid localhost certificate [reject localhost:37243]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## php-file-get-contents

```console
# php --version
PHP 5.6.24-0+deb8u1 (cli) (built: Jul 26 2016 08:17:07)
Copyright (c) 1997-2016 The PHP Group
Zend Engine v2.6.0, Copyright (c) 1998-2016 Zend Technologies
    with Zend OPcache v7.0.6-dev, Copyright (c) 1999-2016, by Zend Technologies
```

```console
# trytls https php php-file-get-contents/run.php
platform: Linux (debian 8.5)
runner: trytls 0.3.3 (CPython 2.7.9, OpenSSL 1.0.1t)
stub: php php-file-get-contents/run.php
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 PASS protection against POODLE attack [reject sslv3.dshield.org:443]
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
 PASS expired certificate [reject expired.badssl.com:443]
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 PASS Superfish CA [reject superfish.badssl.com:443]
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
 PASS support for TLS server name indication (SNI) [accept tlsfun.de:443]
 PASS eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
 SKIP valid certificate Common Name [accept domain-match.badtls.io:10000]
 SKIP valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
 SKIP support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
 SKIP TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
 SKIP certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
 SKIP certificate validity starts in future [reject future.badtls.io:11001]
 SKIP mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
 SKIP Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
 SKIP certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
 SKIP expired certificate [reject expired.badtls.io:11006]
 SKIP invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
 SKIP denies use of RC4 ciphers (RFC7465) [reject rc4.badtls.io:11008]
 SKIP denies use of MD5 signature algorithm (RFC6151) [reject weak-sig.badtls.io:11004]
 SKIP denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
 SKIP valid localhost certificate [accept localhost:38891]
 SKIP invalid localhost certificate [reject localhost:33827]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

<!-- markdownlint-enable MD013 -->
