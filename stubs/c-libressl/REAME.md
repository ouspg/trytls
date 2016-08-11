# LibreSSL stub for TryTLS

Tested with:

 [x] OpenBSD-current (pre-6.1) with LibreSSL 2.5.0
 [x] OS X 10.11 with LibreSSL 2.4.2

## Compile

Run `make`.

Depending on operating system, point the compiler to correct paths:

```console
make \
  CFLAGS=-I/usr/local/Cellar/libressl/2.4.2/include/ \
  LDFLAGS=-L/usr/local/Cellar/libressl/2.4.2/lib
```
