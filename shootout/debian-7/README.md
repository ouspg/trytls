# TryTLS testing with Debian 7

```console
docker run -ti --rm debian7
```

```console
# cat /etc/debian_version
7.11
```

<!-- markdownlint-disable MD013 -->

python2-requests               | python2-urllib2 | python3-urllib                           | go-nethttp          | java-https   | java-net | php-file-get-contents
-------------------------------| --------------- | ---------------------------------------- | ------------------- | ----------   | -------- | ---------------------
FAIL(RC4,MD5,RC4+MD5) w/NO SNI | ERROR           | FAIL(CHK,POODLE,RC4,RC5,RC4+MD5)         | PASS w/NO SNI       | PASS |        PASS      | PASS w/NO SNI

## python2-requests

```console
# python --version
Python 2.7.3
```

```console
# trytls https python python2-requests/run.py
platform: Linux
runner: trytls 0.3.4 (CPython 3.5.2, OpenSSL 1.0.1e)
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
 PASS valid localhost certificate [accept localhost:42664]
 PASS invalid localhost certificate [reject localhost:42348]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## python2-urllib2

```console
# python --version
Python 2.7.3
```

```console
# trytls https python python2-urllib2/run.py
platform: Linux
runner: trytls 0.3.4 (CPython 3.5.2, OpenSSL 1.0.1e)
stub: python python2-urllib2/run.py
ERROR protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR protect against the FREAK attack [reject www.ssllabs.com:10444]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR protect against the Logjam attack [reject www.ssllabs.com:10445]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR protection against POODLE attack [reject sslv3.dshield.org:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR support for TLS server name indication (SNI) [accept badssl.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
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
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
 SKIP self-signed certificate (temporarily using badssl.com) [reject self-signed.badssl.com:443]
      reason: could not detect SNI support
 SKIP eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
      reason: could not detect SNI support
ERROR valid certificate Common Name [accept domain-match.badtls.io:10000]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR certificate validity starts in future [reject future.badtls.io:11001]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR expired certificate [reject expired.badtls.io:11006]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR denies use of RC4 ciphers (RFC7465) [reject rc4.badtls.io:11008]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR denies use of MD5 signature algorithm (RFC6151) [reject weak-sig.badtls.io:11004]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR valid localhost certificate [accept localhost:38285]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR invalid localhost certificate [reject localhost:41825]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR use only the given CA bundle, not system's [reject sha256.badssl.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
```

## python3-urllib

```console
# python3.2 --version
Python 3.2.3
```

```console
# trytls https python3.2 python3-urllib/run.py
platform: Linux
runner: trytls 0.3.4 (CPython 3.5.2, OpenSSL 1.0.1e)
stub: python3.2 python3-urllib/run.py
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 FAIL protection against POODLE attack [reject sslv3.dshield.org:443]
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
 FAIL denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
 PASS valid localhost certificate [accept localhost:39893]
 PASS invalid localhost certificate [reject localhost:37622]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## go-nethttp

```console
# go version
go version go1.0.2
```

```console
# trytls https go run go-nethttp/run.go
platform: Linux
runner: trytls 0.3.4 (CPython 3.5.2, OpenSSL 1.0.1e)
stub: go run go-nethttp/run.go
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
      output: Get https://www.ssllabs.com:10443: remote error: protocol version not supported
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
      output: Get https://www.ssllabs.com:10444: x509: certificate signed by unknown authority
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
      output: Get https://www.ssllabs.com:10445: remote error: handshake failure
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
      output: Get https://cve.freakattack.com:443: x509: certificate signed by unknown authority
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
      output: Get https://cve2.freakattack.com:443: x509: certificate signed by unknown authority
 PASS protection against POODLE attack [reject sslv3.dshield.org:443]
      output: Get https://sslv3.dshield.org:443: local error: protocol version not supported
 FAIL support for TLS server name indication (SNI) [accept badssl.com:443]
      output: Get https://badssl.com:443: x509: certificate signed by unknown authority
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
      output: Get https://tlsfun.de:443: x509: certificate signed by unknown authority
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
 SKIP valid localhost certificate [accept localhost:43252]
 SKIP invalid localhost certificate [reject localhost:32841]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## java-https

```console
# java -version
java version "1.7.0_111"
OpenJDK Runtime Environment (IcedTea 2.6.7) (7u111-2.6.7-1~deb7u1)
OpenJDK 64-Bit Server VM (build 24.111-b01, mixed mode)
```

```console
# trytls https java -classpath java-https Run
platform: Linux
runner: trytls 0.3.4 (CPython 3.5.2, OpenSSL 1.0.1e)
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
 SKIP valid localhost certificate [accept localhost:41619]
 SKIP invalid localhost certificate [reject localhost:33237]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## java-net

```console
# java -version
java version "1.7.0_111"
OpenJDK Runtime Environment (IcedTea 2.6.7) (7u111-2.6.7-1~deb7u1)
OpenJDK 64-Bit Server VM (build 24.111-b01, mixed mode)
```

```console
# trytls https java -classpath java-net Run
platform: Linux
runner: trytls 0.3.4 (CPython 3.5.2, OpenSSL 1.0.1e)
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
 SKIP valid localhost certificate [accept localhost:45245]
 SKIP invalid localhost certificate [reject localhost:43911]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## php-file-get-contents

```console
# php --version
PHP 5.4.45-0+deb7u4 (cli) (built: Jun 29 2016 14:51:18)
Copyright (c) 1997-2014 The PHP Group
Zend Engine v2.4.0, Copyright (c) 1998-2014 Zend Technologies
```

```console
# trytls https php php-file-get-contents/run.php
platform: Linux
runner: trytls 0.3.4 (CPython 3.5.2, OpenSSL 1.0.1e)
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
 SKIP valid localhost certificate [accept localhost:40678]
 SKIP invalid localhost certificate [reject localhost:41923]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

<!-- markdownlint-enable MD013 -->
