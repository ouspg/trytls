# TryTLS testing with Ubuntu

We chose Ubuntu 12.04, 14.04 and 16.04 LTS releases for this TryTLS-shootout
based on the [Ubuntu release end of life](http://www.ubuntu.com/info/release-end-of-life).

<!-- markdownlint-disable MD013 -->

python2-requests | python2-urllib2 | python3-urllib   | go-nethttp     | java-https | java-net | php-file-get-contents
---------------- | --------------- | ---------------- | -------------- | ---------- | -------- | ---------------------
ERROR            | ERROR           | FAIL(CHK,POODLE) | ERROR          | N/A        | N/A      | PASS w/NO SNI

## python2-requests

```console
# trytls https docker run -i --rm shootout-ubuntu12.04 python /root/stubs/python2-requests/run.py
platform: OS X 10.11.5
runner: trytls 0.3.4 (CPython 2.7.10, OpenSSL 0.9.8zh)
stub: docker run -i --rm shootout-ubuntu12.04 python /root/stubs/python2-requests/run.py
ERROR protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
ERROR protect against the FREAK attack [reject www.ssllabs.com:10444]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
ERROR protect against the Logjam attack [reject www.ssllabs.com:10445]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
ERROR protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
ERROR protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
ERROR protection against POODLE attack [reject sslv3.dshield.org:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
ERROR support for TLS server name indication (SNI) [accept badssl.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
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
                File "/root/stubs/python2-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
 SKIP self-signed certificate (temporarily using badssl.com) [reject self-signed.badssl.com:443]
      reason: could not detect SNI support
 SKIP eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
      reason: could not detect SNI support
ERROR valid certificate Common Name [accept domain-match.badtls.io:10000]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
ERROR valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
ERROR support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
ERROR TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
ERROR certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
ERROR certificate validity starts in future [reject future.badtls.io:11001]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
ERROR mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
ERROR Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
ERROR certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
ERROR expired certificate [reject expired.badtls.io:11006]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
ERROR invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
ERROR denies use of RC4 ciphers (RFC7465) [reject rc4.badtls.io:11008]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
ERROR denies use of MD5 signature algorithm (RFC6151) [reject weak-sig.badtls.io:11004]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
ERROR denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
ERROR valid localhost certificate [accept localhost:49781]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
ERROR invalid localhost certificate [reject localhost:49786]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
ERROR use only the given CA bundle, not system's [reject sha256.badssl.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
```

## python2-urllib2

```console
# trytls https docker run -i --rm shootout-ubuntu12.04 python /root/stubs/python2-urllib2/run.py
platform: OS X 10.11.5
runner: trytls 0.3.4 (CPython 2.7.10, OpenSSL 0.9.8zh)
stub: docker run -i --rm shootout-ubuntu12.04 python /root/stubs/python2-urllib2/run.py
ERROR protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR protect against the FREAK attack [reject www.ssllabs.com:10444]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR protect against the Logjam attack [reject www.ssllabs.com:10445]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR protection against POODLE attack [reject sslv3.dshield.org:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR support for TLS server name indication (SNI) [accept badssl.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-urllib2/run.py", line 14, in <module>
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
                File "/root/stubs/python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
 SKIP self-signed certificate (temporarily using badssl.com) [reject self-signed.badssl.com:443]
      reason: could not detect SNI support
 SKIP eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
      reason: could not detect SNI support
ERROR valid certificate Common Name [accept domain-match.badtls.io:10000]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR certificate validity starts in future [reject future.badtls.io:11001]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR expired certificate [reject expired.badtls.io:11006]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR denies use of RC4 ciphers (RFC7465) [reject rc4.badtls.io:11008]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR denies use of MD5 signature algorithm (RFC6151) [reject weak-sig.badtls.io:11004]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR valid localhost certificate [accept localhost:49895]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR invalid localhost certificate [reject localhost:49900]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
ERROR use only the given CA bundle, not system's [reject sha256.badssl.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python2-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError'
```

## python3-urllib

```console
# trytls https docker run -i --rm shootout-ubuntu12.04 python3 /root/stubs/python3-urllib/run.py
platform: OS X 10.11.5
runner: trytls 0.3.4 (CPython 2.7.10, OpenSSL 0.9.8zh)
stub: docker run -i --rm shootout-ubuntu12.04 python3 /root/stubs/python3-urllib/run.py
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
ERROR valid certificate Common Name [accept domain-match.badtls.io:10000]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python3-urllib/run.py", line 14, in <module>
                  urllib.request.urlopen("https://" + host + ":" + port, cafile=cafile)
                File "/usr/lib/python3.2/urllib/request.py", line 128, in urlopen
                  context.load_verify_locations(cafile, capath)
              IOError: [Errno 2] No such file or directory
...
```

## go-nethttp

```console
# trytls https docker run -i --rm shootout-ubuntu12.04 /root/stubs/go-nethttp/run
platform: OS X 10.11.5
runner: trytls 0.3.4 (CPython 2.7.10, OpenSSL 0.9.8zh)
stub: docker run -i --rm shootout-ubuntu12.04 /root/stubs/go-nethttp/run
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
      output: Get https://www.ssllabs.com:10443: remote error: protocol version not supported
ERROR protect against the FREAK attack [reject www.ssllabs.com:10444]
      reason: stub exited with return code 2
      output: panic: crypto: requested hash function is unavailable

              goroutine 1 [running]:
              crypto.Hash.New(0x3800000005, 0x404ab6, 0x7f0664602caf, 0x10)
                /usr/lib/go/src/pkg/crypto/crypto.go:62 +0x95
              crypto/x509.(*Certificate).CheckSignature(0xf84007d840, 0x7f0600000004, 0xf8400a500e, 0xf3f0000041b, 0xf8400a543d, ...)
                /usr/lib/go/src/pkg/crypto/x509/x509.go:391 +0x68
              crypto/x509.(*Certificate).CheckSignatureFrom(0xf84007d580, 0xf84007d840, 0x0, 0x0, 0xf8400a90e0, ...)
                /usr/lib/go/src/pkg/crypto/x509/x509.go:370 +0x15a
              crypto/x509.(*CertPool).findVerifiedParents(0xf8400a7c00, 0xf84007d580, 0x0, 0x0, 0x60, ...)
                /usr/lib/go/src/pkg/crypto/x509/cert_pool.go:44 +0x17d
              crypto/x509.(*Certificate).buildChains(0xf84007d580, 0xf84025b640, 0x7f0664602f48, 0x100000001, 0x7f0664602f60, ...)
                /usr/lib/go/src/pkg/crypto/x509/verify.go:198 +0x1c0
              crypto/x509.(*Certificate).Verify(0xf84007d580, 0x0, 0x0, 0xf8400a7c00, 0xf8400a7ca0, ...)
                /usr/lib/go/src/pkg/crypto/x509/verify.go:177 +0x1c1
              ----- stack segment boundary -----
              crypto/tls.(*Conn).clientHandshake(0xf840073240, 0x0, 0x0, 0x0)
                /usr/lib/go/src/pkg/crypto/tls/handshake_client.go:117 +0xfab
              crypto/tls.(*Conn).Handshake(0xf840073240, 0x0, 0x0, 0xf840073240)
                /usr/lib/go/src/pkg/crypto/tls/conn.go:808 +0xdc
              net/http.(*Transport).getConn(0xf840053a00, 0xf840054810, 0xf840054810, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/transport.go:369 +0x4aa
              net/http.(*Transport).RoundTrip(0xf840053a00, 0xf84007b000, 0x1d, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/transport.go:155 +0x2ba
              net/http.send(0xf84007b000, 0xf840054750, 0xf840053a00, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/client.go:133 +0x3ca
              net/http.(*Client).doFollowingRedirects(0x6a39a8, 0xf84007b000, 0x0, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/client.go:227 +0x5e2
              net/http.(*Client).Get(0x6a39a8, 0xf840051a60, 0x7f060000001d, 0xf800000004, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/client.go:176 +0xb8
              net/http.Get(0xf840051a60, 0x1d, 0x7074746800000008, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/client.go:158 +0x51
              main.main()
                /root/stubs/go-nethttp/run.go:22 +0x159

              goroutine 2 [syscall]:
              created by runtime.main
                /build/buildd/golang-1/src/pkg/runtime/proc.c:221

              goroutine 3 [syscall]:
              syscall.Syscall6()
                /build/buildd/golang-1/src/pkg/syscall/asm_linux_amd64.s:40 +0x5
              syscall.EpollWait(0xf800000006, 0xf840096010, 0xa0000000a, 0xffffffff, 0xc, ...)
                /usr/lib/go/src/pkg/syscall/zerrors_linux_amd64.go:1781 +0xa1
              net.(*pollster).WaitFD(0xf840096000, 0xf840095000, 0x0, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/fd_linux.go:146 +0x110
              net.(*pollServer).Run(0xf840095000, 0x0)
                /usr/lib/go/src/pkg/net/fd.go:236 +0xe4
              created by net.newPollServer
                /usr/lib/go/src/pkg/net/newpollserver.go:35 +0x382
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
      output: Get https://www.ssllabs.com:10445: remote error: handshake failure
ERROR protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
      reason: stub exited with return code 2
      output: panic: crypto: requested hash function is unavailable

              goroutine 1 [running]:
              crypto.Hash.New(0x3800000005, 0x404ab6, 0x7f7f61976caf, 0x10)
                /usr/lib/go/src/pkg/crypto/crypto.go:62 +0x95
              crypto/x509.(*Certificate).CheckSignature(0xf84007d840, 0x7f7f00000004, 0xf8400a400e, 0x10e500000447, 0xf8400a4469, ...)
                /usr/lib/go/src/pkg/crypto/x509/x509.go:391 +0x68
              crypto/x509.(*Certificate).CheckSignatureFrom(0xf84007d580, 0xf84007d840, 0x0, 0x0, 0xf8400ad0e8, ...)
                /usr/lib/go/src/pkg/crypto/x509/x509.go:370 +0x15a
              crypto/x509.(*CertPool).findVerifiedParents(0xf8400abd00, 0xf84007d580, 0x0, 0x0, 0x60, ...)
                /usr/lib/go/src/pkg/crypto/x509/cert_pool.go:44 +0x17d
              crypto/x509.(*Certificate).buildChains(0xf84007d580, 0xf84025fe00, 0x7f7f61976f48, 0x100000001, 0x7f7f61976f60, ...)
                /usr/lib/go/src/pkg/crypto/x509/verify.go:198 +0x1c0
              crypto/x509.(*Certificate).Verify(0xf84007d580, 0x0, 0x0, 0xf8400abd00, 0xf8400abda0, ...)
                /usr/lib/go/src/pkg/crypto/x509/verify.go:177 +0x1c1
              ----- stack segment boundary -----
              crypto/tls.(*Conn).clientHandshake(0xf840073240, 0x0, 0x0, 0x0)
                /usr/lib/go/src/pkg/crypto/tls/handshake_client.go:117 +0xfab
              crypto/tls.(*Conn).Handshake(0xf840073240, 0x0, 0x0, 0xf840073240)
                /usr/lib/go/src/pkg/crypto/tls/conn.go:808 +0xdc
              net/http.(*Transport).getConn(0xf840053a00, 0xf840054810, 0xf840054810, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/transport.go:369 +0x4aa
              net/http.(*Transport).RoundTrip(0xf840053a00, 0xf84007b000, 0x1f, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/transport.go:155 +0x2ba
              net/http.send(0xf84007b000, 0xf840054750, 0xf840053a00, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/client.go:133 +0x3ca
              net/http.(*Client).doFollowingRedirects(0x6a39a8, 0xf84007b000, 0x0, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/client.go:227 +0x5e2
              net/http.(*Client).Get(0x6a39a8, 0xf840051a60, 0x7f7f0000001f, 0xf800000004, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/client.go:176 +0xb8
              net/http.Get(0xf840051a60, 0x1f, 0x7074746800000008, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/client.go:158 +0x51
              main.main()
                /root/stubs/go-nethttp/run.go:22 +0x159

              goroutine 2 [syscall]:
              created by runtime.main
                /build/buildd/golang-1/src/pkg/runtime/proc.c:221

              goroutine 3 [syscall]:
              syscall.Syscall6()
                /build/buildd/golang-1/src/pkg/syscall/asm_linux_amd64.s:40 +0x5
              syscall.EpollWait(0xf800000006, 0xf840096010, 0xa0000000a, 0xffffffff, 0xc, ...)
                /usr/lib/go/src/pkg/syscall/zerrors_linux_amd64.go:1781 +0xa1
              net.(*pollster).WaitFD(0xf840096000, 0xf840095000, 0x0, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/fd_linux.go:146 +0x110
              net.(*pollServer).Run(0xf840095000, 0x0)
                /usr/lib/go/src/pkg/net/fd.go:236 +0xe4
              created by net.newPollServer
                /usr/lib/go/src/pkg/net/newpollserver.go:35 +0x382
ERROR protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
      reason: stub exited with return code 2
      output: panic: crypto: requested hash function is unavailable

              goroutine 1 [running]:
              crypto.Hash.New(0xf800000005, 0x404ab6, 0x7f7c34e75caf, 0x10)
                /usr/lib/go/src/pkg/crypto/crypto.go:62 +0x95
              crypto/x509.(*Certificate).CheckSignature(0xf84007d840, 0x7f7c00000004, 0xf8400a400e, 0x10e500000447, 0xf8400a4469, ...)
                /usr/lib/go/src/pkg/crypto/x509/x509.go:391 +0x68
              crypto/x509.(*Certificate).CheckSignatureFrom(0xf84007d580, 0xf84007d840, 0x0, 0x0, 0xf8400ad0e8, ...)
                /usr/lib/go/src/pkg/crypto/x509/x509.go:370 +0x15a
              crypto/x509.(*CertPool).findVerifiedParents(0xf8400abca0, 0xf84007d580, 0x0, 0x0, 0x60, ...)
                /usr/lib/go/src/pkg/crypto/x509/cert_pool.go:44 +0x17d
              crypto/x509.(*Certificate).buildChains(0xf84007d580, 0xf84012ed00, 0x7f7c34e75f48, 0x100000001, 0x7f7c34e75f60, ...)
                /usr/lib/go/src/pkg/crypto/x509/verify.go:198 +0x1c0
              crypto/x509.(*Certificate).Verify(0xf84007d580, 0x0, 0x0, 0xf8400abca0, 0xf8400abd40, ...)
                /usr/lib/go/src/pkg/crypto/x509/verify.go:177 +0x1c1
              ----- stack segment boundary -----
              crypto/tls.(*Conn).clientHandshake(0xf840073240, 0x0, 0x0, 0x0)
                /usr/lib/go/src/pkg/crypto/tls/handshake_client.go:117 +0xfab
              crypto/tls.(*Conn).Handshake(0xf840073240, 0x0, 0x0, 0xf840073240)
                /usr/lib/go/src/pkg/crypto/tls/conn.go:808 +0xdc
              net/http.(*Transport).getConn(0xf840053a00, 0xf840054d80, 0xf840054d80, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/transport.go:369 +0x4aa
              net/http.(*Transport).RoundTrip(0xf840053a00, 0xf84007b000, 0x20, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/transport.go:155 +0x2ba
              net/http.send(0xf84007b000, 0xf840054750, 0xf840053a00, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/client.go:133 +0x3ca
              net/http.(*Client).doFollowingRedirects(0x6a39a8, 0xf84007b000, 0x0, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/client.go:227 +0x5e2
              net/http.(*Client).Get(0x6a39a8, 0xf8400547b0, 0x7f7c00000020, 0xf800000004, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/client.go:176 +0xb8
              net/http.Get(0xf8400547b0, 0x20, 0x7074746800000008, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/client.go:158 +0x51
              main.main()
                /root/stubs/go-nethttp/run.go:22 +0x159

              goroutine 2 [syscall]:
              created by runtime.main
                /build/buildd/golang-1/src/pkg/runtime/proc.c:221

              goroutine 3 [syscall]:
              syscall.Syscall6()
                /build/buildd/golang-1/src/pkg/syscall/asm_linux_amd64.s:40 +0x5
              syscall.EpollWait(0xf800000006, 0xf840096010, 0xa0000000a, 0xffffffff, 0xc, ...)
                /usr/lib/go/src/pkg/syscall/zerrors_linux_amd64.go:1781 +0xa1
              net.(*pollster).WaitFD(0xf840096000, 0xf840095000, 0x0, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/fd_linux.go:146 +0x110
              net.(*pollServer).Run(0xf840095000, 0x0)
                /usr/lib/go/src/pkg/net/fd.go:236 +0xe4
              created by net.newPollServer
                /usr/lib/go/src/pkg/net/newpollserver.go:35 +0x382
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
ERROR support for TLS server name indication (SNI) [accept tlsfun.de:443]
      reason: stub exited with return code 2
      output: panic: crypto: requested hash function is unavailable

              goroutine 1 [running]:
              crypto.Hash.New(0x3800000005, 0x404ab6, 0x7f3279fd0caf, 0x10)
                /usr/lib/go/src/pkg/crypto/crypto.go:62 +0x95
              crypto/x509.(*Certificate).CheckSignature(0xf84007d840, 0x7f3200000004, 0xf8400a500e, 0xcb2000005b2, 0xf8400a55d4, ...)
                /usr/lib/go/src/pkg/crypto/x509/x509.go:391 +0x68
              crypto/x509.(*Certificate).CheckSignatureFrom(0xf84007d580, 0xf84007d840, 0x0, 0x0, 0xf84006dce0, ...)
                /usr/lib/go/src/pkg/crypto/x509/x509.go:370 +0x15a
              crypto/x509.(*CertPool).findVerifiedParents(0xf8400aa860, 0xf84007d580, 0x0, 0x0, 0x60, ...)
                /usr/lib/go/src/pkg/crypto/x509/cert_pool.go:44 +0x17d
              crypto/x509.(*Certificate).buildChains(0xf84007d580, 0xf8400fcf00, 0x7f3279fd0f48, 0x100000001, 0x7f3279fd0f60, ...)
                /usr/lib/go/src/pkg/crypto/x509/verify.go:198 +0x1c0
              crypto/x509.(*Certificate).Verify(0xf84007d580, 0x0, 0x0, 0xf8400aa860, 0xf8400aa8e0, ...)
                /usr/lib/go/src/pkg/crypto/x509/verify.go:177 +0x1c1
              ----- stack segment boundary -----
              crypto/tls.(*Conn).clientHandshake(0xf840073240, 0x0, 0x0, 0x0)
                /usr/lib/go/src/pkg/crypto/tls/handshake_client.go:117 +0xfab
              crypto/tls.(*Conn).Handshake(0xf840073240, 0x0, 0x0, 0xf840073240)
                /usr/lib/go/src/pkg/crypto/tls/conn.go:808 +0xdc
              net/http.(*Transport).getConn(0xf840053a00, 0xf840054810, 0xf840054810, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/transport.go:369 +0x4aa
              net/http.(*Transport).RoundTrip(0xf840053a00, 0xf84007b000, 0x15, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/transport.go:155 +0x2ba
              net/http.send(0xf84007b000, 0xf840054750, 0xf840053a00, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/client.go:133 +0x3ca
              net/http.(*Client).doFollowingRedirects(0x6a39a8, 0xf84007b000, 0x0, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/client.go:227 +0x5e2
              net/http.(*Client).Get(0x6a39a8, 0xf840051a60, 0x7f3200000015, 0xf800000004, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/client.go:176 +0xb8
              net/http.Get(0xf840051a60, 0x15, 0x7074746800000008, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/client.go:158 +0x51
              main.main()
                /root/stubs/go-nethttp/run.go:22 +0x159

              goroutine 2 [syscall]:
              created by runtime.main
                /build/buildd/golang-1/src/pkg/runtime/proc.c:221

              goroutine 3 [syscall]:
              syscall.Syscall6()
                /build/buildd/golang-1/src/pkg/syscall/asm_linux_amd64.s:40 +0x5
              syscall.EpollWait(0xf800000006, 0xf840096010, 0xa0000000a, 0xffffffff, 0xc, ...)
                /usr/lib/go/src/pkg/syscall/zerrors_linux_amd64.go:1781 +0xa1
              net.(*pollster).WaitFD(0xf840096000, 0xf840095000, 0x0, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/fd_linux.go:146 +0x110
              net.(*pollServer).Run(0xf840095000, 0x0)
                /usr/lib/go/src/pkg/net/fd.go:236 +0xe4
              created by net.newPollServer
                /usr/lib/go/src/pkg/net/newpollserver.go:35 +0x382
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
 SKIP valid localhost certificate [accept localhost:50136]
 SKIP invalid localhost certificate [reject localhost:50141]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## java-https

Java too old to compile this stub in Ubuntu 12.04 LTS.

## java-net

Java too old to compile this stub in Ubuntu 12.04 LTS.

## php-file-get-contents

```console
# trytls https docker run -i --rm shootout-ubuntu12.04 php /root/stubs/php-file-get-contents/run.php
platform: OS X 10.11.5
runner: trytls 0.3.4 (CPython 2.7.10, OpenSSL 0.9.8zh)
stub: docker run -i --rm shootout-ubuntu12.04 php /root/stubs/php-file-get-contents/run.php
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
 SKIP valid localhost certificate [accept localhost:50254]
 SKIP invalid localhost certificate [reject localhost:50259]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

<!-- markdownlint-enable MD013 -->
