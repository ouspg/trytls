
# TryTLS stub for HHVM/PHP remote file Handling

This stub is shameless copy of [php-file-get-contents](../php-file-get-contents/) stub. Only changes are in documentation and `Dockerfile` to run it.

[HHVM](http://hhvm.com/) is *"an open-source virtual machine designed for
executing programs written in Hack and PHP. HHVM uses a just-in-time (JIT)
compilation approach to achieve superior performance while maintaining the
development flexibility that PHP provides."*

# Run directly with HHVM

```console
$ hhvm run.php
```

# Building Dockerfile

```console
$ docker build -t hhvm-file-get-contents .
```

# Running in Docker

```console
$ docker run -ti --rm hhvm-file-get-contents
```
