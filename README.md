# TryTLS

TryTLS verifies the certificate verification behavior of programming languages and libraries. It provides examples and results and tries to make it easy for the community to improve the coverage.

Broken certificate checks is a potentially overlooked issue.

TryTLS is a tool for the: 
 * software and library developers,
 * vulnerability researchers, and
 * software end-users, who are interested about the security of the implementation.
 
We invite people to contribute.

---

## What

 * Check the behavior of a software library - does it properly check the certificates?
 * Test the TLS client code, do not address possible client certificate check problems in server code
 * Test against specialized backends, do not require a man in the middle setup
 * Drive the tests with code, do not worry about smart TVs, IoT toasters and other such devices

---

## How

 * "Checking of checks" -> how libraries handle signatures, domain names, time, SNI etc.
 * Use ports and virtual hosts to provide falsified/broken certificate checks
 * Provide both end results and the source material used to get those results -> enable reproduction
 * Open public project created with scalability in mind -> anyone can contibute
 * Document use cases -> ease of access
 * Utilize docker -> encapsulate dependencies for the examples and the backends
 * Support multiple backends -> use hosted backends or run your own on the host or in the cloud

---

## Architecture

![Architecture](doc/architecture.jpg)

---

## Stubs

Example code (stubs) using TLS in different languages and libraries live in
the [stubs/](stubs/) directory. You can contribute your stub here or just BYOR (Bring Your Own Repository).

These stubs should attempt to use the chosen language and library
properly to establish a secure TLS connection to the given destination.

### Calling convention

All stubs should have a standalone program that takes up to three command
line arguments (`<host> <port> [ca-bundle]`):

 * `<host>` is the DNS name or IP-address of the service to connect to
 * `<port>` is the port to connect to
 * `[ca-bundle]` is optional location of the CA certificate bundle to be used
 instead of the built-in default

### Return values

Stubs should attempt to establish a **secure** connection to the given
service and catch possible errors and exceptions to determine if it was successful.

All stubs should return one of the following strings to the standard output:

 * `VERIFY SUCCESS` when connection was established in a secure way
 * `VERIFY FAILURE` when connection failed to establish in a secure way
 * `UNSUPPORTED` if the example has not implemented the requested behaviour (e.g. setting
   CA certificate bundle)

If anything else is returned, then the test has erred.

Unless a fatal error occurs, examples should always return with process exit value 0.

### Packaging

A stub should be confined to a directory named in a way that describes the
chosen target language and library or service.

A stub should have a top level `README.md` that describes how to run the example. The stubs should have a `run` command.

Optionally a stub can have a `Dockerfile` that encapsulates the environment
and the dependancies needed to run the example.

---

## Test runners

We currently have one [python based test runner](showrunner/) implemented.

Installation:

```console
$ python setup.py install --user
```

Example usage:

```console
$ ~/.local/bin/trytls python3 stubs/python3-urllib/run.py
PASS badssl(True, 'sha1-2016')
PASS badssl(False, 'expired')
...
```

---

## Backends

We currently are working to support following backends implementing the tests:

 * Local backend in the test runner itself (aka `localhost` backend) [WIP]
 * TryTLS backend both as docker based "run-it-yourself" packaging and as a
 hosted service provided by us [WIP]
 * [BadSSL](https://badssl.com)

Test runners should should allow user to test against all or any of these backends.

## TryTLS Team

 * Mauri Miettinen ([@Mamietti](https://github.com/Mamietti))
 * Aleksi Klasila ([@aleksiklasila](https://github.com/aleksiklasila))


