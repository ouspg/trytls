## Stubs

Stubs in different languages and libraries live in here.
You can contribute your stub here or just BYOR (Bring Your Own Repository).

The stubs should attempt to use the chosen language and library
properly to establish a secure TLS connection to the given destination.

"Have you heard of the TryTLS tester who lost his hands? He only had stubs left."

---

### Calling convention

All the stubs should have a standalone program that takes up to three command
line arguments (`<host> <port> [ca-bundle]`):

 * `<host>` is the DNS name or IP-address of the service to connect to
 * `<port>` is the port to connect to
 * `[ca-bundle]` is optional location of the CA certificate bundle
   file to be used. The bundle file should consists of PEM encoded
   certificates concatenated together.

Depending on the TLS library used in a stub, the library might use it's own
CA certificate bundle or one delivered by the operating system or one delivered
by the stub.


---

### Return values

Stubs should attempt to establish a **secure** connection to the given
service(host + port) and catch possible errors and exceptions to determine if the connection was successful.

The last string the stub should print is the verdict (UNSUPPORTED, ACCEPT etc.). If you want the stub to print additional context such as the reason to accept/reject connection or an error message, the stub should print them before the verdict.

The data printed should follow the following set of instructions or a similar one.

<pre>
1.0 print (optional context)
2.0 if [the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)] then
      2.1 if [ the number of arguments is 2 (host + port) or 3 (host + port + ca-bundle) ] then
         print "UNSUPPORTED"
         return zero
      2.2 else goto "fatal error"
3.0 else if [the stub could connect to the service] then
      print "ACCEPT"
      return zero
4.0 else if [the stub could not connect to the service] then
   4. 1 if [the stub could not connect due to reasons closely related to TLS/SSL (certificate, cipher suites, etc..)] then
          print "REJECT"
          return zero
   4.2  else (the stub could not connect due to reasons unrelated to TLS/SSL (Name resolution, etc..))
          goto "fatal error" (5.0, see one line below for more info)
5.0 else ("fatal error occured")
      (optional error message)
      return value other than zero
</pre>
---

### Testing the stub

To test that the stub works as it should you can perform couple of
easy tests by running it on command line (stub is named `run.test`
in these examples).

Running the program without any arguments should give error message and exit with value other than zero:

```sh
$ run.test
<This should print some kind of (helpful) error message>
```

Connecting to `google.com` on HTTPS port should be success and exit with value zero:

```sh
$ run.test google.com 443
ACCEPT
```

Connecting to `badssl.com`'s `untrusted-root` should be failure and exit with value zero:

```sh
$ run.test untrusted-root.badssl.com 443
REJECT
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
$ run.test google.com 443 ca-bundle.pem
ACCEPT
```

---

### Packaging

A stub should be confined to a directory named in a way that describes the
chosen target language and library or service, e.g. `<language>-<library>`.

A stub should have a top level `README.md` which describes how to run the stub and
how to install the potential dependancies needed.

The stubs should have a `run` command with optional and approriate file
extension for the language in question.

Optionally a stub can have a `Dockerfile` that encapsulates the environment
and the dependancies needed to run the example.

Ideally, one should also include a `results.md` that contains the result of a test run as follows:

```
platform: Linux (Ubuntu 16.04)
runner: trytls 0.1.0 (CPython 2.7.11+, OpenSSL 1.0.2g-fips)
stub: python 'stubs/python-urllib2/run.py'
 PASS expired certificate [reject expired.badssl.com:443]
 PASS wrong hostname in certificate [reject wrong.host.badssl.com:443]
 PASS self-signed certificate [reject self-signed.badssl.com:443]
 ...
```

---

### Stubs tested in each release

In Ubuntu 16.04

* python2-requests
* python2-urllib2
* python3-urllib
* go-nethttp
* java-https
* java-net

### Other stubs

* CSharp-Net
* c-libressl
* haskell-wreq
* FSharp-Net
* c-openssl
* dotnet-https
* 3VB-Net
* erlang-httpc
* lua5.1-luasec
* bash-curl
* php-file-get-contents
* bash-opensslSClient
* haskell-http-client-tls
* python2-idiokit

### Acceptance process:

1. Author:
   * Contact the author
* License:
   * Author agrees with the license?
* Contribution list:
   * Author's name on the contributions list
* Specs:
   * Calling convention
* Stub works:
   * Does it?
* Docs + dependencies:
   * Deps documented?
   * **Run** + **Install**
*  Results:
   * results.txt
* Findings + What to do?
   * Pass/ fail ->
      * Ignore?, Writeup?, Upstream?

