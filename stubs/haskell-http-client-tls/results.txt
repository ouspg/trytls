```
platform: OS X 10.11.5
runner: trytls 0.1.0 (CPython 2.7.10, OpenSSL 0.9.8zh)
stub: docker run '--rm' 'test-http-client-tls'
 PASS expired certificate [reject expired.badssl.com:443]
      output: HandshakeFailed (Error_Protocol ("certificate has expired",True,CertificateExpired))
 FAIL wrong hostname in certificate [reject wrong.host.badssl.com:443]
      output: 200 OK
 PASS self-signed certificate [reject self-signed.badssl.com:443]
      output: HandshakeFailed (Error_Protocol ("certificate rejected: [SelfSigned]",True,CertificateUnknown))
 PASS SHA-256 signature [accept sha256.badssl.com:443]
      output: 200 OK
 PASS 1000 subjectAltNames [accept 1000-sans.badssl.com:443]
      output: 200 OK
 PASS incomplete chain of trust [reject incomplete-chain.badssl.com:443]
      output: HandshakeFailed (Error_Protocol ("certificate has unknown CA",True,UnknownCa))
 PASS Superfish CA [reject superfish.badssl.com:443]
      output: HandshakeFailed (Error_Protocol ("certificate has unknown CA",True,UnknownCa))
 PASS eDellRoot CA [reject edellroot.badssl.com:443]
      output: HandshakeFailed (Error_Protocol ("certificate has unknown CA",True,UnknownCa))
 PASS DSDTestProvider CA [reject dsdtestprovider.badssl.com:443]
      output: HandshakeFailed (Error_Protocol ("certificate has unknown CA",True,UnknownCa))
 PASS protect against an OS X vulnerability [reject www.ssllabs.com:10443]
      output: HandshakeFailed (Error_Protocol ("bad SignatureRSA for ecdhparams",True,HandshakeFailure))
 PASS protect against the FREAK attack [reject www.ssllabs.com:10444]
      output: HandshakeFailed (Error_Packet_Parsing "handshake[HandshakeType_ServerKeyXchg]: parsing error: remaining bytes")
 FAIL protect against the Logjam attack [reject www.ssllabs.com:10445]
      output: 200 OK
ERROR valid localhost certificate [accept localhost:50880]
      reason: stub exited with return code 1
      output: Error: Invalid ca-bundle in /var/folders/nt/_ggb7gp565jg1b_ys8xws3600000gp/T/tmpeXV2El/0
ERROR invalid localhost certificate [reject localhost:50885]
      reason: stub exited with return code 1
      output: Error: Invalid ca-bundle in /var/folders/nt/_ggb7gp565jg1b_ys8xws3600000gp/T/tmpNSbZYo/0
ERROR use only the given CA bundle, not system's [reject sha256.badssl.com:443]
      reason: stub exited with return code 1
      output: Error: Invalid ca-bundle in /var/folders/nt/_ggb7gp565jg1b_ys8xws3600000gp/T/tmpc5FNQm/0
```
