## Stubs

Example code (stubs) using TLS in different languages and libraries live in here.
You can contribute your stub here or just BYOR (Bring Your Own Repository).

These stubs should attempt to use the chosen language and library
properly to establish a secure TLS connection to the given destination.

"Have you heard of the TryTLS tester who lost his hands? He only had stubs left."

---

### Calling convention

All stubs should have a standalone program that takes up to three command
line arguments (`<host> <port> [ca-bundle]`):

 * `<host>` is the DNS name or IP-address of the service to connect to
 * `<port>` is the port to connect to
 * `[ca-bundle]` is optional location of the CA certificate bundle
   file to be used. The bundle file should consists of PEM encoded
   certificates concatenated together.

Depending on the TLS library used in stub, the library might use own
CA certificate bundle bundled with library or use one delivered by
operating system.


---

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


---

### Testing the stub

To test that the stub works as it should you can perform couple of
easy tests by running it on command line (stub is named `forrest.run`
in these examples).

Running the program without any arguments should give error message:

```sh
$ forrest.run
<This should print some kind of (helpful) error message>
```

Connecting to `google.com` on HTTPS port should be success:

```sh
$ forrest.run google.com 443
VERIFY SUCCESS
```

Connecting to `badssl.com`'s `untrusted-root` should be failure:

```sh
$ forrest.run untrusted-root.badssl.com 443
VERIFY FAILURE
```

If these simple tests work, your stub is ready to be tested with
TryTLS runner.

If you want to test the CA bundle argument, then you need valid CA
bundle file for example from
[certifi.io](https://certifi.io/en/latest/).

Download the certifi.io CA bundle to file named `ca-bundle.pem` (with
for example curl: `curl -L -o ca-bundle.pem
https://mkcert.org/generate/`) and then test:

```sh
$ forrest.run google.com 443 ca-bundle.pem
VERIFY SUCCESS
```

---

### Packaging

A stub should be confined to a directory named in a way that describes the
chosen target language and library or service, e.g. `<language>-<library>`.

A stub should have a top level `README.md` that describes how to run the stub.

The stubs should have a `run` command with optional and approriate file
extension for the language in question.

Optionally a stub can have a `Dockerfile` that encapsulates the environment
and the dependancies needed to run the example.

---

Finished stubs (documentation and correct calling convention):
* go-nethttp
* haskell-wreq
* java-https
* java-net
* lua5.1-luasec
* python-requests
* python-urllib2
* python-urllib3
* python3-urllib
