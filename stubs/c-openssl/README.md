
## Get started

### Install

* gcc + openssl [deps](https://github.com/openssl/openssl)

### Run (example)
```
..# export LD_LIBRARY_PATH=/usr/local/lib/:$LD_LIBRARY_PATH ; may be required
..# gcc run.c -o run -L/usr/local/lib -lssl -lcrypto        ; in linux
..# ./run [host] [port] [ca-bundle]
```
