# TryTLS testing with Debian 7

```console
docker run -ti --rm debian7
```

```console
# cat /etc/debian_version
7.11
```

<!-- markdownlint-disable MD013 -->

OS         | python2-requests | python2-urllib2 | python3-urllib | go-nethttp | java-https | java-net | php-file-get-contents
---------- | ---------------- | --------------- | -------------- | ---------- | ---------- | -------- | ---------------------
CentOS 7.2 | FAIL             | ERROR           | FAIL           | NO-SNI     | PASS       | PASS     | NO SNI

## python2-requests

```console
# python --version
Python 2.7.3
```

```console
# trytls https python python2-requests/run.py
platform: Linux
runner: trytls 0.3.0 (CPython 3.5.2, OpenSSL 1.0.1e)
stub: python python2-requests/run.py
 PASS valid certificate Common Name [accept domain-match.badtls.io:10000]
 PASS valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
 PASS support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
 PASS TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
 PASS certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
 PASS certificate validity starts in future [reject future.badtls.io:11001]
 PASS mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
 PASS Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
 FAIL MD5 signature algorithm [reject weak-sig.badtls.io:11004]
 PASS certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
 PASS expired certificate [reject expired.badtls.io:11006]
 PASS invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
 FAIL supports RC4 ciphers [reject rc4.badtls.io:11008]
 FAIL supports RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
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
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 PASS protection against POODLE attack [reject sslv3.dshield.org:443]
 PASS eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
 PASS valid localhost certificate [accept localhost:34560]
 PASS invalid localhost certificate [reject localhost:36282]
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
runner: trytls 0.3.0 (CPython 3.5.2, OpenSSL 1.0.1e)
stub: python python2-urllib2/run.py
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
ERROR MD5 signature algorithm [reject weak-sig.badtls.io:11004]
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
ERROR supports RC4 ciphers [reject rc4.badtls.io:11008]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR supports RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
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
ERROR eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR valid localhost certificate [accept localhost:38087]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR invalid localhost certificate [reject localhost:34178]
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
# python3 --version
Python 3.5.2
```

```console
# trytls https python3 python3-urllib/run.py
platform: Linux
runner: trytls 0.3.0 (CPython 3.5.2, OpenSSL 1.0.1e)
stub: python3 python3-urllib/run.py
 PASS valid certificate Common Name [accept domain-match.badtls.io:10000]
 PASS valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
 PASS support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
 PASS TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
 PASS certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
 PASS certificate validity starts in future [reject future.badtls.io:11001]
 PASS mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
 PASS Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
 FAIL MD5 signature algorithm [reject weak-sig.badtls.io:11004]
 PASS certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
 PASS expired certificate [reject expired.badtls.io:11006]
 PASS invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
 PASS supports RC4 ciphers [reject rc4.badtls.io:11008]
 PASS supports RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
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
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 PASS protection against POODLE attack [reject sslv3.dshield.org:443]
 PASS eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
 PASS valid localhost certificate [accept localhost:34017]
 PASS invalid localhost certificate [reject localhost:36174]
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
runner: trytls 0.3.0 (CPython 3.5.2, OpenSSL 1.0.1e)
stub: go run go-nethttp/run.go
 SKIP valid certificate Common Name [accept domain-match.badtls.io:10000]
 SKIP valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
 SKIP support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
 SKIP TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
 SKIP certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
 SKIP certificate validity starts in future [reject future.badtls.io:11001]
 SKIP mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
 SKIP Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
 SKIP MD5 signature algorithm [reject weak-sig.badtls.io:11004]
 SKIP certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
 SKIP expired certificate [reject expired.badtls.io:11006]
 SKIP invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
 SKIP supports RC4 ciphers [reject rc4.badtls.io:11008]
 SKIP supports RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
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
ERROR protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
      reason: stub exited with return code 1
      output: Get https://www.ssllabs.com:10443: remote error: protocol version not supported
              exit status 1
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
ERROR protection against POODLE attack [reject sslv3.dshield.org:443]
      reason: stub exited with return code 1
      output: Get https://sslv3.dshield.org:443: local error: protocol version not supported
              exit status 1
 PASS eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
 SKIP valid localhost certificate [accept localhost:46253]
 SKIP invalid localhost certificate [reject localhost:32995]
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
runner: trytls 0.3.0 (CPython 3.5.2, OpenSSL 1.0.1e)
stub: java -classpath java-https Run
 SKIP valid certificate Common Name [accept domain-match.badtls.io:10000]
 SKIP valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
 SKIP support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
 SKIP TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
 SKIP certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
 SKIP certificate validity starts in future [reject future.badtls.io:11001]
 SKIP mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
 SKIP Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
 SKIP MD5 signature algorithm [reject weak-sig.badtls.io:11004]
 SKIP certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
 SKIP expired certificate [reject expired.badtls.io:11006]
 SKIP invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
 SKIP supports RC4 ciphers [reject rc4.badtls.io:11008]
 SKIP supports RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
      output: javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target
 PASS expired certificate [reject expired.badssl.com:443]
      output: javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: PKIX path validation failed: java.security.cert.CertPathValidatorException: timestamp check failed
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
      output: javax.net.ssl.SSLHandshakeException: java.security.cert.CertificateException: No subject alternative DNS name matching wrong.host.badssl.com found.
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
      output: javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target
 PASS Superfish CA [reject superfish.badssl.com:443]
      output: javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
      output: javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
      output: javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
      output: javax.net.ssl.SSLException: Received fatal alert: protocol_version
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
      output: javax.net.ssl.SSLProtocolException: Protocol violation: server sent a server key exchangemessage for key exchange RSA
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
      output: javax.net.ssl.SSLHandshakeException: DHPublicKey does not comply to algorithm constraints
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
      output: javax.net.ssl.SSLProtocolException: Protocol violation: server sent a server key exchangemessage for key exchange RSA
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
      output: javax.net.ssl.SSLProtocolException: Protocol violation: server sent a server key exchangemessage for key exchange RSA
 PASS protection against POODLE attack [reject sslv3.dshield.org:443]
      output: javax.net.ssl.SSLHandshakeException: Server chose SSLv3, but that protocol version is not enabled or not supported by the client.
 PASS eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
      output: javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target
 SKIP valid localhost certificate [accept localhost:38528]
 SKIP invalid localhost certificate [reject localhost:46750]
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
runner: trytls 0.3.0 (CPython 3.5.2, OpenSSL 1.0.1e)
stub: java -classpath java-net Run
 SKIP valid certificate Common Name [accept domain-match.badtls.io:10000]
 SKIP valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
 SKIP support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
 SKIP TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
 SKIP certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
 SKIP certificate validity starts in future [reject future.badtls.io:11001]
 SKIP mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
 SKIP Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
 SKIP MD5 signature algorithm [reject weak-sig.badtls.io:11004]
 SKIP certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
 SKIP expired certificate [reject expired.badtls.io:11006]
 SKIP invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
 SKIP supports RC4 ciphers [reject rc4.badtls.io:11008]
 SKIP supports RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
      output: javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target
 PASS expired certificate [reject expired.badssl.com:443]
      output: javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: PKIX path validation failed: java.security.cert.CertPathValidatorException: timestamp check failed
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
      output: javax.net.ssl.SSLHandshakeException: java.security.cert.CertificateException: No subject alternative DNS name matching wrong.host.badssl.com found.
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
      output: javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target
 PASS Superfish CA [reject superfish.badssl.com:443]
      output: javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
      output: javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
      output: javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
      output: javax.net.ssl.SSLException: Received fatal alert: protocol_version
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
      output: javax.net.ssl.SSLProtocolException: Protocol violation: server sent a server key exchangemessage for key exchange RSA
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
      output: javax.net.ssl.SSLHandshakeException: DHPublicKey does not comply to algorithm constraints
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
      output: javax.net.ssl.SSLProtocolException: Protocol violation: server sent a server key exchangemessage for key exchange RSA
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
      output: javax.net.ssl.SSLProtocolException: Protocol violation: server sent a server key exchangemessage for key exchange RSA
 PASS protection against POODLE attack [reject sslv3.dshield.org:443]
      output: javax.net.ssl.SSLHandshakeException: Server chose SSLv3, but that protocol version is not enabled or not supported by the client.
 PASS eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
      output: javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target
 SKIP valid localhost certificate [accept localhost:45571]
 SKIP invalid localhost certificate [reject localhost:45449]
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
runner: trytls 0.3.0 (CPython 3.5.2, OpenSSL 1.0.1e)
stub: php php-file-get-contents/run.php
 SKIP valid certificate Common Name [accept domain-match.badtls.io:10000]
 SKIP valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
 SKIP support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
 SKIP TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
 SKIP certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
 SKIP certificate validity starts in future [reject future.badtls.io:11001]
 SKIP mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
 SKIP Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
 SKIP MD5 signature algorithm [reject weak-sig.badtls.io:11004]
 SKIP certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
 SKIP expired certificate [reject expired.badtls.io:11006]
 SKIP invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
 SKIP supports RC4 ciphers [reject rc4.badtls.io:11008]
 SKIP supports RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
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
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
 PASS protection against POODLE attack [reject sslv3.dshield.org:443]
 PASS eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
 SKIP valid localhost certificate [accept localhost:40557]
 SKIP invalid localhost certificate [reject localhost:38690]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

<!-- markdownlint-enable MD013 -->
