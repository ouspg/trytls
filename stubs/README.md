## Stubs

Example code (stubs) using TLS in different languages and libraries live in here. 
You can contribute your stub here or just BYOR (Bring Your Own Repository).

These stubs should attempt to use the chosen language and library
properly to establish a secure TLS connection to the given destination.

---

### Calling convention

All stubs should have a standalone program that takes up to three command
line arguments (`<host> <port> [ca-bundle]`):

 * `<host>` is the DNS name or IP-address of the service to connect to
 * `<port>` is the port to connect to
 * `[ca-bundle]` is optional location of the CA certificate bundle to be used
 instead of the built-in default

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

### Packaging

Create new directory: lanugage-library
Name the file that's to be executed as run.x or Run.x.
* x is the normal filename extensions for the chosen language

A stub should have a top level `README.md` that describes how to run the stub. The stubs should have a `run` command.

Optionally a stub can have a `Dockerfile` that encapsulates the environment
and the dependancies needed to run the example.
