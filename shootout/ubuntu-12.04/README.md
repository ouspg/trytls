# TryTLS testing with Ubuntu

We chose Ubuntu 12.04, 14.04 and 16.04 LTS releases for this TryTLS-shootout
based on the [Ubuntu release end of life](http://www.ubuntu.com/info/release-end-of-life).

```console
$ docker run -ti --rm ubuntu-12.04

# grep DISTRIB_DESCRIPTION /etc/lsb-release
DISTRIB_DESCRIPTION="Ubuntu 12.04.5 LTS"
```

<!-- markdownlint-disable MD013 -->

OS                 | python-requests | python-urllib2 | python3-urllib | go-nethttp | java-https | java-net | php-file-get-contents
------------------ | --------------- | -------------- | -------------- | ---------- | ---------- | -------- | ---------------------
Ubuntu 12.04.5 LTS | ERROR           | ERROR          | FAIL           | NO SNI     | N/A        | N/A      | NO SNI

## python-requests

```console
# python --version
Python 2.7.3

$ trytls https docker run -i --rm ubuntu-12.04 python /root/stubs/python-requests/run.py
platform: OS X 10.10.5
runner: trytls 0.2.1 (CPython 2.7.10, OpenSSL 0.9.8zg)
stub: docker run '-i' '--rm' 'ubuntu-12.04' python '/root/stubs/python-requests/run.py'
ERROR support for TLS server name indication (SNI) [accept badssl.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python-requests/run.py", line 13, in <module>
                  except requests.exceptions.SSLError as err:
              AttributeError: 'module' object has no attribute 'SSLError'
...
```

## python-urllib2

```console
# python --version
Python 2.7.3

# trytls https docker run -i --rm ubuntu-12.04 python /root/stubs/python-urllib2/run.py
platform: OS X 10.10.5
runner: trytls 0.2.1 (CPython 2.7.10, OpenSSL 0.9.8zg)
stub: docker run '-i' '--rm' 'ubuntu-12.04' python '/root/stubs/python-urllib2/run.py'
ERROR support for TLS server name indication (SNI) [accept badssl.com:443]
      reason: stub exited with return code 1
      output: Traceback (most recent call last):
                File "/root/stubs/python-urllib2/run.py", line 14, in <module>
                  except ssl.CertificateError:
              AttributeError: 'module' object has no attribute 'CertificateError
```

## python3-urllib

```console
# python3 --version
Python 3.2.3

# trytls https docker run -i --rm ubuntu-12.04 python3 /root/stubs/python3-urllib/run.py
platform: OS X 10.10.5
runner: trytls 0.2.1 (CPython 2.7.10, OpenSSL 0.9.8zg)
stub: docker run '-i' '--rm' 'ubuntu-12.04' python3 '/root/stubs/python3-urllib/run.py'
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 FAIL expired certificate [reject expired.badssl.com:443]
 FAIL wrong hostname in certificate [reject wrong.host.badssl.com:443]
 FAIL self-signed certificate [reject self-signed.badssl.com:443]
 PASS SHA-256 signature [accept sha256.badssl.com:443]
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
 FAIL incomplete chain of trust [reject incomplete-chain.badssl.com:443]
 FAIL Superfish CA [reject superfish.badssl.com:443]
 FAIL eDellRoot CA [reject edellroot.badssl.com:443]
 FAIL DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
 PASS protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
 PASS protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
 PASS protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
[SKIPPED localhost backend - not compatible with docker run in ca passing]
```

## go-nethttp

```console
# go version
go version go1

# trytls https docker run -i --rm ubuntu-12.04 /root/stubs/go-nethttp/run
docker run -i --rm ubuntu-12.04 /root/stubs/go-nethttp/run | expand
platform: OS X 10.10.5
runner: trytls 0.2.1 (CPython 2.7.10, OpenSSL 0.9.8zg)
stub: docker run '-i' '--rm' 'ubuntu-12.04' '/root/stubs/go-nethttp/run'
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
ERROR protect against Apple's TLS vulnerability CVE-2014-1266 [reject www.ssllabs.com:10443]
      reason: stub exited with return code 1
      output: Get https://www.ssllabs.com:10443: remote error: protocol version not supported
ERROR protect against the FREAK attack [reject www.ssllabs.com:10444]
      reason: stub exited with return code 2
      output: panic: crypto: requested hash function is unavailable

              goroutine 1 [running]:
              crypto.Hash.New(0x3800000005, 0x404b9c, 0x7fe073806caf, 0x10)
                /usr/lib/go/src/pkg/crypto/crypto.go:62 +0x95
              crypto/x509.(*Certificate).CheckSignature(0xf84007d840, 0x7fe000000004, 0xf8400a500e, 0xf3f0000041b, 0xf8400a543d, ...)
                /usr/lib/go/src/pkg/crypto/x509/x509.go:391 +0x68
              crypto/x509.(*Certificate).CheckSignatureFrom(0xf84007d580, 0xf84007d840, 0x0, 0x0, 0xf8400a90e0, ...)
                /usr/lib/go/src/pkg/crypto/x509/x509.go:370 +0x15a
              crypto/x509.(*CertPool).findVerifiedParents(0xf8400a7c00, 0xf84007d580, 0x0, 0x0, 0x60, ...)
                /usr/lib/go/src/pkg/crypto/x509/cert_pool.go:44 +0x17d
              crypto/x509.(*Certificate).buildChains(0xf84007d580, 0xf84025b420, 0x7fe073806f48, 0x100000001, 0x7fe073806f60, ...)
                /usr/lib/go/src/pkg/crypto/x509/verify.go:198 +0x1c0
              crypto/x509.(*Certificate).Verify(0xf84007d580, 0x0, 0x0, 0xf8400a7c00, 0xf8400a7ca0, ...)
                /usr/lib/go/src/pkg/crypto/x509/verify.go:177 +0x1c1
              ----- stack segment boundary -----
              crypto/tls.(*Conn).clientHandshake(0xf840073240, 0x0, 0x0, 0x0)
                /usr/lib/go/src/pkg/crypto/tls/handshake_client.go:117 +0xfab
              crypto/tls.(*Conn).Handshake(0xf840073240, 0x0, 0x0, 0xf840073240)
                /usr/lib/go/src/pkg/crypto/tls/conn.go:808 +0xdc
              net/http.(*Transport).getConn(0xf840053000, 0xf840054810, 0xf840054810, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/transport.go:369 +0x4aa
              net/http.(*Transport).RoundTrip(0xf840053000, 0xf84007b000, 0x1d, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/transport.go:155 +0x2ba
              net/http.send(0xf84007b000, 0xf840054750, 0xf840053000, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/client.go:133 +0x3ca
              net/http.(*Client).doFollowingRedirects(0x6a39a8, 0xf84007b000, 0x0, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/client.go:227 +0x5e2
              net/http.(*Client).Get(0x6a39a8, 0xf840051a60, 0x7fe00000001d, 0xf800000004, 0x0, ...)
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
              syscall.EpollWait(0xf800000006, 0xf840095010, 0xa0000000a, 0xffffffff, 0xc, ...)
                /usr/lib/go/src/pkg/syscall/zerrors_linux_amd64.go:1781 +0xa1
              net.(*pollster).WaitFD(0xf840095000, 0xf840053a00, 0x0, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/fd_linux.go:146 +0x110
              net.(*pollServer).Run(0xf840053a00, 0x0)
                /usr/lib/go/src/pkg/net/fd.go:236 +0xe4
              created by net.newPollServer
                /usr/lib/go/src/pkg/net/newpollserver.go:35 +0x382
 PASS protect against the Logjam attack [reject www.ssllabs.com:10445]
ERROR protect against FREAK attack (test server 1) [reject cve.freakattack.com:443]
      reason: stub exited with return code 2
      output: panic: crypto: requested hash function is unavailable

              goroutine 1 [running]:
              crypto.Hash.New(0x3800000005, 0x404b9c, 0x7fbd3c18ecaf, 0x10)
                /usr/lib/go/src/pkg/crypto/crypto.go:62 +0x95
              crypto/x509.(*Certificate).CheckSignature(0xf84007d840, 0x7fbd00000004, 0xf8400a400e, 0x10e500000447, 0xf8400a4469, ...)
                /usr/lib/go/src/pkg/crypto/x509/x509.go:391 +0x68
              crypto/x509.(*Certificate).CheckSignatureFrom(0xf84007d580, 0xf84007d840, 0x0, 0x0, 0xf8400ad0e8, ...)
                /usr/lib/go/src/pkg/crypto/x509/x509.go:370 +0x15a
              crypto/x509.(*CertPool).findVerifiedParents(0xf8400abd00, 0xf84007d580, 0x0, 0x0, 0x60, ...)
                /usr/lib/go/src/pkg/crypto/x509/cert_pool.go:44 +0x17d
              crypto/x509.(*Certificate).buildChains(0xf84007d580, 0xf840270e00, 0x7fbd3c18ef48, 0x100000001, 0x7fbd3c18ef60, ...)
                /usr/lib/go/src/pkg/crypto/x509/verify.go:198 +0x1c0
              crypto/x509.(*Certificate).Verify(0xf84007d580, 0x0, 0x0, 0xf8400abd00, 0xf8400abda0, ...)
                /usr/lib/go/src/pkg/crypto/x509/verify.go:177 +0x1c1
              ----- stack segment boundary -----
              crypto/tls.(*Conn).clientHandshake(0xf840073240, 0x0, 0x0, 0x0)
                /usr/lib/go/src/pkg/crypto/tls/handshake_client.go:117 +0xfab
              crypto/tls.(*Conn).Handshake(0xf840073240, 0x0, 0x0, 0xf840073240)
                /usr/lib/go/src/pkg/crypto/tls/conn.go:808 +0xdc
              net/http.(*Transport).getConn(0xf840053000, 0xf840054810, 0xf840054810, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/transport.go:369 +0x4aa
              net/http.(*Transport).RoundTrip(0xf840053000, 0xf84007b000, 0x1f, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/transport.go:155 +0x2ba
              net/http.send(0xf84007b000, 0xf840054750, 0xf840053000, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/client.go:133 +0x3ca
              net/http.(*Client).doFollowingRedirects(0x6a39a8, 0xf84007b000, 0x0, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/client.go:227 +0x5e2
              net/http.(*Client).Get(0x6a39a8, 0xf840051a60, 0x7fbd0000001f, 0xf800000004, 0x0, ...)
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
              syscall.EpollWait(0xf800000006, 0xf840095010, 0xa0000000a, 0xffffffff, 0xc, ...)
                /usr/lib/go/src/pkg/syscall/zerrors_linux_amd64.go:1781 +0xa1
              net.(*pollster).WaitFD(0xf840095000, 0xf840053a00, 0x0, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/fd_linux.go:146 +0x110
              net.(*pollServer).Run(0xf840053a00, 0x0)
                /usr/lib/go/src/pkg/net/fd.go:236 +0xe4
              created by net.newPollServer
                /usr/lib/go/src/pkg/net/newpollserver.go:35 +0x382
ERROR protect against FREAK attack (test server 2) [reject cve2.freakattack.com:443]
      reason: stub exited with return code 2
      output: panic: crypto: requested hash function is unavailable

              goroutine 1 [running]:
              crypto.Hash.New(0x3800000005, 0x404b9c, 0x7fa8a61e1caf, 0x10)
                /usr/lib/go/src/pkg/crypto/crypto.go:62 +0x95
              crypto/x509.(*Certificate).CheckSignature(0xf84007d840, 0x7fa800000004, 0xf8400a500e, 0x10e500000447, 0xf8400a5469, ...)
                /usr/lib/go/src/pkg/crypto/x509/x509.go:391 +0x68
              crypto/x509.(*Certificate).CheckSignatureFrom(0xf84007d580, 0xf84007d840, 0x0, 0x0, 0xf8400ae0e8, ...)
                /usr/lib/go/src/pkg/crypto/x509/x509.go:370 +0x15a
              crypto/x509.(*CertPool).findVerifiedParents(0xf8400accc0, 0xf84007d580, 0x0, 0x0, 0x60, ...)
                /usr/lib/go/src/pkg/crypto/x509/cert_pool.go:44 +0x17d
              crypto/x509.(*Certificate).buildChains(0xf84007d580, 0xf84025fdc0, 0x7fa8a61e1f48, 0x100000001, 0x7fa8a61e1f60, ...)
                /usr/lib/go/src/pkg/crypto/x509/verify.go:198 +0x1c0
              crypto/x509.(*Certificate).Verify(0xf84007d580, 0x0, 0x0, 0xf8400accc0, 0xf8400acd60, ...)
                /usr/lib/go/src/pkg/crypto/x509/verify.go:177 +0x1c1
              ----- stack segment boundary -----
              crypto/tls.(*Conn).clientHandshake(0xf840073240, 0x0, 0x0, 0x0)
                /usr/lib/go/src/pkg/crypto/tls/handshake_client.go:117 +0xfab
              crypto/tls.(*Conn).Handshake(0xf840073240, 0x0, 0x0, 0xf840073240)
                /usr/lib/go/src/pkg/crypto/tls/conn.go:808 +0xdc
              net/http.(*Transport).getConn(0xf840053000, 0xf840054d80, 0xf840054d80, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/transport.go:369 +0x4aa
              net/http.(*Transport).RoundTrip(0xf840053000, 0xf84007b000, 0x20, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/transport.go:155 +0x2ba
              net/http.send(0xf84007b000, 0xf840054750, 0xf840053000, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/client.go:133 +0x3ca
              net/http.(*Client).doFollowingRedirects(0x6a39a8, 0xf84007b000, 0x0, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/http/client.go:227 +0x5e2
              net/http.(*Client).Get(0x6a39a8, 0xf8400547b0, 0x7fa800000020, 0xf800000004, 0x0, ...)
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
              syscall.EpollWait(0xf800000006, 0xf840095010, 0xa0000000a, 0xffffffff, 0xc, ...)
                /usr/lib/go/src/pkg/syscall/zerrors_linux_amd64.go:1781 +0xa1
              net.(*pollster).WaitFD(0xf840095000, 0xf840053a00, 0x0, 0x0, 0x0, ...)
                /usr/lib/go/src/pkg/net/fd_linux.go:146 +0x110
              net.(*pollServer).Run(0xf840053a00, 0x0)
                /usr/lib/go/src/pkg/net/fd.go:236 +0xe4
              created by net.newPollServer
                /usr/lib/go/src/pkg/net/newpollserver.go:35 +0x382
 SKIP valid localhost certificate [accept localhost:50940]
 SKIP invalid localhost certificate [reject localhost:50947]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

## java-https

Java too old to compile this stub in Ubuntu 12.04 LTS.

## java-net

Java too old to compile this stub in Ubuntu 12.04 LTS.

## php-file-get-contents

```console
# php --version
PHP 5.3.10-1ubuntu3.24 with Suhosin-Patch (cli) (built: Aug  1 2016 20:32:15)
Copyright (c) 1997-2012 The PHP Group
Zend Engine v2.3.0, Copyright (c) 1998-2012 Zend Technologies

# trytls https docker run -i --rm ubuntu-12.04 php /root/stubs/php-file-get-contents/run.php
platform: OS X 10.10.5
runner: trytls 0.2.1 (CPython 2.7.10, OpenSSL 0.9.8zg)
stub: docker run '-i' '--rm' 'ubuntu-12.04' php '/root/stubs/php-file-get-contents/run.php'
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
 SKIP valid localhost certificate [accept localhost:51071]
 SKIP invalid localhost certificate [reject localhost:51078]
 SKIP use only the given CA bundle, not system's [reject sha256.badssl.com:443]
```

<!-- markdownlint-enable MD013 -->
