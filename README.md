# TryTLS [![CircleCI](https://circleci.com/gh/ouspg/trytls.svg?style=shield)](https://circleci.com/gh/ouspg/trytls)

Does *your* TLS/SSL library check
[certificates](https://tools.ietf.org/html/rfc5280) properly?
Broken certificate checks seems to be an overlooked issue.
Handling certificates is surprisingly complex, and calls for extra attention.

TryTLS is a tool for the software and library developers, vulnerability
researchers, and end-users, who want to use TLS safely.

We hope to help you to test certificate handling easily. We support
systematic and readily planned tests and try make integrating your
favorite language and library easy.

## How Does It Work

![Architecture](doc/concept-pic.png)

* **Backends (servers)** provide TLS/SSL tests for stubs (clients).
* **Stubs** attempt to establish secure TLS/SSL connections to backends.
* **Runners** run the stubs against backends and provide the results of the tests.

I you prefer watching over reading, take a look at
[TryTLS training under 4 minutes!](https://www.youtube.com/watch?v=85EO61l2Oa4)
and
[What exactly does TryTLS test?](https://www.youtube.com/watch?v=aHw2Ulr6zH8) on
YouTube.

## Runners

* [trytls](runners/trytls/) (official)
* [bashtls](runners/bashtls/) +
  [simplerunner](runners/bashtls/shared/simplerunner) (unofficial)

### Installation

```sh
pip install trytls
```

<!-- markdownlint-disable MD013 -->

In case you don't have [`pip`](https://pip.pypa.io/) installed, please refer to
[these instructions](http://docs.python-guide.org/en/latest/starting/installation/).

<!-- markdownlint-enable MD013 -->

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

## Stubs

Stubs and their documentation can be found from the [stubs/](stubs/) directory.

## Backends

We are currently working to support the following [backends](backends/):

* [BadSSL](https://badssl.com) - we have cherry picked the
  [relevant tests](backends/badssl/README.md)
* Local backend in the test runner itself (aka `localhost` backend)
* [SSLLabs](https://ssllabs.com) - protection against
  [certain attacks](backends/ssllabs/README.md)
* [freakattack.com](https://freakattack.com/) - protection against
  [FREAK](https://mitls.org/pages/attacks/SMACK#freak)
* [Trytls backend](backends/trytls) both as docker based
  "run-it-yourself" packaging and as a hosted service provided by us [WIP]

Test runners allow user to test against all or any of these backends.

## What TryTLS Is Not

* We do not address possible client certificate check problems in server code
* We do not do or require a man-in-the-middle tools
* We do not support smart TVs, IoT toasters and other such devices that
  can't run any of the runners

## Found issues

We have tested some of our releases against popular software.
Results and repro instructions of these tests are collected
in the [shootout documentation](shootout/).

We have also collected links to other TryTLS inspired findings:

<!-- markdownlint-disable MD013 -->

* [Wreq connection to HTTPS site with invalid hostname · Issue #84 · bos/wreq](https://github.com/bos/wreq/issues/84)
  * See also [Is Wreq suitable for HTTPS applications? · Issue #82 · bos/wreq](https://github.com/bos/wreq/issues/82)
  * Related [http-client-tls connection to HTTPS site with invalid hostname · Issue #212 · snoyberg/http-client](https://github.com/snoyberg/http-client/issues/212)
* [http-client-tls vulnerable to Logjam? · Issue #215 · snoyberg/http-client](https://github.com/snoyberg/http-client/issues/215)
* [RFC7465: Prohibiting RC4 Cipher Suites · Issue #153 · vincenthz/hs-tls](https://github.com/vincenthz/hs-tls/issues/153)
* [Invoke-Webrequest accepts bad TLS certificates / crypto on MacOS · #1942 · PowerShell/PowerShell](https://github.com/PowerShell/PowerShell/issues/1942)
* [badtls.io certificates created with an old version of asn1crypto? · #1 · wbond/badtls.io](https://github.com/wbond/badtls.io/issues/1)
* [crypto/x509: bad error message  · #16834 · golang/go](https://github.com/golang/go/issues/16834)
* [crypto/x509: Certs with odd RDN layouts not handled, cause confusing errors · #16836 · golang/go](https://github.com/golang/go/issues/16836)

<!-- markdownlint-enable MD013 -->

## Contributors

* Mauri Miettinen ([@Mamietti](https://github.com/Mamietti))
* Aleksi Klasila ([@aleksiklasila](https://github.com/aleksiklasila))
* Jani Kenttälä ([@evilon](https://github.com/evilon))
* Ossi Herrala ([@oherrala](https://github.com/oherrala))
* Joachim Viide ([@jviide](https://github.com/jviide))
* Marko Laakso ([@ikisusi](https://github.com/ikisusi))
* Pekka Pietikäinen ([@ppietikainen](https://github.com/ppietikainen))
* Joonas Kuorilehto ([@joneskoo](https://github.com/joneskoo))
* Kasper Kyllönen ([@nkapu](https://github.com/nkapu))
* Timo Mattila ([@timattil](https://github.com/timattil))
* Low Kian Seong ([@lowks](https://github.com/lowks))
* Mikko Yliniemi ([@mikessu](https://github.com/mikessu))
* Christian Wieser
* Jakub Wilk ([@jwilk](https://github.com/jwilk))
* Juho Myllylahti ([@mutjake](https://github.com/mutjake))

We invite people to [contribute](CONTRIBUTING.md).

## Contact us

* Preferred: public tweet
  * Use #trytls and point it to @oupsg
* Less public alternative: direct twitter-message to @ouspg
