# BadSSL services and reasons for usage/ignore

[badssl.com service](https://badssl.com) is an unofficial service provided
by Google and its source code is available on the [GitHub](https://github.com/google/badssl.com).

[badssl.com](https://badssl.com) is meant for manual testing of security UI
in web clients. We are (ab)using it as one of the backends for the TryTLS.

Tests suitable or unsuitable for the automation in this content are document below
with some reasoning for the selection.

## Word of caution

As stated in the `badssl.com` repository:

> Most subdomains are likely to have stable functionality, but anything could change without notice. If you would like a documented guarantee for a particular use case, please file an issue. (Alternatively, you could make a fork and host your own copy.)

## Used

* `expired`: Obsolete cert should not be valid
* `wrong.host`: Wrong host should not be valid
 * In 2016-07 this was implemented as `wrong.host.badssl.com` against `*.badssl.com` wildcard certificate. RFCs for use of TLS in different protocols disagree on how wildcard certificates should be verified against the hostname.
 * See [About Wildcard Certificates by cacert.org](http://wiki.cacert.org/WildcardCertificates)
* `self-signed`: Who knows who signed? Should not be valid
* `sha256`: Should be valid to future proof
* `1000-sans`: Massive amount of alternative names should be valid
* `incomplete-chain`: Cert should have full proof of chain to the trusted CA and hence this should not be valid
* Dangerous or comporimised CAs:
 * `superfish`: Super fishy CA should not be valid
 * `edellroot`: Rotten roots CA should not be valid
 * `dsdtestprovider`: Unproviding CA should not be valid

## Unused

* `sha1-2016`: Maybe invalid after 2016
* `sha1-2017`: Maybe invalid after 2017
* `10000-sans`: Gargantuan amount of alternative names, useful as valid for possible future proofing
* `rsa8192`: Not compulsory, but if one wants to future proof, make valid
* `pinning-test`: Should be invalid, but only used for Chrome
* **other tests**: Out of scope or not yet reviewed
