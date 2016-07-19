**Author: [@oherrala](https://github.com/oherrala)**

# TryTLS stub for Haskell's wreq library

https://hackage.haskell.org/package/wreq

## Howto build and run

You have three different options for running tests. Docker, Stack and
Cabal.

### Docker

Tests can be easily run inside [Docker](https://www.docker.com/)
container. This takes care of setting up the appropriate Haskell
environment with all dependencies and test stub installed.

build:

```console
$ docker build -t test-wreq --rm .
```

test:

```console
$ docker run --rm test-wreq
test-wreq <host> <port> [ca-bundle]
```

run:

```console
$ trytls https -- docker run --rm test-wreq
```

cleanup (destroys docker container image):

```console
$ docker rmi test-wreq
```

### Stack

If you have [The Haskell Tool Stack](http://www.haskellstack.org/)
already installed then this might be easier and faster than Docker
version above. However, `stack` might not use latest and greatest
version of all required packages so check out the `resolver` setting
from `stack.yaml` file and adjust to your needs or pass `--resolver`
flag to `stack` command to select it at runtime.

build:

```console
$ stack build
```

test:

```console
$ stack exec test-wreq
test-wreq <host> <port> [ca-bundle]
```

run:

```console
$ trytls https -- stack exec test-wreq
```

cleanup:

```console
$ rm -rf .stack-work
```

### Cabal sandbox

Cabal is the traditional software to build Haskell libraries and
programs. Both examples above (Docker and Stack) use Cabal under the
hood for building.

build:

```console
$ cabal sandbox init
$ cabal install --only-dependencies
$ cabal build
```

test:

```console
$ ./dist/build/test-wreq/test-wreq
test-wreq <host> <port> [ca-bundle]
```

run:

```
$ trytls https -- ./dist/build/test-wreq/test-wreq
```

cleanup:

```console
$ cabal sandbox delete
```
