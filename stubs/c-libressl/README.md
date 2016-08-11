# LibreSSL stub for TryTLS

Stub is tested to work with:

 * OpenBSD-current (pre-6.1) with LibreSSL 2.5.0
 * OS X 10.11 with LibreSSL 2.4.2
 * Void Linux with LibreSSL 2.3.7

Doesn't work with:

 * LibreSSL 2.2.6 (tested in Alpine Edge (pre-3.5))

## Compile

Run `make`.

Depending on operating system, point the compiler to correct paths:

```console
make \
  CFLAGS=-I/usr/local/Cellar/libressl/2.4.2/include/ \
  LDFLAGS=-L/usr/local/Cellar/libressl/2.4.2/lib
```

## Test it

```console
$ ./run
./run <host> <port> [ca-bundle]

$ ./run google.com 443
HTTP/1.0 302 Found
ACCEPT
```

## Run it with TryTLS

```console
$ trytls https ./run
platform: OpenBSD
runner: trytls 0.2.1 (CPython 2.7.12, LibreSSL 2.5.0)
stub: './run'
..
<results removed>
..
```
