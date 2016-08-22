# TryTLS

Does *your* library check TLS certificates properly?
Broken certificate checks seems to be an overlooked issue.
Handling certificates is surprisingly complex, and calls for extra attention.

TryTLS is a tool for the software and library developers, vulnerability
researchers, and end-users, who want to use TLS safely.

We hope to help you to test certificate handling easily. We support
systematic and readily planned tests and try make integrating your
favorite language and library easy.

This is an open source project and anyone can contribute.

---

# What TryTLS Is Not

* We do not address possible client certificate check problems in server code
* We do not do or require a man-in-the-middle tools
* We do not support smart TVs, IoT toasters and other such devices that
  can't run any of the runners

---

# Architecture

![Architecture](https://raw.githubusercontent.com/ouspg/trytls/master/doc/architecture-scaled.jpg)

* **Backends (servers)** provide TLS/SSL tests for stubs (clients).
* **Stubs** attempt to establish secure TLS/SSL connections to backends.
* **Runners** run the stubs against backends and provide the results of the tests.

--simple explanation: Runner tells stub to connect to a backend, stub attempts connection to backend, if the stub connects returns accept, if it does not connect reject or error

---

# Shootouts

We run the TryTLS tests against popular OS distributions and
languages with the latest versions of both the stubs and the runner. We use Docker for repeatability
and ease of reproduction.

We have already had two shootouts, 0.2 and 0.3.
Results and reproduction instructions of these tests are collected
in the shootout documentation in our github repository.

---

# Found issues

## OS X OpenSSL verification surprises

When using native python shipped with OS X, the system default bundle will be
trusted even if instructed otherwise. This is troubling, as some organizations
do not want to trust the default bundles. Also, lately, the reputation of some
CAs have been brought into question.

## Shootout 0.3: Python vulnerabilities

It seems it may be unsafe to do TLS in some of the  common distros.
E.g. the native Python version in the distros varies wildly, and not all fixes have
been backported. In these cases Python still doesn't always have certificate
checking enabled by default. Administrators can use configuration tools to mitigate this somewhat.

---

# Who gave we contacted?

* python-dev: Shootout 0.2 & 0.3 Python vulnerability reveal
* oss-security: Shootout 0.3 Python vulnerability reveal
* Reddit: "Market speech"
 * Python
 * NetSec
 * Information_Security

---
