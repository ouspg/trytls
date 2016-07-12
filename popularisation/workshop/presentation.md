# TryTLS

Does *your* library check TLS certificates properly?
Broken certificate checks seems to be an overlooked issue.
Handling certificates is surprisingly complex, and calls for extra attention.

TryTLS is a tool for the software and library developers, vulnerability
researchers, and end-users, who want to use TLS safely for their favorite language and library.

---

## Architecture recap

![Architecture](https://raw.githubusercontent.com/ouspg/trytls/master/doc/architecture-scaled.jpg)

 * **Backends** use ports and virtual hosts to provide falsified/broken certificate checks
 * **Stubs** are written for the target languages and libraries to attempt the TLS connection
 * **Runners** "check the checks" by calling the stubs systematically to find out
 how libraries handle signatures, domain names, time, SNI etc. against the backends

---

## Installation

```sh
$ git clone https://github.com/ouspg/trytls.git
$ cd trytls
$ pip install .
```

In case you don't have `pip` (https://pip.pypa.io/) installed, please refer to these instructions: http://docs.python-guide.org/en/latest/starting/installation/

---

## Usage

Run a stub yourself:

```
$ trytls https python stubs/python-urllib2/run.py
  PASS badssl(False, 'expired')
  PASS badssl(False, 'wrong.host')
  PASS badssl(False, 'self-signed')
  PASS badssl(True, 'sha256')
  PASS badssl(True, '1000-sans')
x FAIL badssl(True, '10000-sans')
x FAIL badssl(False, 'incomplete-chain')
  PASS badssl(False, 'superfish')
  PASS badssl(False, 'edellroot')
  PASS badssl(False, 'dsdtestprovider')
x FAIL badssl_onlymyca(False, 'sha256')
  PASS local(True, 'localhost', callback=<function https_callback at 0x108efe050>)
  PASS local(False, 'nothing', callback=<function https_callback at 0x108efe050>)
```

---

# HOW?

## Stubs

Example code (stubs) using TLS in different languages and libraries live in `stubs/`.
You can contribute your stub there or just BYOR (Bring Your Own Repository).

These stubs should attempt to use the chosen language and library
properly to establish a secure TLS connection to the given destination and catch possible errors and exceptions to determine if it was successful.

---

## Calling convention

All stubs should have a standalone program that takes up to three command
line arguments (`<host> <port> [ca-bundle]`):

 * `<host>` is the DNS name or IP-address of the service to connect to
 * `<port>` is the port to connect to
 * `[ca-bundle]` is optional location of the CA certificate bundle to be used
 instead of the built-in default

---

## Return values

All stubs should return one of the following strings to the standard output:

 * `VERIFY SUCCESS` when connection was established in a secure way
 * `VERIFY FAILURE` when connection failed to establish in a secure way
 * `UNSUPPORTED` if the example has not implemented the requested behaviour (e.g. setting
   CA certificate bundle)

If anything else is returned, then the test has erred.

Unless a fatal error occurs, examples should always return with process exit value 0.

---

# Time to get stubbing!

If you need a quick recap of the calling convention,
go to `stubs/` folder in our GitHub repo https://github.com/ouspg/trytls.git

$ trytls https python stubs/python-urllib2/run.py

---

# Packaging

A stub should be confined to a directory named in a way that describes the
chosen target language and library or service, e.g. `<language>-<library>`.

A stub should have a top level `README.md` that describes how to run the stub.

The stubs should have a `run` command with optional and approriate file
extension for the language in question.
