# How to run

```console
./run.php expired.badssl.com 443
```

# Dependencies

  * ​PHP (version >= 4.3.0) [compiled with OpenSSL support]

# Building Dockerfile

```console
docker build -t php-file-get-contents .
```

# Running in Docker

```console
$ docker run -ti --rm php-file-get-contents
platform: Linux (debian 8.5)
runner: trytls 0.0.8 (CPython 2.7.9, OpenSSL 1.0.1t)
stub: php 'run.php'
 PASS expired certificate [reject expired.badssl.com:443]
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 PASS Superfish CA [reject superfish.badssl.com:443]
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
 PASS protect against an OS X vulnerability [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 SKIP valid localhost certificate [accept localhost:46041]
 SKIP invalid localhost certificate [reject localhost:45752]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```
