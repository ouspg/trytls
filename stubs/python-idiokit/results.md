```
platform: Linux (Ubuntu 16.04)
runner: trytls ...
stub: python 'stubs/python-idiokit/run.py'

[WIP]


...



platform: Linux (Ubuntu 16.04)
runner: simplerunner
stub: python 'stubs/python-idiokit/run.py'

[python-idiokit][ PASS ][VERIFY SUCCESS][ Valid cert ][google.com]
[python-idiokit][ PASS ][VERIFY FAILURE][ OS X vulnerability ][www.ssllabs.com]
[python-idiokit][ PASS ][VERIFY FAILURE][ Freak              ][www.ssllabs.com]
[python-idiokit][ PASS ][VERIFY FAILURE][ Logjam             ][www.ssllabs.com]
[python-idiokit][ PASS ][VERIFY SUCCESS][ correct cert                               ][localhost]
[python-idiokit][ PASS ][VERIFY FAILURE][ wrong hostname                             ][localhost]
[python-idiokit][ PASS ][VERIFY FAILURE][ correct cn, wrong san                      ][localhost]
[python-idiokit][ OK?  ][VERIFY SUCCESS][ correct cn, no san                         ][localhost]
[python-idiokit][ PASS ][VERIFY FAILURE][ expired cert                               ][localhost]
[python-idiokit][ PASS ][VERIFY FAILURE][ sslv2 supported                            ][localhost]
[python-idiokit][ PASS ][VERIFY FAILURE][ sslv3 supported                            ][localhost]
[python-idiokit][ PASS ][VERIFY SUCCESS][ tlsv1 supported                            ][localhost]
[python-idiokit][ PASS ][VERIFY SUCCESS][ tlsv1.1 supported                          ][localhost]
[python-idiokit][ PASS ][VERIFY SUCCESS][ tlsv1.2 supported                          ][localhost]
[python-idiokit][ PASS ][VERIFY SUCCESS][ supports ssl in at least some level        ][localhost]
[python-idiokit][ PASS ][VERIFY SUCCESS][ supports high(>128 bit) 'secure' ciphers   ][localhost]
[python-idiokit][ OK?  ][VERIFY FAILURE][ supports medium(~128 bit) 'secure' ciphers ][localhost]
[python-idiokit][ PASS ][VERIFY FAILURE][ supports 'insecure' ciphers                ][localhost]
[python-idiokit][ PASS ][VERIFY SUCCESS][ supports 'RSA'                             ][localhost]
[python-idiokit][ PASS ][VERIFY SUCCESS][ supports 'AES256'                          ][localhost]
[python-idiokit][ PASS ][VERIFY SUCCESS][ supports 'SHA384'                          ][localhost]
[python-idiokit][ OK?  ][VERIFY FAILURE][ supports 'ECDSA'                           ][localhost]
[python-idiokit][ OK?  ][VERIFY FAILURE][ supports 'SRP'                             ][localhost]
[python-idiokit][ PASS ][VERIFY SUCCESS][ supports 'AES'                             ][localhost]
[python-idiokit][ PASS ][VERIFY SUCCESS][ supports 'DH'                              ][localhost]
[python-idiokit][ PASS ][VERIFY SUCCESS][ supports 'SHA'                             ][localhost]
[python-idiokit][ OK?  ][VERIFY FAILURE][ supports 'DSS'                             ][localhost]
[python-idiokit][ PASS ][VERIFY SUCCESS][ supports 'CAMELLIA256'                     ][localhost]
[python-idiokit][ PASS ][VERIFY FAILURE][ supports 'AECDH'                           ][localhost]
[python-idiokit][ OK?  ][VERIFY FAILURE][ supports 'PSK'                             ][localhost]
[python-idiokit][ PASS ][VERIFY SUCCESS][ supports 'AES128'                          ][localhost]
[python-idiokit][ OK?  ][VERIFY FAILURE][ supports 'SEED'                            ][localhost]
[python-idiokit][ PASS ][VERIFY SUCCESS][ supports 'CAMELLIA128'                     ][localhost]
[python-idiokit][ PASS ][VERIFY FAILURE][ supports 'AECDH'                           ][localhost]
[python-idiokit][ PASS ][VERIFY FAILURE][ supports 'ADH'                             ][localhost]
[python-idiokit][ PASS ][VERIFY SUCCESS][ supports 'SHA256'                          ][localhost]
[python-idiokit][ PASS ][VERIFY FAILURE][ supports 'RC4'                             ][localhost]
[python-idiokit][ PASS ][VERIFY FAILURE][ supports 'MD5'                             ][localhost]
[python-idiokit][ PASS ][VERIFY FAILURE][ supports 'DES'                             ][localhost]
[python-idiokit][ PASS ][VERIFY SUCCESS][ supports 'EDH'                             ][localhost]
[python-idiokit][ PASS ][VERIFY SUCCESS][ supports 'ECDH'                            ][localhost]
[python-idiokit][ PASS ][VERIFY FAILURE][ supports 'ECDSA'                           ][localhost]
[python-idiokit][ PASS ][VERIFY SUCCESS][ supports '3DES'                            ][localhost]
[python-idiokit][ PASS ][VERIFY FAILURE][ supports 'NULL'                            ][localhost]
```
