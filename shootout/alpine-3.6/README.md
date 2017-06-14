# TryTLS testing with Alpine

We chose Alpine 3.6 release for this TryTLS-shootout
based on the [Alpine Releases](https://wiki.alpinelinux.org/wiki/Alpine_Linux:Releases).

```console
docker run -ti --rm alpine-3.6
```

```console
# cat /etc/os-release
NAME="Alpine Linux"
ID=alpine
VERSION_ID=3.6.0
PRETTY_NAME="Alpine Linux v3.6"
HOME_URL="http://alpinelinux.org"
BUG_REPORT_URL="http://bugs.alpinelinux.org"
```

<!-- markdownlint-disable MD013 -->

python2-requests | python2-urllib2 | python3-urllib | go-nethttp | java-https | java-net | php-file-get-contents
---------------- | --------------- | -------------- | ---------- | ---------- | -------- | ---------------------
?                | ?               | ?              | ?          | ?          | ?        | ?

## python2-requests

```console
# python --version
Python 2.7.13
```

```console
# trytls https python python2-requests/run.py
platform: Linux
runner: trytls 0.3.7 (CPython 2.7.13)
stub: python python2-requests/run.py
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
 PASS expired certificate [reject expired.badssl.com:443]
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
 PASS SHA-256 signature algorithm [accept sha256.badssl.com:443]
 PASS certificate with 1000 different Subject Alternative Names [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 PASS Superfish CA [reject superfish.badssl.com:443]
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
 PASS untrusted root certificate [reject untrusted-root.badssl.com:443]
 PASS denies use of RC4 ciphers (RFC 7465) [reject rc4.badssl.com:443]
 PASS denies use of RC4 with MD5 ciphers [reject rc4-md5.badssl.com:443]
 PASS denies use of null cipher [reject null.badssl.com:443]
 PASS denies use of 480 bit Diffie-Hellman (DH) [reject dh480.badssl.com:443]
 PASS denies use of 512 bit Diffie-Hellman (DH) [reject dh512.badssl.com:443]
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
 PASS denies use of RC4 ciphers (RFC 7465) [reject rc4.badtls.io:11008]
 FAIL denies use of MD5 signature algorithm (RFC 6151) [reject weak-sig.badtls.io:11004]
 PASS denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
 PASS valid localhost certificate [accept localhost:<temp port>]
 PASS invalid localhost certificate [reject localhost:<temp port>]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## python2-urllib2

```console
# python --version
Python 2.7.13
```

```console
# trytls https python python2-urllib2/run.py
platform: Linux
runner: trytls 0.3.7 (CPython 2.7.13)
stub: python python2-urllib2/run.py
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
 PASS expired certificate [reject expired.badssl.com:443]
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
 PASS SHA-256 signature algorithm [accept sha256.badssl.com:443]
 PASS certificate with 1000 different Subject Alternative Names [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 PASS Superfish CA [reject superfish.badssl.com:443]
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
 PASS untrusted root certificate [reject untrusted-root.badssl.com:443]
 PASS denies use of RC4 ciphers (RFC 7465) [reject rc4.badssl.com:443]
 PASS denies use of RC4 with MD5 ciphers [reject rc4-md5.badssl.com:443]
 PASS denies use of null cipher [reject null.badssl.com:443]
 PASS denies use of 480 bit Diffie-Hellman (DH) [reject dh480.badssl.com:443]
 PASS denies use of 512 bit Diffie-Hellman (DH) [reject dh512.badssl.com:443]
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
 PASS denies use of RC4 ciphers (RFC 7465) [reject rc4.badtls.io:11008]
 FAIL denies use of MD5 signature algorithm (RFC 6151) [reject weak-sig.badtls.io:11004]
 PASS denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
 PASS valid localhost certificate [accept localhost:<temp port>]
 PASS invalid localhost certificate [reject localhost:<temp port>]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## python3-urllib

```console
# python3 --version
Python 3.6.1
```

```console
# trytls https python3 python3-urllib/run.py
platform: Linux
runner: trytls 0.3.7 (CPython 2.7.13)
stub: python3 python3-urllib/run.py
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
 PASS expired certificate [reject expired.badssl.com:443]
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
 PASS SHA-256 signature algorithm [accept sha256.badssl.com:443]
 PASS certificate with 1000 different Subject Alternative Names [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 PASS Superfish CA [reject superfish.badssl.com:443]
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
 PASS untrusted root certificate [reject untrusted-root.badssl.com:443]
 PASS denies use of RC4 ciphers (RFC 7465) [reject rc4.badssl.com:443]
 PASS denies use of RC4 with MD5 ciphers [reject rc4-md5.badssl.com:443]
 PASS denies use of null cipher [reject null.badssl.com:443]
 PASS denies use of 480 bit Diffie-Hellman (DH) [reject dh480.badssl.com:443]
 PASS denies use of 512 bit Diffie-Hellman (DH) [reject dh512.badssl.com:443]
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
 PASS denies use of RC4 ciphers (RFC 7465) [reject rc4.badtls.io:11008]
 FAIL denies use of MD5 signature algorithm (RFC 6151) [reject weak-sig.badtls.io:11004]
 PASS denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
 PASS valid localhost certificate [accept localhost:<temp port>]
 PASS invalid localhost certificate [reject localhost:<temp port>]
 PASS use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## go-nethttp

```console
# go version
go version go1.8.1 linux/amd64
```

```console
# trytls https go-nethttp/run
platform: Linux
runner: trytls 0.3.7 (CPython 2.7.13)
stub: go-nethttp/run
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
      output: Get https://www.ssllabs.com:10443: crypto/rsa: verification error
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
      output: Get https://www.ssllabs.com:10444: tls: unexpected ServerKeyExchange
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
      output: Get https://www.ssllabs.com:10445: remote error: tls: handshake failure
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
      output: Get https://self-signed.badssl.com:443: x509: certificate signed by unknown authority
 PASS expired certificate [reject expired.badssl.com:443]
      output: Get https://expired.badssl.com:443: x509: certificate has expired or is not yet valid
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
      output: Get https://wrong.host.badssl.com:443: x509: certificate is valid for *.badssl.com, badssl.com, not wrong.host.badssl.com
 PASS SHA-256 signature algorithm [accept sha256.badssl.com:443]
 PASS certificate with 1000 different Subject Alternative Names [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
      output: Get https://incomplete-chain.badssl.com:443: x509: certificate signed by unknown authority
 PASS Superfish CA [reject superfish.badssl.com:443]
      output: Get https://superfish.badssl.com:443: x509: certificate signed by unknown authority
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
      output: Get https://edellroot.badssl.com:443: x509: certificate signed by unknown authority
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
      output: Get https://dsdtestprovider.badssl.com:443: x509: certificate signed by unknown authority
 PASS untrusted root certificate [reject untrusted-root.badssl.com:443]
      output: Get https://untrusted-root.badssl.com:443: x509: certificate signed by unknown authority
 PASS denies use of RC4 ciphers (RFC 7465) [reject rc4.badssl.com:443]
      output: Get https://rc4.badssl.com:443: remote error: tls: handshake failure
 PASS denies use of RC4 with MD5 ciphers [reject rc4-md5.badssl.com:443]
      output: Get https://rc4-md5.badssl.com:443: remote error: tls: handshake failure
 PASS denies use of null cipher [reject null.badssl.com:443]
      output: Get https://null.badssl.com:443: remote error: tls: handshake failure
 PASS denies use of 480 bit Diffie-Hellman (DH) [reject dh480.badssl.com:443]
      output: Get https://dh480.badssl.com:443: remote error: tls: handshake failure
 PASS denies use of 512 bit Diffie-Hellman (DH) [reject dh512.badssl.com:443]
      output: Get https://dh512.badssl.com:443: remote error: tls: handshake failure
 SKIP valid certificate Common Name [accept domain-match.badtls.io:10000]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP certificate validity starts in future [reject future.badtls.io:11001]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP expired certificate [reject expired.badtls.io:11006]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP denies use of RC4 ciphers (RFC 7465) [reject rc4.badtls.io:11008]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP denies use of MD5 signature algorithm (RFC 6151) [reject weak-sig.badtls.io:11004]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP valid localhost certificate [accept localhost:<temp port>]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP invalid localhost certificate [reject localhost:<temp port>]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
```

## java-https

```console
# java -version
java version "1.7.0_131"
OpenJDK Runtime Environment (IcedTea 2.6.9) (Alpine 7.131.2.6.9-r1)
OpenJDK 64-Bit Server VM (build 24.131-b00, mixed mode)
```

```console
# trytls https java -classpath java-https Run
platform: Linux
runner: trytls 0.3.7 (CPython 2.7.13)
stub: java -classpath java-https Run
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
 PASS expired certificate [reject expired.badssl.com:443]
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
 PASS SHA-256 signature algorithm [accept sha256.badssl.com:443]
 PASS certificate with 1000 different Subject Alternative Names [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 PASS Superfish CA [reject superfish.badssl.com:443]
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
 PASS untrusted root certificate [reject untrusted-root.badssl.com:443]
 PASS denies use of RC4 ciphers (RFC 7465) [reject rc4.badssl.com:443]
 PASS denies use of RC4 with MD5 ciphers [reject rc4-md5.badssl.com:443]
 PASS denies use of null cipher [reject null.badssl.com:443]
 PASS denies use of 480 bit Diffie-Hellman (DH) [reject dh480.badssl.com:443]
 PASS denies use of 512 bit Diffie-Hellman (DH) [reject dh512.badssl.com:443]
 SKIP valid certificate Common Name [accept domain-match.badtls.io:10000]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP certificate validity starts in future [reject future.badtls.io:11001]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP expired certificate [reject expired.badtls.io:11006]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP denies use of RC4 ciphers (RFC 7465) [reject rc4.badtls.io:11008]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP denies use of MD5 signature algorithm (RFC 6151) [reject weak-sig.badtls.io:11004]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP valid localhost certificate [accept localhost:<temp port>]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP invalid localhost certificate [reject localhost:<temp port>]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
```

## java-net

```console
# java -version
java version "1.7.0_131"
OpenJDK Runtime Environment (IcedTea 2.6.9) (Alpine 7.131.2.6.9-r1)
OpenJDK 64-Bit Server VM (build 24.131-b00, mixed mode)
```

```console
# trytls https java -classpath java-net Run
platform: Linux
runner: trytls 0.3.7 (CPython 2.7.13)
stub: java -classpath java-net Run
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
 PASS expired certificate [reject expired.badssl.com:443]
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
 PASS SHA-256 signature algorithm [accept sha256.badssl.com:443]
 PASS certificate with 1000 different Subject Alternative Names [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 PASS Superfish CA [reject superfish.badssl.com:443]
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
 PASS untrusted root certificate [reject untrusted-root.badssl.com:443]
 PASS denies use of RC4 ciphers (RFC 7465) [reject rc4.badssl.com:443]
 PASS denies use of RC4 with MD5 ciphers [reject rc4-md5.badssl.com:443]
 PASS denies use of null cipher [reject null.badssl.com:443]
 PASS denies use of 480 bit Diffie-Hellman (DH) [reject dh480.badssl.com:443]
 PASS denies use of 512 bit Diffie-Hellman (DH) [reject dh512.badssl.com:443]
 SKIP valid certificate Common Name [accept domain-match.badtls.io:10000]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP certificate validity starts in future [reject future.badtls.io:11001]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP expired certificate [reject expired.badtls.io:11006]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP denies use of RC4 ciphers (RFC 7465) [reject rc4.badtls.io:11008]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP denies use of MD5 signature algorithm (RFC 6151) [reject weak-sig.badtls.io:11004]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP valid localhost certificate [accept localhost:<temp port>]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP invalid localhost certificate [reject localhost:<temp port>]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
```

## php-file-get-contents

```console
# php5 --version
PHP 5.6.30 (cli) (built: Jun  1 2017 09:28:04)
Copyright (c) 1997-2016 The PHP Group
Zend Engine v2.6.0, Copyright (c) 1998-2016 Zend Technologies
```

```console
# trytls https php5 php-file-get-contents/run.php
platform: Linux
runner: trytls 0.3.7 (CPython 2.7.13)
stub: php5 php-file-get-contents/run.php
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 FAIL support for TLS server name indication (SNI) [accept badssl.com:443]
 SKIP self-signed certificate [reject self-signed.badssl.com:443]
      reason: could not detect SNI support
 SKIP expired certificate [reject expired.badssl.com:443]
      reason: could not detect SNI support
 SKIP wrong hostname in certificate [reject wrong.host.badssl.com:443]
      reason: could not detect SNI support
 SKIP SHA-256 signature algorithm [accept sha256.badssl.com:443]
      reason: could not detect SNI support
 SKIP certificate with 1000 different Subject Alternative Names [accept 1000-sans.badssl.com:443]
      reason: could not detect SNI support
 SKIP incomplete chain of trust [reject incomplete-chain.badssl.com:443]
      reason: could not detect SNI support
 SKIP Superfish CA [reject superfish.badssl.com:443]
      reason: could not detect SNI support
 SKIP eDellRoot CA [reject edellroot.badssl.com:443]
      reason: could not detect SNI support
 SKIP DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
      reason: could not detect SNI support
 SKIP untrusted root certificate [reject untrusted-root.badssl.com:443]
      reason: could not detect SNI support
 SKIP denies use of RC4 ciphers (RFC 7465) [reject rc4.badssl.com:443]
      reason: could not detect SNI support
 SKIP denies use of RC4 with MD5 ciphers [reject rc4-md5.badssl.com:443]
      reason: could not detect SNI support
 SKIP denies use of null cipher [reject null.badssl.com:443]
      reason: could not detect SNI support
 SKIP denies use of 480 bit Diffie-Hellman (DH) [reject dh480.badssl.com:443]
      reason: could not detect SNI support
 SKIP denies use of 512 bit Diffie-Hellman (DH) [reject dh512.badssl.com:443]
      reason: could not detect SNI support
 SKIP valid certificate Common Name [accept domain-match.badtls.io:10000]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP valid wildcard certificate Common Name [accept wildcard-match.badtls.io:10001]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP support for Subject Alternative Name (SAN) [accept san-match.badtls.io:10002]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP TLS handshake with 1024 bit Diffie-Hellman (DH) [accept dh1024.badtls.io:10005]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP certificate expired in year 1963 [reject expired-1963.badtls.io:11000]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP certificate validity starts in future [reject future.badtls.io:11001]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP mismatch in certificate's Common Name [reject domain-mismatch.badtls.io:11002]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP Subject Alternative Name (SAN) mismatch [reject san-mismatch.badtls.io:11003]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP certificate has invalid key usage for HTTPS connection [reject bad-key-usage.badtls.io:11005]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP expired certificate [reject expired.badtls.io:11006]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP invalid wildcard certificate Common Name [reject wildcard.mismatch.badtls.io:11007]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP denies use of RC4 ciphers (RFC 7465) [reject rc4.badtls.io:11008]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP denies use of MD5 signature algorithm (RFC 6151) [reject weak-sig.badtls.io:11004]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP denies use of RC4 with MD5 ciphers [reject rc4-md5.badtls.io:11009]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP valid localhost certificate [accept localhost:<temp port>]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP invalid localhost certificate [reject localhost:<temp port>]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
      reason: the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)
```

<!-- markdownlint-enable MD013 -->
