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
CentOS 7.2 | ?                | ?               | ?              | ?          | ?          | ?        | ?

## python2-requests

```console
# python --version
Python 2.7.9
```

```console
# trytls https python python2-requests/run.py
[1mplatform:[0m Linux (debian 8.5)[0m
[0m[1mrunner:[0m trytls 0.3.2 (CPython 2.7.9, OpenSSL 1.0.1t)[0m
[0m[1mstub:[0m python python2-requests/run.py[0m
[0m[32m PASS[0m protect against Apple's TLS vulnerability CVE-2014-1266 [2m[reject www.ssllabs.com:10443][0m
[0m[32m PASS[0m protect against the FREAK attack [2m[reject www.ssllabs.com:10444][0m
[0m[32m PASS[0m protect against the Logjam attack [2m[reject www.ssllabs.com:10445][0m
[0m[32m PASS[0m protect against FREAK attack (test server 1) [2m[reject cve.freakattack.com:443][0m
[0m[32m PASS[0m protect against FREAK attack (test server 2) [2m[reject cve2.freakattack.com:443][0m
[0m[31m FAIL[0m[31m protection against POODLE attack [2m[accept sslv3.dshield.org:443][0m
[0m[32m PASS[0m support for TLS server name indication (SNI) [2m[accept badssl.com:443][0m
[0m[32m PASS[0m self-signed certificate [2m[reject self-signed.badssl.com:443][0m
[0m[32m PASS[0m expired certificate [2m[reject expired.badssl.com:443][0m
[0m[32m PASS[0m wrong hostname in certificate [2m[reject wrong.host.badssl.com:443][0m
[0m[32m PASS[0m SHA-256 signature [2m[accept sha256.badssl.com:443][0m
[0m[32m PASS[0m 1000 subjectAltNames [2m[accept 1000-sans.badssl.com:443][0m
[0m[32m PASS[0m incomplete chain of trust [2m[reject incomplete-chain.badssl.com:443][0m
[0m[32m PASS[0m Superfish CA [2m[reject superfish.badssl.com:443][0m
[0m[32m PASS[0m eDellRoot CA [2m[reject edellroot.badssl.com:443][0m
[0m[32m PASS[0m DSDTestProvider CA [2m[reject dsdtestprovider.badssl.com:443][0m
[0m[32m PASS[0m support for TLS server name indication (SNI) [2m[accept tlsfun.de:443][0m
[0m[32m PASS[0m self-signed certificate [2m[reject expired.tlsfun.de:443][0m
[0m[32m PASS[0m eDellRoot CA #2 [2m[reject badcert-edell.tlsfun.de:443][0m
[0m[32m PASS[0m valid certificate Common Name [2m[accept domain-match.badtls.io:10000][0m
[0m[32m PASS[0m valid wildcard certificate Common Name [2m[accept wildcard-match.badtls.io:10001][0m
[0m[32m PASS[0m support for Subject Alternative Name (SAN) [2m[accept san-match.badtls.io:10002][0m
[0m[32m PASS[0m TLS handshake with 1024 bit Diffie-Hellman (DH) [2m[accept dh1024.badtls.io:10005][0m
[0m[32m PASS[0m certificate expired in year 1963 [2m[reject expired-1963.badtls.io:11000][0m
[0m[32m PASS[0m certificate validity starts in future [2m[reject future.badtls.io:11001][0m
[0m[32m PASS[0m mismatch in certificate's Common Name [2m[reject domain-mismatch.badtls.io:11002][0m
[0m[32m PASS[0m Subject Alternative Name (SAN) mismatch [2m[reject san-mismatch.badtls.io:11003][0m
[0m[31m FAIL[0m[31m MD5 signature algorithm [2m[reject weak-sig.badtls.io:11004][0m
[0m[32m PASS[0m certificate has invalid key usage for HTTPS connection [2m[reject bad-key-usage.badtls.io:11005][0m
[0m[32m PASS[0m expired certificate [2m[reject expired.badtls.io:11006][0m
[0m[32m PASS[0m invalid wildcard certificate Common Name [2m[reject wildcard.mismatch.badtls.io:11007][0m
[0m[32m PASS[0m supports RC4 ciphers [2m[reject rc4.badtls.io:11008][0m
[0m[32m PASS[0m supports RC4 with MD5 ciphers [2m[reject rc4-md5.badtls.io:11009][0m
[0m[32m PASS[0m valid localhost certificate [2m[accept localhost:45109][0m
[0m[32m PASS[0m invalid localhost certificate [2m[reject localhost:45566][0m
[0m[32m PASS[0m use only the given CA bundle, not system's [2m[reject sha256.badssl.com:443][0m
[0m[0m```

## python2-urllib2

```console
# python --version
Python 2.7.9
```

```console
# trytls https python python2-urllib2/run.py
[1mplatform:[0m Linux (debian 8.5)[0m
[0m[1mrunner:[0m trytls 0.3.2 (CPython 2.7.9, OpenSSL 1.0.1t)[0m
[0m[1mstub:[0m python python2-urllib2/run.py[0m
[0m[32m PASS[0m protect against Apple's TLS vulnerability CVE-2014-1266 [2m[reject www.ssllabs.com:10443][0m
[0m[32m PASS[0m protect against the FREAK attack [2m[reject www.ssllabs.com:10444][0m
[0m[32m PASS[0m protect against the Logjam attack [2m[reject www.ssllabs.com:10445][0m
[0m[32m PASS[0m protect against FREAK attack (test server 1) [2m[reject cve.freakattack.com:443][0m
[0m[32m PASS[0m protect against FREAK attack (test server 2) [2m[reject cve2.freakattack.com:443][0m
[0m[31m FAIL[0m[31m protection against POODLE attack [2m[accept sslv3.dshield.org:443][0m
[0m[32m PASS[0m support for TLS server name indication (SNI) [2m[accept badssl.com:443][0m
[0m[32m PASS[0m self-signed certificate [2m[reject self-signed.badssl.com:443][0m
[0m[32m PASS[0m expired certificate [2m[reject expired.badssl.com:443][0m
[0m[32m PASS[0m wrong hostname in certificate [2m[reject wrong.host.badssl.com:443][0m
[0m[32m PASS[0m SHA-256 signature [2m[accept sha256.badssl.com:443][0m
[0m[32m PASS[0m 1000 subjectAltNames [2m[accept 1000-sans.badssl.com:443][0m
[0m[32m PASS[0m incomplete chain of trust [2m[reject incomplete-chain.badssl.com:443][0m
[0m[32m PASS[0m Superfish CA [2m[reject superfish.badssl.com:443][0m
[0m[32m PASS[0m eDellRoot CA [2m[reject edellroot.badssl.com:443][0m
[0m[32m PASS[0m DSDTestProvider CA [2m[reject dsdtestprovider.badssl.com:443][0m
[0m[32m PASS[0m support for TLS server name indication (SNI) [2m[accept tlsfun.de:443][0m
[0m[32m PASS[0m self-signed certificate [2m[reject expired.tlsfun.de:443][0m
[0m[32m PASS[0m eDellRoot CA #2 [2m[reject badcert-edell.tlsfun.de:443][0m
[0m[32m PASS[0m valid certificate Common Name [2m[accept domain-match.badtls.io:10000][0m
[0m[32m PASS[0m valid wildcard certificate Common Name [2m[accept wildcard-match.badtls.io:10001][0m
[0m[32m PASS[0m support for Subject Alternative Name (SAN) [2m[accept san-match.badtls.io:10002][0m
[0m[32m PASS[0m TLS handshake with 1024 bit Diffie-Hellman (DH) [2m[accept dh1024.badtls.io:10005][0m
[0m[32m PASS[0m certificate expired in year 1963 [2m[reject expired-1963.badtls.io:11000][0m
[0m[32m PASS[0m certificate validity starts in future [2m[reject future.badtls.io:11001][0m
[0m[32m PASS[0m mismatch in certificate's Common Name [2m[reject domain-mismatch.badtls.io:11002][0m
[0m[32m PASS[0m Subject Alternative Name (SAN) mismatch [2m[reject san-mismatch.badtls.io:11003][0m
[0m[31m FAIL[0m[31m MD5 signature algorithm [2m[reject weak-sig.badtls.io:11004][0m
[0m[32m PASS[0m certificate has invalid key usage for HTTPS connection [2m[reject bad-key-usage.badtls.io:11005][0m
[0m[32m PASS[0m expired certificate [2m[reject expired.badtls.io:11006][0m
[0m[32m PASS[0m invalid wildcard certificate Common Name [2m[reject wildcard.mismatch.badtls.io:11007][0m
[0m[31m FAIL[0m[31m supports RC4 ciphers [2m[reject rc4.badtls.io:11008][0m
[0m[32m PASS[0m supports RC4 with MD5 ciphers [2m[reject rc4-md5.badtls.io:11009][0m
[0m[32m PASS[0m valid localhost certificate [2m[accept localhost:44679][0m
[0m[32m PASS[0m invalid localhost certificate [2m[reject localhost:34013][0m
[0m[32m PASS[0m use only the given CA bundle, not system's [2m[reject sha256.badssl.com:443][0m
[0m[0m```

## python3-urllib

```console
# python3 --version
Python 3.4.2
```

```console
# trytls https python3 python3-urllib/run.py
[1mplatform:[0m Linux (debian 8.5)[0m
[0m[1mrunner:[0m trytls 0.3.2 (CPython 2.7.9, OpenSSL 1.0.1t)[0m
[0m[1mstub:[0m python3 python3-urllib/run.py[0m
[0m[32m PASS[0m protect against Apple's TLS vulnerability CVE-2014-1266 [2m[reject www.ssllabs.com:10443][0m
[0m[32m PASS[0m protect against the FREAK attack [2m[reject www.ssllabs.com:10444][0m
[0m[32m PASS[0m protect against the Logjam attack [2m[reject www.ssllabs.com:10445][0m
[0m[32m PASS[0m protect against FREAK attack (test server 1) [2m[reject cve.freakattack.com:443][0m
[0m[32m PASS[0m protect against FREAK attack (test server 2) [2m[reject cve2.freakattack.com:443][0m
[0m[31m FAIL[0m[31m protection against POODLE attack [2m[accept sslv3.dshield.org:443][0m
[0m[32m PASS[0m support for TLS server name indication (SNI) [2m[accept badssl.com:443][0m
[0m[31m FAIL[0m[31m self-signed certificate [2m[reject self-signed.badssl.com:443][0m
[0m[2m SKIP[0m[2m expired certificate [2m[reject expired.badssl.com:443][0m[2m
      reason: stub didn't reject a self-signed certificate[0m
[0m[2m SKIP[0m[2m wrong hostname in certificate [2m[reject wrong.host.badssl.com:443][0m[2m
      reason: stub didn't reject a self-signed certificate[0m
[0m[2m SKIP[0m[2m SHA-256 signature [2m[accept sha256.badssl.com:443][0m[2m
      reason: stub didn't reject a self-signed certificate[0m
[0m[2m SKIP[0m[2m 1000 subjectAltNames [2m[accept 1000-sans.badssl.com:443][0m[2m
      reason: stub didn't reject a self-signed certificate[0m
[0m[2m SKIP[0m[2m incomplete chain of trust [2m[reject incomplete-chain.badssl.com:443][0m[2m
      reason: stub didn't reject a self-signed certificate[0m
[0m[2m SKIP[0m[2m Superfish CA [2m[reject superfish.badssl.com:443][0m[2m
      reason: stub didn't reject a self-signed certificate[0m
[0m[2m SKIP[0m[2m eDellRoot CA [2m[reject edellroot.badssl.com:443][0m[2m
      reason: stub didn't reject a self-signed certificate[0m
[0m[2m SKIP[0m[2m DSDTestProvider CA [2m[reject dsdtestprovider.badssl.com:443][0m[2m
      reason: stub didn't reject a self-signed certificate[0m
[0m[32m PASS[0m support for TLS server name indication (SNI) [2m[accept tlsfun.de:443][0m
[0m[31m[41m[37mERROR[0m[31m self-signed certificate [2m[reject expired.tlsfun.de:443][0m[31m
      reason: stub exited with return code 1[0m[31m
      output: [2mTraceback (most recent call last):
                File "python3-urllib/run.py", line 14, in <module>
                  urllib.request.urlopen("https://" + host + ":" + port, cafile=cafile)
                File "/usr/lib/python3.4/urllib/request.py", line 153, in urlopen
                  return opener.open(url, data, timeout)
                File "/usr/lib/python3.4/urllib/request.py", line 461, in open
                  response = meth(req, response)
                File "/usr/lib/python3.4/urllib/request.py", line 571, in http_response
                  'http', request, response, code, msg, hdrs)
                File "/usr/lib/python3.4/urllib/request.py", line 499, in error
                  return self._call_chain(*args)
                File "/usr/lib/python3.4/urllib/request.py", line 433, in _call_chain
                  result = func(*args)
                File "/usr/lib/python3.4/urllib/request.py", line 579, in http_error_default
                  raise HTTPError(req.full_url, code, msg, hdrs, fp)
              urllib.error.HTTPError: HTTP Error 403: Forbidden[0m
[0m[2m SKIP[0m[2m eDellRoot CA #2 [2m[reject badcert-edell.tlsfun.de:443][0m[2m
      reason: stub didn't reject a self-signed certificate[0m
[0m[32m PASS[0m valid certificate Common Name [2m[accept domain-match.badtls.io:10000][0m
[0m[32m PASS[0m valid wildcard certificate Common Name [2m[accept wildcard-match.badtls.io:10001][0m
[0m[32m PASS[0m support for Subject Alternative Name (SAN) [2m[accept san-match.badtls.io:10002][0m
[0m[32m PASS[0m TLS handshake with 1024 bit Diffie-Hellman (DH) [2m[accept dh1024.badtls.io:10005][0m
[0m[32m PASS[0m certificate expired in year 1963 [2m[reject expired-1963.badtls.io:11000][0m
[0m[32m PASS[0m certificate validity starts in future [2m[reject future.badtls.io:11001][0m
[0m[32m PASS[0m mismatch in certificate's Common Name [2m[reject domain-mismatch.badtls.io:11002][0m
[0m[32m PASS[0m Subject Alternative Name (SAN) mismatch [2m[reject san-mismatch.badtls.io:11003][0m
[0m[31m FAIL[0m[31m MD5 signature algorithm [2m[reject weak-sig.badtls.io:11004][0m
[0m[32m PASS[0m certificate has invalid key usage for HTTPS connection [2m[reject bad-key-usage.badtls.io:11005][0m
[0m[32m PASS[0m expired certificate [2m[reject expired.badtls.io:11006][0m
[0m[32m PASS[0m invalid wildcard certificate Common Name [2m[reject wildcard.mismatch.badtls.io:11007][0m
[0m[31m FAIL[0m[31m supports RC4 ciphers [2m[reject rc4.badtls.io:11008][0m
[0m[32m PASS[0m supports RC4 with MD5 ciphers [2m[reject rc4-md5.badtls.io:11009][0m
[0m[32m PASS[0m valid localhost certificate [2m[accept localhost:38778][0m
[0m[32m PASS[0m invalid localhost certificate [2m[reject localhost:45981][0m
[0m[32m PASS[0m use only the given CA bundle, not system's [2m[reject sha256.badssl.com:443][0m
[0m[0m```

## go-nethttp

```console
# go version
go version go1.3.3 linux/amd64
```

```console
# trytls https go-nethttp/run
[1mplatform:[0m Linux (debian 8.5)[0m
[0m[1mrunner:[0m trytls 0.3.2 (CPython 2.7.9, OpenSSL 1.0.1t)[0m
[0m[1mstub:[0m go-nethttp/run[0m
[0m[32m PASS[0m protect against Apple's TLS vulnerability CVE-2014-1266 [2m[reject www.ssllabs.com:10443][0m
      output: [2mGet https://www.ssllabs.com:10443: crypto/rsa: verification error[0m
[0m[32m PASS[0m protect against the FREAK attack [2m[reject www.ssllabs.com:10444][0m
      output: [2mGet https://www.ssllabs.com:10444: tls: unexpected ServerKeyExchange[0m
[0m[32m PASS[0m protect against the Logjam attack [2m[reject www.ssllabs.com:10445][0m
      output: [2mGet https://www.ssllabs.com:10445: remote error: handshake failure[0m
[0m[32m PASS[0m protect against FREAK attack (test server 1) [2m[reject cve.freakattack.com:443][0m
      output: [2mGet https://cve.freakattack.com:443: tls: unexpected ServerKeyExchange[0m
[0m[32m PASS[0m protect against FREAK attack (test server 2) [2m[reject cve2.freakattack.com:443][0m
      output: [2mGet https://cve2.freakattack.com:443: tls: unexpected ServerKeyExchange[0m
[0m[31m FAIL[0m[31m protection against POODLE attack [2m[accept sslv3.dshield.org:443][0m[31m
      output: Get https://sslv3.dshield.org:443: tls: server selected unsupported protocol version 300[0m
[0m[32m PASS[0m support for TLS server name indication (SNI) [2m[accept badssl.com:443][0m
[0m[32m PASS[0m self-signed certificate [2m[reject self-signed.badssl.com:443][0m
      output: [2mGet https://self-signed.badssl.com:443: x509: certificate signed by unknown authority[0m
[0m[32m PASS[0m expired certificate [2m[reject expired.badssl.com:443][0m
      output: [2mGet https://expired.badssl.com:443: x509: certificate has expired or is not yet valid[0m
[0m[32m PASS[0m wrong hostname in certificate [2m[reject wrong.host.badssl.com:443][0m
      output: [2mGet https://wrong.host.badssl.com:443: x509: certificate is valid for *.badssl.com, badssl.com, not wrong.host.badssl.com[0m
[0m[32m PASS[0m SHA-256 signature [2m[accept sha256.badssl.com:443][0m
[0m[32m PASS[0m 1000 subjectAltNames [2m[accept 1000-sans.badssl.com:443][0m
[0m[32m PASS[0m incomplete chain of trust [2m[reject incomplete-chain.badssl.com:443][0m
      output: [2mGet https://incomplete-chain.badssl.com:443: x509: certificate signed by unknown authority[0m
[0m[32m PASS[0m Superfish CA [2m[reject superfish.badssl.com:443][0m
      output: [2mGet https://superfish.badssl.com:443: x509: certificate signed by unknown authority[0m
[0m[32m PASS[0m eDellRoot CA [2m[reject edellroot.badssl.com:443][0m
      output: [2mGet https://edellroot.badssl.com:443: x509: certificate signed by unknown authority[0m
[0m[32m PASS[0m DSDTestProvider CA [2m[reject dsdtestprovider.badssl.com:443][0m
      output: [2mGet https://dsdtestprovider.badssl.com:443: x509: certificate signed by unknown authority[0m
[0m[32m PASS[0m support for TLS server name indication (SNI) [2m[accept tlsfun.de:443][0m
[0m[32m PASS[0m self-signed certificate [2m[reject expired.tlsfun.de:443][0m
      output: [2mGet https://expired.tlsfun.de:443: x509: certificate has expired or is not yet valid[0m
[0m[32m PASS[0m eDellRoot CA #2 [2m[reject badcert-edell.tlsfun.de:443][0m
      output: [2mGet https://badcert-edell.tlsfun.de:443: x509: certificate signed by unknown authority[0m
[0m[2m SKIP[0m[2m valid certificate Common Name [2m[accept domain-match.badtls.io:10000][0m
[0m[2m SKIP[0m[2m valid wildcard certificate Common Name [2m[accept wildcard-match.badtls.io:10001][0m
[0m[2m SKIP[0m[2m support for Subject Alternative Name (SAN) [2m[accept san-match.badtls.io:10002][0m
[0m[2m SKIP[0m[2m TLS handshake with 1024 bit Diffie-Hellman (DH) [2m[accept dh1024.badtls.io:10005][0m
[0m[2m SKIP[0m[2m certificate expired in year 1963 [2m[reject expired-1963.badtls.io:11000][0m
[0m[2m SKIP[0m[2m certificate validity starts in future [2m[reject future.badtls.io:11001][0m
[0m[2m SKIP[0m[2m mismatch in certificate's Common Name [2m[reject domain-mismatch.badtls.io:11002][0m
[0m[2m SKIP[0m[2m Subject Alternative Name (SAN) mismatch [2m[reject san-mismatch.badtls.io:11003][0m
[0m[2m SKIP[0m[2m MD5 signature algorithm [2m[reject weak-sig.badtls.io:11004][0m
[0m[2m SKIP[0m[2m certificate has invalid key usage for HTTPS connection [2m[reject bad-key-usage.badtls.io:11005][0m
[0m[2m SKIP[0m[2m expired certificate [2m[reject expired.badtls.io:11006][0m
[0m[2m SKIP[0m[2m invalid wildcard certificate Common Name [2m[reject wildcard.mismatch.badtls.io:11007][0m
[0m[2m SKIP[0m[2m supports RC4 ciphers [2m[reject rc4.badtls.io:11008][0m
[0m[2m SKIP[0m[2m supports RC4 with MD5 ciphers [2m[reject rc4-md5.badtls.io:11009][0m
[0m[2m SKIP[0m[2m valid localhost certificate [2m[accept localhost:42274][0m
[0m[2m SKIP[0m[2m invalid localhost certificate [2m[reject localhost:43663][0m
[0m[2m SKIP[0m[2m use only the given CA bundle, not system's [2m[reject sha256.badssl.com:443][0m
[0m[0m```

## java-https

```console
# java -version
java version "1.7.0_111"
OpenJDK Runtime Environment (IcedTea 2.6.7) (7u111-2.6.7-1~deb8u1)
OpenJDK 64-Bit Server VM (build 24.111-b01, mixed mode)
```

```console
# trytls https java -classpath java-https Run
[1mplatform:[0m Linux (debian 8.5)[0m
[0m[1mrunner:[0m trytls 0.3.2 (CPython 2.7.9, OpenSSL 1.0.1t)[0m
[0m[1mstub:[0m java -classpath java-https Run[0m
[0m[32m PASS[0m protect against Apple's TLS vulnerability CVE-2014-1266 [2m[reject www.ssllabs.com:10443][0m
[0m[32m PASS[0m protect against the FREAK attack [2m[reject www.ssllabs.com:10444][0m
[0m[32m PASS[0m protect against the Logjam attack [2m[reject www.ssllabs.com:10445][0m
[0m[32m PASS[0m protect against FREAK attack (test server 1) [2m[reject cve.freakattack.com:443][0m
[0m[32m PASS[0m protect against FREAK attack (test server 2) [2m[reject cve2.freakattack.com:443][0m
[0m[31m FAIL[0m[31m protection against POODLE attack [2m[accept sslv3.dshield.org:443][0m
[0m[32m PASS[0m support for TLS server name indication (SNI) [2m[accept badssl.com:443][0m
[0m[32m PASS[0m self-signed certificate [2m[reject self-signed.badssl.com:443][0m
[0m[32m PASS[0m expired certificate [2m[reject expired.badssl.com:443][0m
[0m[32m PASS[0m wrong hostname in certificate [2m[reject wrong.host.badssl.com:443][0m
[0m[32m PASS[0m SHA-256 signature [2m[accept sha256.badssl.com:443][0m
[0m[32m PASS[0m 1000 subjectAltNames [2m[accept 1000-sans.badssl.com:443][0m
[0m[32m PASS[0m incomplete chain of trust [2m[reject incomplete-chain.badssl.com:443][0m
[0m[32m PASS[0m Superfish CA [2m[reject superfish.badssl.com:443][0m
[0m[32m PASS[0m eDellRoot CA [2m[reject edellroot.badssl.com:443][0m
[0m[32m PASS[0m DSDTestProvider CA [2m[reject dsdtestprovider.badssl.com:443][0m
[0m[32m PASS[0m support for TLS server name indication (SNI) [2m[accept tlsfun.de:443][0m
[0m[32m PASS[0m self-signed certificate [2m[reject expired.tlsfun.de:443][0m
[0m[32m PASS[0m eDellRoot CA #2 [2m[reject badcert-edell.tlsfun.de:443][0m
[0m[2m SKIP[0m[2m valid certificate Common Name [2m[accept domain-match.badtls.io:10000][0m
[0m[2m SKIP[0m[2m valid wildcard certificate Common Name [2m[accept wildcard-match.badtls.io:10001][0m
[0m[2m SKIP[0m[2m support for Subject Alternative Name (SAN) [2m[accept san-match.badtls.io:10002][0m
[0m[2m SKIP[0m[2m TLS handshake with 1024 bit Diffie-Hellman (DH) [2m[accept dh1024.badtls.io:10005][0m
[0m[2m SKIP[0m[2m certificate expired in year 1963 [2m[reject expired-1963.badtls.io:11000][0m
[0m[2m SKIP[0m[2m certificate validity starts in future [2m[reject future.badtls.io:11001][0m
[0m[2m SKIP[0m[2m mismatch in certificate's Common Name [2m[reject domain-mismatch.badtls.io:11002][0m
[0m[2m SKIP[0m[2m Subject Alternative Name (SAN) mismatch [2m[reject san-mismatch.badtls.io:11003][0m
[0m[2m SKIP[0m[2m MD5 signature algorithm [2m[reject weak-sig.badtls.io:11004][0m
[0m[2m SKIP[0m[2m certificate has invalid key usage for HTTPS connection [2m[reject bad-key-usage.badtls.io:11005][0m
[0m[2m SKIP[0m[2m expired certificate [2m[reject expired.badtls.io:11006][0m
[0m[2m SKIP[0m[2m invalid wildcard certificate Common Name [2m[reject wildcard.mismatch.badtls.io:11007][0m
[0m[2m SKIP[0m[2m supports RC4 ciphers [2m[reject rc4.badtls.io:11008][0m
[0m[2m SKIP[0m[2m supports RC4 with MD5 ciphers [2m[reject rc4-md5.badtls.io:11009][0m
[0m[2m SKIP[0m[2m valid localhost certificate [2m[accept localhost:34829][0m
[0m[2m SKIP[0m[2m invalid localhost certificate [2m[reject localhost:33216][0m
[0m[2m SKIP[0m[2m use only the given CA bundle, not system's [2m[reject sha256.badssl.com:443][0m
[0m[0m```

## java-net

```console
# java -version
java version "1.7.0_111"
OpenJDK Runtime Environment (IcedTea 2.6.7) (7u111-2.6.7-1~deb8u1)
OpenJDK 64-Bit Server VM (build 24.111-b01, mixed mode)
```

```console
# trytls https java -classpath java-net Run
[1mplatform:[0m Linux (debian 8.5)[0m
[0m[1mrunner:[0m trytls 0.3.2 (CPython 2.7.9, OpenSSL 1.0.1t)[0m
[0m[1mstub:[0m java -classpath java-net Run[0m
[0m[32m PASS[0m protect against Apple's TLS vulnerability CVE-2014-1266 [2m[reject www.ssllabs.com:10443][0m
[0m[32m PASS[0m protect against the FREAK attack [2m[reject www.ssllabs.com:10444][0m
[0m[32m PASS[0m protect against the Logjam attack [2m[reject www.ssllabs.com:10445][0m
[0m[32m PASS[0m protect against FREAK attack (test server 1) [2m[reject cve.freakattack.com:443][0m
[0m[32m PASS[0m protect against FREAK attack (test server 2) [2m[reject cve2.freakattack.com:443][0m
[0m[31m FAIL[0m[31m protection against POODLE attack [2m[accept sslv3.dshield.org:443][0m
[0m[32m PASS[0m support for TLS server name indication (SNI) [2m[accept badssl.com:443][0m
[0m[32m PASS[0m self-signed certificate [2m[reject self-signed.badssl.com:443][0m
[0m[32m PASS[0m expired certificate [2m[reject expired.badssl.com:443][0m
[0m[32m PASS[0m wrong hostname in certificate [2m[reject wrong.host.badssl.com:443][0m
[0m[32m PASS[0m SHA-256 signature [2m[accept sha256.badssl.com:443][0m
[0m[32m PASS[0m 1000 subjectAltNames [2m[accept 1000-sans.badssl.com:443][0m
[0m[32m PASS[0m incomplete chain of trust [2m[reject incomplete-chain.badssl.com:443][0m
[0m[32m PASS[0m Superfish CA [2m[reject superfish.badssl.com:443][0m
[0m[32m PASS[0m eDellRoot CA [2m[reject edellroot.badssl.com:443][0m
[0m[32m PASS[0m DSDTestProvider CA [2m[reject dsdtestprovider.badssl.com:443][0m
[0m[32m PASS[0m support for TLS server name indication (SNI) [2m[accept tlsfun.de:443][0m
[0m[32m PASS[0m self-signed certificate [2m[reject expired.tlsfun.de:443][0m
[0m[32m PASS[0m eDellRoot CA #2 [2m[reject badcert-edell.tlsfun.de:443][0m
[0m[2m SKIP[0m[2m valid certificate Common Name [2m[accept domain-match.badtls.io:10000][0m
[0m[2m SKIP[0m[2m valid wildcard certificate Common Name [2m[accept wildcard-match.badtls.io:10001][0m
[0m[2m SKIP[0m[2m support for Subject Alternative Name (SAN) [2m[accept san-match.badtls.io:10002][0m
[0m[2m SKIP[0m[2m TLS handshake with 1024 bit Diffie-Hellman (DH) [2m[accept dh1024.badtls.io:10005][0m
[0m[2m SKIP[0m[2m certificate expired in year 1963 [2m[reject expired-1963.badtls.io:11000][0m
[0m[2m SKIP[0m[2m certificate validity starts in future [2m[reject future.badtls.io:11001][0m
[0m[2m SKIP[0m[2m mismatch in certificate's Common Name [2m[reject domain-mismatch.badtls.io:11002][0m
[0m[2m SKIP[0m[2m Subject Alternative Name (SAN) mismatch [2m[reject san-mismatch.badtls.io:11003][0m
[0m[2m SKIP[0m[2m MD5 signature algorithm [2m[reject weak-sig.badtls.io:11004][0m
[0m[2m SKIP[0m[2m certificate has invalid key usage for HTTPS connection [2m[reject bad-key-usage.badtls.io:11005][0m
[0m[2m SKIP[0m[2m expired certificate [2m[reject expired.badtls.io:11006][0m
[0m[2m SKIP[0m[2m invalid wildcard certificate Common Name [2m[reject wildcard.mismatch.badtls.io:11007][0m
[0m[2m SKIP[0m[2m supports RC4 ciphers [2m[reject rc4.badtls.io:11008][0m
[0m[2m SKIP[0m[2m supports RC4 with MD5 ciphers [2m[reject rc4-md5.badtls.io:11009][0m
[0m[2m SKIP[0m[2m valid localhost certificate [2m[accept localhost:37048][0m
[0m[2m SKIP[0m[2m invalid localhost certificate [2m[reject localhost:40361][0m
[0m[2m SKIP[0m[2m use only the given CA bundle, not system's [2m[reject sha256.badssl.com:443][0m
[0m[0m```

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
[1mplatform:[0m Linux (debian 8.5)[0m
[0m[1mrunner:[0m trytls 0.3.2 (CPython 2.7.9, OpenSSL 1.0.1t)[0m
[0m[1mstub:[0m php php-file-get-contents/run.php[0m
[0m[32m PASS[0m protect against Apple's TLS vulnerability CVE-2014-1266 [2m[reject www.ssllabs.com:10443][0m
[0m[32m PASS[0m protect against the FREAK attack [2m[reject www.ssllabs.com:10444][0m
[0m[32m PASS[0m protect against the Logjam attack [2m[reject www.ssllabs.com:10445][0m
[0m[32m PASS[0m protect against FREAK attack (test server 1) [2m[reject cve.freakattack.com:443][0m
[0m[32m PASS[0m protect against FREAK attack (test server 2) [2m[reject cve2.freakattack.com:443][0m
[0m[31m FAIL[0m[31m protection against POODLE attack [2m[accept sslv3.dshield.org:443][0m
[0m[32m PASS[0m support for TLS server name indication (SNI) [2m[accept badssl.com:443][0m
[0m[32m PASS[0m self-signed certificate [2m[reject self-signed.badssl.com:443][0m
[0m[32m PASS[0m expired certificate [2m[reject expired.badssl.com:443][0m
[0m[32m PASS[0m wrong hostname in certificate [2m[reject wrong.host.badssl.com:443][0m
[0m[32m PASS[0m SHA-256 signature [2m[accept sha256.badssl.com:443][0m
[0m[32m PASS[0m 1000 subjectAltNames [2m[accept 1000-sans.badssl.com:443][0m
[0m[32m PASS[0m incomplete chain of trust [2m[reject incomplete-chain.badssl.com:443][0m
[0m[32m PASS[0m Superfish CA [2m[reject superfish.badssl.com:443][0m
[0m[32m PASS[0m eDellRoot CA [2m[reject edellroot.badssl.com:443][0m
[0m[32m PASS[0m DSDTestProvider CA [2m[reject dsdtestprovider.badssl.com:443][0m
[0m[32m PASS[0m support for TLS server name indication (SNI) [2m[accept tlsfun.de:443][0m
[0m[32m PASS[0m self-signed certificate [2m[reject expired.tlsfun.de:443][0m
[0m[32m PASS[0m eDellRoot CA #2 [2m[reject badcert-edell.tlsfun.de:443][0m
[0m[2m SKIP[0m[2m valid certificate Common Name [2m[accept domain-match.badtls.io:10000][0m
[0m[2m SKIP[0m[2m valid wildcard certificate Common Name [2m[accept wildcard-match.badtls.io:10001][0m
[0m[2m SKIP[0m[2m support for Subject Alternative Name (SAN) [2m[accept san-match.badtls.io:10002][0m
[0m[2m SKIP[0m[2m TLS handshake with 1024 bit Diffie-Hellman (DH) [2m[accept dh1024.badtls.io:10005][0m
[0m[2m SKIP[0m[2m certificate expired in year 1963 [2m[reject expired-1963.badtls.io:11000][0m
[0m[2m SKIP[0m[2m certificate validity starts in future [2m[reject future.badtls.io:11001][0m
[0m[2m SKIP[0m[2m mismatch in certificate's Common Name [2m[reject domain-mismatch.badtls.io:11002][0m
[0m[2m SKIP[0m[2m Subject Alternative Name (SAN) mismatch [2m[reject san-mismatch.badtls.io:11003][0m
[0m[2m SKIP[0m[2m MD5 signature algorithm [2m[reject weak-sig.badtls.io:11004][0m
[0m[2m SKIP[0m[2m certificate has invalid key usage for HTTPS connection [2m[reject bad-key-usage.badtls.io:11005][0m
[0m[2m SKIP[0m[2m expired certificate [2m[reject expired.badtls.io:11006][0m
[0m[2m SKIP[0m[2m invalid wildcard certificate Common Name [2m[reject wildcard.mismatch.badtls.io:11007][0m
[0m[2m SKIP[0m[2m supports RC4 ciphers [2m[reject rc4.badtls.io:11008][0m
[0m[2m SKIP[0m[2m supports RC4 with MD5 ciphers [2m[reject rc4-md5.badtls.io:11009][0m
[0m[2m SKIP[0m[2m valid localhost certificate [2m[accept localhost:37660][0m
[0m[2m SKIP[0m[2m invalid localhost certificate [2m[reject localhost:41637][0m
[0m[2m SKIP[0m[2m use only the given CA bundle, not system's [2m[reject sha256.badssl.com:443][0m
[0m[0m```

<!-- markdownlint-enable MD013 -->
