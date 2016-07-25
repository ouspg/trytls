```
platform: Linux (Ubuntu 16.04)
runner: trytls ...
stub: python 'stubs/python-idiokit/run.py'

[WIP]


...



platform: Linux (Ubuntu 16.04)
runner: simplerunner
stub: python 'stubs/python-idiokit/run.py'

[python-idiokit][ PASS ][VERIFY ACCEPT][ Valid cert ][google.com]
[python-idiokit][ PASS ][VERIFY REJECT][ OS X vulnerability ][www.ssllabs.com]
[python-idiokit][ PASS ][VERIFY REJECT][ Freak              ][www.ssllabs.com]
[python-idiokit][ PASS ][VERIFY REJECT][ Logjam             ][www.ssllabs.com]
[python-idiokit][ PASS ][VERIFY ACCEPT][ correct cert                               ][localhost]
[python-idiokit][ PASS ][VERIFY REJECT][ wrong hostname                             ][localhost]
[python-idiokit][ PASS ][VERIFY REJECT][ correct cn, wrong san                      ][localhost]
[python-idiokit][ OK?  ][VERIFY ACCEPT][ correct cn, no san                         ][localhost]
[python-idiokit][ PASS ][VERIFY REJECT][ expired cert                               ][localhost]
[python-idiokit][ PASS ][VERIFY REJECT][ sslv2 supported                            ][localhost]
[python-idiokit][ PASS ][VERIFY REJECT][ sslv3 supported                            ][localhost]
[python-idiokit][ PASS ][VERIFY ACCEPT][ tlsv1 supported                            ][localhost]
[python-idiokit][ PASS ][VERIFY ACCEPT][ tlsv1.1 supported                          ][localhost]
[python-idiokit][ PASS ][VERIFY ACCEPT][ tlsv1.2 supported                          ][localhost]
[python-idiokit][ PASS ][VERIFY ACCEPT][ supports ssl in at least some level        ][localhost]
[python-idiokit][ PASS ][VERIFY ACCEPT][ supports high(>128 bit) 'secure' ciphers   ][localhost]
[python-idiokit][ OK?  ][VERIFY REJECT][ supports medium(~128 bit) 'secure' ciphers ][localhost]
[python-idiokit][ PASS ][VERIFY REJECT][ supports 'insecure' ciphers                ][localhost]
[python-idiokit][ PASS ][VERIFY ACCEPT][ supports 'RSA'                             ][localhost]
[python-idiokit][ PASS ][VERIFY ACCEPT][ supports 'AES256'                          ][localhost]
[python-idiokit][ PASS ][VERIFY ACCEPT][ supports 'SHA384'                          ][localhost]
[python-idiokit][ OK?  ][VERIFY REJECT][ supports 'ECDSA'                           ][localhost]
[python-idiokit][ OK?  ][VERIFY REJECT][ supports 'SRP'                             ][localhost]
[python-idiokit][ PASS ][VERIFY ACCEPT][ supports 'AES'                             ][localhost]
[python-idiokit][ PASS ][VERIFY ACCEPT][ supports 'DH'                              ][localhost]
[python-idiokit][ PASS ][VERIFY ACCEPT][ supports 'SHA'                             ][localhost]
[python-idiokit][ OK?  ][VERIFY REJECT][ supports 'DSS'                             ][localhost]
[python-idiokit][ PASS ][VERIFY ACCEPT][ supports 'CAMELLIA256'                     ][localhost]
[python-idiokit][ PASS ][VERIFY REJECT][ supports 'AECDH'                           ][localhost]
[python-idiokit][ OK?  ][VERIFY REJECT][ supports 'PSK'                             ][localhost]
[python-idiokit][ PASS ][VERIFY ACCEPT][ supports 'AES128'                          ][localhost]
[python-idiokit][ OK?  ][VERIFY REJECT][ supports 'SEED'                            ][localhost]
[python-idiokit][ PASS ][VERIFY ACCEPT][ supports 'CAMELLIA128'                     ][localhost]
[python-idiokit][ PASS ][VERIFY REJECT][ supports 'AECDH'                           ][localhost]
[python-idiokit][ PASS ][VERIFY REJECT][ supports 'ADH'                             ][localhost]
[python-idiokit][ PASS ][VERIFY ACCEPT][ supports 'SHA256'                          ][localhost]
[python-idiokit][ PASS ][VERIFY REJECT][ supports 'RC4'                             ][localhost]
[python-idiokit][ PASS ][VERIFY REJECT][ supports 'MD5'                             ][localhost]
[python-idiokit][ PASS ][VERIFY REJECT][ supports 'DES'                             ][localhost]
[python-idiokit][ PASS ][VERIFY ACCEPT][ supports 'EDH'                             ][localhost]
[python-idiokit][ PASS ][VERIFY ACCEPT][ supports 'ECDH'                            ][localhost]
[python-idiokit][ PASS ][VERIFY REJECT][ supports 'ECDSA'                           ][localhost]
[python-idiokit][ PASS ][VERIFY ACCEPT][ supports '3DES'                            ][localhost]
[python-idiokit][ PASS ][VERIFY REJECT][ supports 'NULL'                            ][localhost]
```
