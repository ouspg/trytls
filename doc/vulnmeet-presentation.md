# TryTLS [![CircleCI](https://circleci.com/gh/ouspg/trytls.svg?style=shield)](https://circleci.com/gh/ouspg/trytls) [![Build status](https://ci.appveyor.com/api/projects/status/91p39fn87pbiy1gs?svg=true)](https://ci.appveyor.com/project/jviide/trytls)

Does *your* TLS/SSL library check certificates properly?
Broken certificate checks seems to be an overlooked issue.
Handling certificates is surprisingly complex, and calls for extra attention.

TryTLS is a tool for the software and library developers, vulnerability
researchers, and end-users, who want to use TLS safely.

We hope to help you to test certificate handling easily. We support
systematic and readily planned tests and try make integrating your
favorite language and library easy.

We are completely open source, feel free to contribute!

----

## What TryTLS Is Not

* We do not address possible client certificate check problems in server code
* We do not do or require a man-in-the-middle tools
* We do not support smart TVs, IoT toasters and other such devices that
  can't run any of the runners

----

## How Does It Work

![Architecture](https://raw.githubusercontent.com/ouspg/trytls/master/doc/concept-pic.png)

* **Backends (servers)** provide TLS/SSL tests for stubs (clients).
* **Stubs** attempt to establish secure TLS/SSL connections to backends.
* **Runners** run the stubs against backends and provide the results of the tests.

----

## Runners

* trytls (official)
* bashtls + simplerunner (unofficial)

### Installation

```sh
pip install trytls
```

### Usage

```sh
$ git clone https://github.com/ouspg/trytls.git
$ trytls https python trytls/stubs/python-urllib2/run.py
platform: OS X 10.11.5
runner: trytls 0.2.0 (CPython 2.7.10, OpenSSL 0.9.8zh)
stub: python 'run.py'
 PASS support for TLS server name indication (SNI) [accept badssl.com:443]
 PASS expired certificate [reject expired.badssl.com:443]
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
  ...
```

----

## Stubs

Stubs attempt to establish a **secure** connection to the given
service(host + port) and catch possible errors and exceptions to
determine if the connection was successful.

The last string the stub prints is the verdict (UNSUPPORTED,
ACCEPT etc.). If the stub provides additional context such as
the reason to accept/reject connection or an error message, the stub
prints them before the verdict.

Stubs in our directory are example TLS implementations for various
languages. TryTLS maintainers try to do their best to keep stubs up to
date.

However, TryTLS stub for specific library is best to be placed in
library's own repository and integrate TryTLS into any testing
framework in place. This way TryTLS gives best results in the long
run!

----

### Calling convention

All the stubs have a standalone program that takes up to three command
line arguments (`<host> <port> [ca-bundle]`):

 * `<host>` is the DNS name or IP-address of the service to connect to
 * `<port>` is the port to connect to
 * `[ca-bundle]` is optional location of the CA certificate bundle
   file to be used. The bundle file consists of PEM encoded
   certificates concatenated together.

Depending on the TLS library used in a stub, the library might use its own
CA certificate bundle or one delivered by the operating system or one delivered
by the stub.

----

## Backends

We currently support the following backends:

* BadSSL - we have cherry picked the relevant tests
* Local backend in the test runner itself (aka `localhost` backend)
* SSLLabs - protection against certain attacks
* freakattack.com - protection againstFREAK
* badtls.io
* tlsfun.de

Test runners allow user to test against all or any of these backends.

----

## Shootouts

We have tested some of our releases against popular software.
Results and repro instructions of these tests are collected
in the shootout documentation.

---

## Shootout 0.2

We ran TryTLS tests on major and still supported distributions.
For this shootout we limited ourselves to the official Docker images
of the distributions. Our objective was to check that the bundled
languages and libraries are safe to use with TLS. TryTLS focuses
on making sure that the certificates are checked properly.

Our main observations were:

* The same Python code produced different results in different distributions.
  Due to this, we should reach out Python gurus, are we doing something wrong
  or is running apparently correct Python code in some major distributions
  actually dangerous.

* Java stubs had issues we need to investigate and possibly fix before next
  shootout. Due to this, some Java results are not available.

* We were surprised to see the lack of SNI support in many of the still
  supported distributions. In next study we might investigate SNI support
  separately to get more directly security related results.
  
---

## Shootout 0.2

After previous shootout we contacted Python developers.
  TLS certificate verification failures in some OS distributions is a known
  problem to them. Some distributions have chosen not to enable this by default
  for backward compatibility. In some cases administrators have the possibility
  to add support per-case. More information can be found from our discussion tracking.
  Next we will try to reach out to the OS distribution maintainers for
  clarifications and further pointers.

---

## Shootout 0.3

We ran the TryTLS tests against the same target OS distributions and
languages as in the previous shootout, but used newer versions of
both the stubs and the runner. We used Docker for repeatibility
and ease of reproduction.

Our main observations were:

* OS distributions have issues with their Python version policies. Proper
  certificate checks are either not back ported from the fixed Python
  versions or changes have to be made either to the configuration or
  the code that works in safe manner in up to date environments. This
  is a hazard where neither software developers or users
  realize that code that works well for the developer may be
  unsafe for the user using different OS distribution than
  the developer. In a nutshell, there are many cases where the
  python based software may fail to check certificates in
  OS distributions currently still in wide use.
  
* Support of RC4 and MD5 is the in Python stubs is the most common
  crypto weakness identified in this shootout.

* Conflicting results where go stub accepts one SNI test but declines
  another in Ubuntu 14.04 requires further investigation.

---

### OS X OpenSSL verification surprises

When using native python shipped with OS X, the system default bundle will be
trusted even if instructed otherwise. This is troubling, as some organizations
do not want to trust the default bundles. Also, lately, the reputation of some
CAs have been brought into question.

This issue has been reported already 2014-03-03 by Hynek Schlawack.
CVE-2014-2234 describes the vulnerability exists on *A certain Apple patch for OpenSSL in
Apple OS X 10.9.2*. However, we have reproduced it in OS X 10.11.5 (15F34)
2016-06-12. The same behavior was observed with other python libraries
(e.g. urllib3 and requests) - as long as the
python shipped with OS X was used.

---

### How we found it

While developing the tool, we found an unexpected behavior. Apple's patch to their OpenSSL, apparently
made back in 2011, gives the user of OpenSSL more CAs than she bargained for. If the certificate check
fails with  user provided CA, Apple's OpenSSL *gives failed verifications a
second chance using the system keyring as trust store.*

Suggested workarounds
 * User: avoid running python code with native OS X python installation
 * Developer: consider warning users if OS X native python is used
    and non-ca-bundle is set by the user.

## Other found issues

We have also collected links to other unofficial TryTLS *inspired* findings:

* [Wreq connection to HTTPS site with invalid hostname · Issue #84 · bos/wreq](https://github.com/bos/wreq/issues/84)
  * See also [Is Wreq suitable for HTTPS applications? · Issue #82 · bos/wreq](https://github.com/bos/wreq/issues/82)
  * Related [http-client-tls connection to HTTPS site with invalid hostname · Issue #212 · snoyberg/http-client](https://github.com/snoyberg/http-client/issues/212)
* [http-client-tls vulnerable to Logjam? · Issue #215 · snoyberg/http-client](https://github.com/snoyberg/http-client/issues/215)
* [RFC7465: Prohibiting RC4 Cipher Suites · Issue #153 · vincenthz/hs-tls](https://github.com/vincenthz/hs-tls/issues/153)
* [Invoke-Webrequest accepts bad TLS certificates / crypto on MacOS · #1942 · PowerShell/PowerShell](https://github.com/PowerShell/PowerShell/issues/1942)
* [badtls.io certificates created with an old version of asn1crypto? · #1 · wbond/badtls.io](https://github.com/wbond/badtls.io/issues/1)
* [crypto/x509: bad error message  · #16834 · golang/go](https://github.com/golang/go/issues/16834)
* [crypto/x509: Certs with odd RDN layouts not handled, cause confusing errors · #16836 · golang/go](https://github.com/golang/go/issues/16836)
* [httpc:request("https://ssllabs:com:10444") not working correctly · #ERL-232 · Erlang/OTP 19](https://bugs.erlang.org/browse/ERL-232)

----

## Contact us

* Preferred: public tweet
  * Use #trytls and point it to @oupsg
* Less public alternative: direct twitter-message to @ouspg
