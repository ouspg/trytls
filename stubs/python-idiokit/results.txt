```
platform: Linux (Ubuntu 16.04)
runner: trytls ...
stub: python 'stubs/python-idiokit/run.py'

[WIP]


...



platform: Linux (Ubuntu 16.04)
runner: simplerunner
stub: python 'stubs/python-idiokit/run.py'

[python-idiokit][ PASS ][ACCEPT][ Valid cert ][google.com]
[python-idiokit][ PASS ][REJECT][ OS X vulnerability ][www.ssllabs.com]
[python-idiokit][ PASS ][REJECT][ Freak              ][www.ssllabs.com]
[python-idiokit][ PASS ][REJECT][ Logjam             ][www.ssllabs.com]
[python-idiokit][ PASS ][ACCEPT][ correct cert                               ][localhost]
[python-idiokit][ PASS ][REJECT][ wrong hostname                             ][localhost]
[python-idiokit][ PASS ][REJECT][ correct cn, wrong san                      ][localhost]
[python-idiokit][ OK?  ][ACCEPT][ correct cn, no san                         ][localhost]
[python-idiokit][ PASS ][REJECT][ expired cert                               ][localhost]
[python-idiokit][ PASS ][REJECT][ sslv2 supported                            ][localhost]
[python-idiokit][ PASS ][REJECT][ sslv3 supported                            ][localhost]
[python-idiokit][ PASS ][ACCEPT][ tlsv1 supported                            ][localhost]
[python-idiokit][ PASS ][ACCEPT][ tlsv1.1 supported                          ][localhost]
[python-idiokit][ PASS ][ACCEPT][ tlsv1.2 supported                          ][localhost]
[python-idiokit][ PASS ][ACCEPT][ supports ssl in at least some level        ][localhost]
[python-idiokit][ PASS ][ACCEPT][ supports high(>128 bit) 'secure' ciphers   ][localhost]
[python-idiokit][ OK?  ][REJECT][ supports medium(~128 bit) 'secure' ciphers ][localhost]
[python-idiokit][ PASS ][REJECT][ supports 'insecure' ciphers                ][localhost]
[python-idiokit][ PASS ][ACCEPT][ supports 'RSA'                             ][localhost]
[python-idiokit][ PASS ][ACCEPT][ supports 'AES256'                          ][localhost]
[python-idiokit][ PASS ][ACCEPT][ supports 'SHA384'                          ][localhost]
[python-idiokit][ OK?  ][REJECT][ supports 'ECDSA'                           ][localhost]
[python-idiokit][ OK?  ][REJECT][ supports 'SRP'                             ][localhost]
[python-idiokit][ PASS ][ACCEPT][ supports 'AES'                             ][localhost]
[python-idiokit][ PASS ][ACCEPT][ supports 'DH'                              ][localhost]
[python-idiokit][ PASS ][ACCEPT][ supports 'SHA'                             ][localhost]
[python-idiokit][ OK?  ][REJECT][ supports 'DSS'                             ][localhost]
[python-idiokit][ PASS ][ACCEPT][ supports 'CAMELLIA256'                     ][localhost]
[python-idiokit][ PASS ][REJECT][ supports 'AECDH'                           ][localhost]
[python-idiokit][ OK?  ][REJECT][ supports 'PSK'                             ][localhost]
[python-idiokit][ PASS ][ACCEPT][ supports 'AES128'                          ][localhost]
[python-idiokit][ OK?  ][REJECT][ supports 'SEED'                            ][localhost]
[python-idiokit][ PASS ][ACCEPT][ supports 'CAMELLIA128'                     ][localhost]
[python-idiokit][ PASS ][REJECT][ supports 'AECDH'                           ][localhost]
[python-idiokit][ PASS ][REJECT][ supports 'ADH'                             ][localhost]
[python-idiokit][ PASS ][ACCEPT][ supports 'SHA256'                          ][localhost]
[python-idiokit][ PASS ][REJECT][ supports 'RC4'                             ][localhost]
[python-idiokit][ PASS ][REJECT][ supports 'MD5'                             ][localhost]
[python-idiokit][ PASS ][REJECT][ supports 'DES'                             ][localhost]
[python-idiokit][ PASS ][ACCEPT][ supports 'EDH'                             ][localhost]
[python-idiokit][ PASS ][ACCEPT][ supports 'ECDH'                            ][localhost]
[python-idiokit][ PASS ][REJECT][ supports 'ECDSA'                           ][localhost]
[python-idiokit][ PASS ][ACCEPT][ supports '3DES'                            ][localhost]
[python-idiokit][ PASS ][REJECT][ supports 'NULL'                            ][localhost]
```
