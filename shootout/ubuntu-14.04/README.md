# TryTLS testing with Ubuntu

We chose Ubuntu 12.04, 14.04 and 16.04 LTS releases for this TryTLS-shootout
based on the [Ubuntu release end of life](http://www.ubuntu.com/info/release-end-of-life).

```console
docker run -ti --rm ubuntu-14.04
```

```console
# grep DISTRIB_DESCRIPTION /etc/lsb-release
DISTRIB_DESCRIPTION="Ubuntu 14.04.5 LTS"
```

<!-- markdownlint-disable MD013 -->

python2-requests               | python2-urllib2 | python3-urllib    | go-nethttp    | java-https | java-net | php-file-get-contents
------------------------------ | --------------- | ----------------- | ------------- | ---------- | -------- | ---------------------
FAIL(RC4,MD5,RC4+MD5) w/NO-SNI | ERROR           | FAIL(CHK,RC4,MD5) | PASS w/SNI?   | PASS       | PASS     | PASS w/NO-SNI

## python2-requests

```console
# python --version
Python 2.7.6
```

```console
# trytls https python python2-requests/run.py
platform: Linux (Ubuntu 14.04)
runner: trytls 0.3.4 (CPython 2.7.6, OpenSSL 1.0.1f)
stub: python python2-requests/run.py
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 PASS protection against POODLE attack [reject sslv3.dshield.org:443]
 FAIL support for TLS server name indication (SNI) [accept badssl.com:443]
 SKIP self-signed certificate [reject self-signed.badssl.com:443]
      reason: could not detect SNI support
 SKIP expired certificate [reject expired.badssl.com:443]
      reason: could not detect SNI support
 SKIP wrong hostname in certificate [reject wrong.host.badssl.com:443]
      reason: could not detect SNI support
 SKIP SHA-256 signature [accept sha256.badssl.com:443]
      reason: could not detect SNI support
 SKIP 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
      reason: could not detect SNI support
 SKIP incomplete chain of trust [reject incomplete-chain.badssl.com:443]
      reason: could not detect SNI support
 SKIP Superfish CA [reject superfish.badssl.com:443]
      reason: could not detect SNI support
 SKIP eDellRoot CA [reject edellroot.badssl.com:443]
      reason: could not detect SNI support
 SKIP DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
      reason: could not detect SNI support
 FAIL support for TLS server name indication (SNI) [accept tlsfun.de:443]
 SKIP self-signed certificate (temporarily using badssl.com) [reject self-signed.badssl.com:443]
      reason: could not detect SNI support
 SKIP eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
      reason: could not detect SNI support
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
 FAIL denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
 PASS valid localhost certificate [accept localhost:42414]
 PASS invalid localhost certificate [reject localhost:39425]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## python2-urllib2

```console
# python --version
Python 2.7.6
```

```console
# trytls https python python2-urllib2/run.py
platform: Linux (Ubuntu 14.04)
runner: trytls 0.3.4 (CPython 2.7.6, OpenSSL 1.0.1f)
stub: python python2-urllib2/run.py
ERROR protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
ERROR protect against the FREAK attack [reject www.ssllabs.com:10444]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
ERROR protect against the Logjam attack [reject www.ssllabs.com:10445]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
ERROR protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
ERROR protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
ERROR protection against POODLE attack [reject sslv3.dshield.org:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
ERROR support for TLS server name indication (SNI) [accept badssl.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
 SKIP self-signed certificate [reject self-signed.badssl.com:443]
      reason: could not detect SNI support
 SKIP expired certificate [reject expired.badssl.com:443]
      reason: could not detect SNI support
 SKIP wrong hostname in certificate [reject wrong.host.badssl.com:443]
      reason: could not detect SNI support
 SKIP SHA-256 signature [accept sha256.badssl.com:443]
      reason: could not detect SNI support
 SKIP 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
      reason: could not detect SNI support
 SKIP incomplete chain of trust [reject incomplete-chain.badssl.com:443]
      reason: could not detect SNI support
 SKIP Superfish CA [reject superfish.badssl.com:443]
      reason: could not detect SNI support
 SKIP eDellRoot CA [reject edellroot.badssl.com:443]
      reason: could not detect SNI support
 SKIP DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
      reason: could not detect SNI support
ERROR support for TLS server name indication (SNI) [accept tlsfun.de:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
 SKIP self-signed certificate (temporarily using badssl.com) [reject self-signed.badssl.com:443]
      reason: could not detect SNI support
 SKIP eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
      reason: could not detect SNI support
ERROR valid certificate Common Name [accept domain-match.badtls.io:10000]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
ERROR valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
ERROR support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
ERROR TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
ERROR certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
ERROR certificate validity starts in future [reject future.badtls.io:11001]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
ERROR mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
ERROR Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
ERROR certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
ERROR expired certificate [reject expired.badtls.io:11006]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
ERROR invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
ERROR denies use of RC4 ciphers (RFC7465) [reject rc4.badtls.io:11008]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
ERROR denies use of MD5 signature algorithm (RFC6151) [reject weak-sig.badtls.io:11004]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
ERROR denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
ERROR valid localhost certificate [accept localhost:33303]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
ERROR invalid localhost certificate [reject localhost:36770]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
ERROR use only the given CA bundle, not system's [reject sha256.badssl.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 13, in <module>
                  urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
              TypeError: urlopen() got an unexpected keyword argument 'cafile'
```

## python3-urllib

```console
# python3 --version
Python 3.4.3
```

```console
# trytls https python3 python3-urllib/run.py
platform: Linux (Ubuntu 14.04)
runner: trytls 0.3.4 (CPython 2.7.6, OpenSSL 1.0.1f)
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
 FAIL self-signed certificate (temporarily using badssl.com) [reject self-signed.badssl.com:443]
 SKIP eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
      reason: stub didn't reject a self-signed certificate
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
 PASS valid localhost certificate [accept localhost:33275]
 PASS invalid localhost certificate [reject localhost:37997]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## go-nethttp

```console
# go version
go version go1.2.1 linux/amd64
```

```console
# trytls https go-nethttp/run
platform: Linux (Ubuntu 14.04)
runner: trytls 0.3.4 (CPython 2.7.6, OpenSSL 1.0.1f)
stub: go-nethttp/run
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
      output: Get https://www.ssllabs.com:10443: crypto/rsa: verification error
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
      output: Get https://www.ssllabs.com:10444: unexpected ServerKeyExchange
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
      output: Get https://www.ssllabs.com:10445: remote error: handshake failure
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
      output: Get https://cve.freakattack.com:443: x509: certificate signed by unknown authority (possibly because of "x509: cannot verify signature: algorithm unimplemented" while trying to verify candidate authority certificate "COMODO RSA Certification Authority")
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
      output: Get https://cve2.freakattack.com:443: x509: certificate signed by unknown authority (possibly because of "x509: cannot verify signature: algorithm unimplemented" while trying to verify candidate authority certificate "COMODO RSA Certification Authority")
 PASS protection against POODLE attack [reject sslv3.dshield.org:443]
      output: Get https://sslv3.dshield.org:443: local error: protocol version not supported
 FAIL support for TLS server name indication (SNI) [accept badssl.com:443]
      output: Get https://badssl.com:443: x509: certificate signed by unknown authority (possibly because of "x509: cannot verify signature: algorithm unimplemented" while trying to verify candidate authority certificate "COMODO RSA Certification Authority")
 SKIP self-signed certificate [reject self-signed.badssl.com:443]
      reason: could not detect SNI support
 SKIP expired certificate [reject expired.badssl.com:443]
      reason: could not detect SNI support
 SKIP wrong hostname in certificate [reject wrong.host.badssl.com:443]
      reason: could not detect SNI support
 SKIP SHA-256 signature [accept sha256.badssl.com:443]
      reason: could not detect SNI support
 SKIP 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
      reason: could not detect SNI support
 SKIP incomplete chain of trust [reject incomplete-chain.badssl.com:443]
      reason: could not detect SNI support
 SKIP Superfish CA [reject superfish.badssl.com:443]
      reason: could not detect SNI support
 SKIP eDellRoot CA [reject edellroot.badssl.com:443]
      reason: could not detect SNI support
 SKIP DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
      reason: could not detect SNI support
 PASS support for TLS server name indication (SNI) [accept tlsfun.de:443]
 PASS self-signed certificate (temporarily using badssl.com) [reject self-signed.badssl.com:443]
      output: Get https://self-signed.badssl.com:443: x509: certificate signed by unknown authority
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
 SKIP valid localhost certificate [accept localhost:40788]
 SKIP invalid localhost certificate [reject localhost:43219]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## java-https

```console
# java -version
java version "1.7.0_111"
OpenJDK Runtime Environment (IcedTea 2.6.7) (7u111-2.6.7-0ubuntu0.14.04.3)
OpenJDK 64-Bit Server VM (build 24.111-b01, mixed mode)
```

```console
# trytls https java -classpath java-https Run
platform: Linux (Ubuntu 14.04)
runner: trytls 0.3.4 (CPython 2.7.6, OpenSSL 1.0.1f)
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
 PASS self-signed certificate (temporarily using badssl.com) [reject self-signed.badssl.com:443]
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
 SKIP valid localhost certificate [accept localhost:40718]
 SKIP invalid localhost certificate [reject localhost:44225]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## java-net

```console
# java -version
java version "1.7.0_111"
OpenJDK Runtime Environment (IcedTea 2.6.7) (7u111-2.6.7-0ubuntu0.14.04.3)
OpenJDK 64-Bit Server VM (build 24.111-b01, mixed mode)
```

```console
# trytls https java -classpath java-net Run
platform: Linux (Ubuntu 14.04)
runner: trytls 0.3.4 (CPython 2.7.6, OpenSSL 1.0.1f)
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
 PASS self-signed certificate (temporarily using badssl.com) [reject self-signed.badssl.com:443]
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
 SKIP valid localhost certificate [accept localhost:36580]
 SKIP invalid localhost certificate [reject localhost:46476]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## php-file-get-contents

```console
# php --version
PHP 5.5.9-1ubuntu4.19 (cli) (built: Jul 28 2016 19:31:33)
Copyright (c) 1997-2014 The PHP Group
Zend Engine v2.5.0, Copyright (c) 1998-2014 Zend Technologies
    with Zend OPcache v7.0.3, Copyright (c) 1999-2014, by Zend Technologies
```

```console
# trytls https php php-file-get-contents/run.php
platform: Linux (Ubuntu 14.04)
runner: trytls 0.3.4 (CPython 2.7.6, OpenSSL 1.0.1f)
stub: php php-file-get-contents/run.php
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 PASS protection against POODLE attack [reject sslv3.dshield.org:443]
 FAIL support for TLS server name indication (SNI) [accept badssl.com:443]
 SKIP self-signed certificate [reject self-signed.badssl.com:443]
      reason: could not detect SNI support
 SKIP expired certificate [reject expired.badssl.com:443]
      reason: could not detect SNI support
 SKIP wrong hostname in certificate [reject wrong.host.badssl.com:443]
      reason: could not detect SNI support
 SKIP SHA-256 signature [accept sha256.badssl.com:443]
      reason: could not detect SNI support
 SKIP 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
      reason: could not detect SNI support
 SKIP incomplete chain of trust [reject incomplete-chain.badssl.com:443]
      reason: could not detect SNI support
 SKIP Superfish CA [reject superfish.badssl.com:443]
      reason: could not detect SNI support
 SKIP eDellRoot CA [reject edellroot.badssl.com:443]
      reason: could not detect SNI support
 SKIP DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
      reason: could not detect SNI support
 FAIL support for TLS server name indication (SNI) [accept tlsfun.de:443]
 SKIP self-signed certificate (temporarily using badssl.com) [reject self-signed.badssl.com:443]
      reason: could not detect SNI support
 SKIP eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
      reason: could not detect SNI support
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
 SKIP valid localhost certificate [accept localhost:41151]
 SKIP invalid localhost certificate [reject localhost:36320]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

<!-- markdownlint-enable MD013 -->
