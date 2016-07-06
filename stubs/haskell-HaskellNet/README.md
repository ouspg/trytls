# TryTLS test for Haskell's HaskellNet-SSL library

https://hackage.haskell.org/package/HaskellNet-SSL

## Howto build and run

You have three different options for running tests. Docker, Stack and
Cabal.

### Docker

Tests can be easily run inside [Docker](https://www.docker.com/)
container. This takes care of setting up the appropriate Haskell
environment with all dependencies and test stub installed.

build:

```
$ docker build -t test-haskellnet --rm .
```

test:

```
$ docker run --rm test-haskellnet
test-HaskellNet <host> <port> [ca-bundle]
```

run:

```
$ trytls -- docker run --rm test-haskellnet
```

cleanup (destroys docker container image):

```
$ docker rmi test-haskellnet
```

### Stack

If you have [The Haskell Tool Stack](http://www.haskellstack.org/)
already installed then this might be easier and faster than Docker
version above. However, `stack` might not use latest and greatest
version of all required packages so check out the `resolver` setting
from `stack.yaml` file and adjust to your needs or pass `--resolver`
flag to `stack` command to select it at runtime.

build:

```
$ stack build
```

test:

```
$ stack exec test-haskellnet
test-haskellnet <host> <port> [ca-bundle]
```

run:

```
$ trytls -- stack exec test-Haskellnet
```

cleanup:

```
$ rm -rf .stack-work
```

### Cabal sandbox

Cabal

build:

```
$ cabal sandbox init
$ cabal install --only-dependencies
$ cabal build
```

test:

```
$ ./dist/build/test-HaskellNet/test-HaskellNet
test-HaskellNet <host> <port> [ca-bundle]
```

run:

```
$ trytls ./dist/build/test-HaskellNet/test-HaskellNet
```

cleanup:

```
$ cabal sandbox delete
```
