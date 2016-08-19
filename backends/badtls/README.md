# BadSSL services and reasons for usage/ignore

[badtls.io service](https://badtls.io) is an unofficial service and its source code is available on the [GitHub](https://github.com/wbond/badtls.io).

[badtls.io](https://badssl.com) is a server that serves up various bad (and good) TLS certificates and configurations for the sake of testing.. We are (ab)using it as one of the backends for the TryTLS.

Tests suitable or unsuitable for the automation in this content are document below
with some reasoning for the selection.

# Used
```
domain-match.badtls.io:10000      valid certificate Common Name, should pass
wildcard-match.badtls.io:10001    valid certificate Common Name using wildcards, should pass
san-match.badtls.io:10002         supprt for Subject Alternative Name (SAN), should pass
dh1024.badtls.io:10005            TLS handshake with 1024 bit Diffie-Hellman (DH), should pass
expired-1963.badtls.io:11000      certificate expired in year 1963, should fail
future.badtls.io:11001            certificate validity starts in future, should fail
domain-mismatch.badtls.io:11002   mismatch in certificate's Common Name, should fail
san-mismatch.badtls.io:11003      Subject Alternative Name (SAN) mismatch, should fail
weak-sig.badtls.io:11004          MD5 signature algorithm, should fail
bad-key-usage.badtls.io:11005     certificate has invalid key usage for HTTPS connection, should fail
expired.badtls.io:11006           expired certificate, should fail
wildcard.mismatch.badtls.io:11007 invalid wildcard certificate Common Name, should fail
rc4.badtls.io:11008               supports RC4 ciphers, should fail
rc4-md5.badtls.io:11009           supports RC4 with MD5 ciphers, should fail
```

# Unused

```
required-auth.badtls.io:11009     Out of scope
optional-auth.badtls.io:11009     Out of scope
```
