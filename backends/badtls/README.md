# badtls services

## Used

 * `domain-match.badtls.io:10000`: valid certificate Common Name
 * `wildcard-match.badtls.io:10001`: valid wildcard certificate Common Name
 * `san-match.badtls.io:10002`: support for Subject Alternative Name (SAN)
 * `dh1024.badtls.io:10005`: TLS handshake with 1024 bit Diffie-Hellman (DH)
 * `expired-1963.badtls.io:11000`: certificate expired in year 1963
 * `future.badtls.io 11001`: certificate validity starts in future
 * `domain-mismatch.badtls.io:11002`: mismatch in certificate's Common Name
 * `san-mismatch.badtls.io:11003`: Subject Alternative Name (SAN) mismatch
 * `bad-key-usage.badtls.io:11005`: certificate has invalid key usage for HTTPS connection
 * `expired.badtls.io:11006`: expired certificate
 * `wildcard.mismatch.badtls.io:11007`: invalid wildcard certificate Common Name"
 * `rc4.badtls.io:11008`: RC4 ciphers (RFC7465)
 * `weak-sig.badtls.io:11004`: MD5 signature algorithm (RFC6151)
 * `rc4-md5.badtls.io:11009`: RC4 with MD5 ciphers

