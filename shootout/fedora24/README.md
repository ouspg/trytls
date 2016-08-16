# TryTLS testing with Fedora latest

```console
docker run -ti --rm fedora24
```

```console
# cat /etc/redhat-release
Fedora release 24 (Twenty Four)
```

<!-- markdownlint-disable MD013 -->

python2-requests | python2-urllib2 | python3-urllib | go-nethttp | java-https | java-net | php-file-get-contents
---------------- | --------------- | -------------- | ---------- | ---------- | -------- | ---------------------
PASS             | PASS            | PASS           | ERROR      | PASS       | PASS     | PASS

## python2-requests

```console
# python --version
Python 2.7.12
```

```console
# trytls https python python2-requests/run.py
platform: Linux (Fedora 24)
runner: trytls 0.3.0 (CPython 2.7.12, OpenSSL 1.0.2h-fips)
stub: python python2-requests/run.py
 PASS valid certificate Common Name [accept domain-match.badtls.io:10000]
      output: /usr/lib/python2.7/site-packages/requests/packages/urllib3/connection.py:303: SubjectAltNameWarning: Certificate for domain-match.badtls.io has no `subjectAltName`, falling back to check for a `commonName` for now. This feature is being removed by major browsers and deprecated by RFC 2818. (See https://github.com/shazow/urllib3/issues/497 for details.)  SubjectAltNameWarning
 PASS valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
      output: /usr/lib/python2.7/site-packages/requests/packages/urllib3/connection.py:303: SubjectAltNameWarning: Certificate for wildcard-match.badtls.io has no `subjectAltName`, falling back to check for a `commonName` for now. This feature is being removed by major browsers and deprecated by RFC 2818. (See https://github.com/shazow/urllib3/issues/497 for details.)  SubjectAltNameWarning
 PASS support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
 PASS TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
      output: /usr/lib/python2.7/site-packages/requests/packages/urllib3/connection.py:303: SubjectAltNameWarning: Certificate for dh1024.badtls.io has no `subjectAltName`, falling back to check for a `commonName` for now. This feature is being removed by major browsers and deprecated by RFC 2818. (See https://github.com/shazow/urllib3/issues/497 for details.)  SubjectAltNameWarning
 PASS certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
 PASS certificate validity starts in future [reject future.badtls.io:11001]
 PASS mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
      output: /usr/lib/python2.7/site-packages/requests/packages/urllib3/connection.py:303: SubjectAltNameWarning: Certificate for domain-mismatch.badtls.io has no `subjectAltName`, falling back to check for a `commonName` for now. This feature is being removed by major browsers and deprecated by RFC 2818. (See https://github.com/shazow/urllib3/issues/497 for details.)  SubjectAltNameWarning
 PASS Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
 PASS MD5 signature algorithm [reject weak-sig.badtls.io:11004]
 PASS certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
 PASS expired certificate [reject expired.badtls.io:11006]
 PASS invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
      output: /usr/lib/python2.7/site-packages/requests/packages/urllib3/connection.py:303: SubjectAltNameWarning: Certificate for wildcard.mismatch.badtls.io has no `subjectAltName`, falling back to check for a `commonName` for now. This feature is being removed by major browsers and deprecated by RFC 2818. (See https://github.com/shazow/urllib3/issues/497 for details.)  SubjectAltNameWarning
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
 PASS valid localhost certificate [accept localhost:45667]
      output: /usr/lib/python2.7/site-packages/requests/packages/urllib3/connection.py:303: SubjectAltNameWarning: Certificate for localhost has no `subjectAltName`, falling back to check for a `commonName` for now. This feature is being removed by major browsers and deprecated by RFC 2818. (See https://github.com/shazow/urllib3/issues/497 for details.)  SubjectAltNameWarning
 PASS invalid localhost certificate [reject localhost:46159]
      output: /usr/lib/python2.7/site-packages/requests/packages/urllib3/connection.py:303: SubjectAltNameWarning: Certificate for localhost has no `subjectAltName`, falling back to check for a `commonName` for now. This feature is being removed by major browsers and deprecated by RFC 2818. (See https://github.com/shazow/urllib3/issues/497 for details.)  SubjectAltNameWarning
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## python2-urllib2

```console
# python --version
Python 2.7.12
```

```console
# trytls https python python2-urllib2/run.py
platform: Linux (Fedora 24)
runner: trytls 0.3.0 (CPython 2.7.12, OpenSSL 1.0.2h-fips)
stub: python python2-urllib2/run.py
 PASS valid certificate Common Name [accept domain-match.badtls.io:10000]
 PASS valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
 PASS support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
 PASS TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
 PASS certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
 PASS certificate validity starts in future [reject future.badtls.io:11001]
 PASS mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
 PASS Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
 PASS MD5 signature algorithm [reject weak-sig.badtls.io:11004]
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
 PASS valid localhost certificate [accept localhost:36576]
 PASS invalid localhost certificate [reject localhost:42532]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## python3-urllib

```console
# python3 --version
Python 3.5.1
```

```console
# trytls https python3 python3-urllib/run.py
platform: Linux (Fedora 24)
runner: trytls 0.3.0 (CPython 2.7.12, OpenSSL 1.0.2h-fips)
stub: python3 python3-urllib/run.py
 PASS valid certificate Common Name [accept domain-match.badtls.io:10000]
 PASS valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
 PASS support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
 PASS TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
 PASS certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
 PASS certificate validity starts in future [reject future.badtls.io:11001]
 PASS mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
 PASS Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
 PASS MD5 signature algorithm [reject weak-sig.badtls.io:11004]
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
 PASS valid localhost certificate [accept localhost:46772]
 PASS invalid localhost certificate [reject localhost:46715]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## go-nethttp

```console
# go version
go version go1.6.3 linux/amd64
```

```console
# trytls https go-nethttp/run
platform: Linux (Fedora 24)
runner: trytls 0.3.0 (CPython 2.7.12, OpenSSL 1.0.2h-fips)
stub: go-nethttp/run
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
ERROR protection against POODLE attack [reject sslv3.dshield.org:443]
      reason: stub exited with return code 1
      output: Get https://sslv3.dshield.org:443: tls: server selected unsupported protocol version 300
 PASS eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
 SKIP valid localhost certificate [accept localhost:43305]
 SKIP invalid localhost certificate [reject localhost:43601]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## java-https

```console
# java -version
openjdk version "1.8.0_101"
OpenJDK Runtime Environment (build 1.8.0_101-b14)
OpenJDK 64-Bit Server VM (build 25.101-b14, mixed mode)
```

```console
# trytls https java -classpath java-https Run
platform: Linux (Fedora 24)
runner: trytls 0.3.0 (CPython 2.7.12, OpenSSL 1.0.2h-fips)
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
      output: javax.net.ssl.SSLKeyException: Invalid signature on ECDH server key exchange message
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
      output: javax.net.ssl.SSLProtocolException: Protocol violation: server sent a server key exchange message for key exchange RSA
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
      output: javax.net.ssl.SSLHandshakeException: DHPublicKey does not comply to algorithm constraints
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
      output: javax.net.ssl.SSLProtocolException: Protocol violation: server sent a server key exchange message for key exchange RSA
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
      output: javax.net.ssl.SSLProtocolException: Protocol violation: server sent a server key exchange message for key exchange RSA
 PASS protection against POODLE attack [reject sslv3.dshield.org:443]
      output: javax.net.ssl.SSLHandshakeException: Server chose SSLv3, but that protocol version is not enabled or not supported by the client.
 PASS eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
      output: javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target
 SKIP valid localhost certificate [accept localhost:37482]
 SKIP invalid localhost certificate [reject localhost:42140]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## java-net

```console
# java -version
openjdk version "1.8.0_101"
OpenJDK Runtime Environment (build 1.8.0_101-b14)
OpenJDK 64-Bit Server VM (build 25.101-b14, mixed mode)
```

```console
# trytls https java -classpath java-net Run
platform: Linux (Fedora 24)
runner: trytls 0.3.0 (CPython 2.7.12, OpenSSL 1.0.2h-fips)
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
      output: javax.net.ssl.SSLKeyException: Invalid signature on ECDH server key exchange message
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
      output: javax.net.ssl.SSLProtocolException: Protocol violation: server sent a server key exchange message for key exchange RSA
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
      output: javax.net.ssl.SSLHandshakeException: DHPublicKey does not comply to algorithm constraints
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
      output: javax.net.ssl.SSLProtocolException: Protocol violation: server sent a server key exchange message for key exchange RSA
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
      output: javax.net.ssl.SSLProtocolException: Protocol violation: server sent a server key exchange message for key exchange RSA
 PASS protection against POODLE attack [reject sslv3.dshield.org:443]
      output: javax.net.ssl.SSLHandshakeException: Server chose SSLv3, but that protocol version is not enabled or not supported by the client.
 PASS eDellRoot CA #2 [reject badcert-edell.tlsfun.de:443]
      output: javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target
 SKIP valid localhost certificate [accept localhost:42313]
 SKIP invalid localhost certificate [reject localhost:35036]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## php-file-get-contents

```console
# php --version
PHP 5.6.24 (cli) (built: Jul 21 2016 05:04:03)
Copyright (c) 1997-2016 The PHP Group
Zend Engine v2.6.0, Copyright (c) 1998-2016 Zend Technologies
```

```console
# trytls https php php-file-get-contents/run.php
platform: Linux (Fedora 24)
runner: trytls 0.3.0 (CPython 2.7.12, OpenSSL 1.0.2h-fips)
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
 SKIP valid localhost certificate [accept localhost:33830]
 SKIP invalid localhost certificate [reject localhost:45954]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

<!-- markdownlint-enable MD013 -->
