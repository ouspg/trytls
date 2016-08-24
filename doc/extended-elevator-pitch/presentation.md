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
https://github.com/ouspg/trytls

---

# What TryTLS Is Not

* We do not address possible client certificate check problems in server code
* We do not do or require a man-in-the-middle tools
* We do not support smart TVs, IoT toasters and other such devices that
  can't run any of the runners

---

# Architecture

![Architecture](https://raw.githubusercontent.com/ouspg/trytls/master/doc/concept-pic.png)

* **Backends (servers)** provide TLS/SSL tests for stubs (clients).
* **Stubs** attempt to establish secure TLS/SSL connections to backends.
* **Runners** run the stubs against backends and provide the results of the tests.

---

# Shootouts

We run the TryTLS tests against popular OS distributions and
languages with the latest versions of both the stubs and the runner. We use Docker for repeatability
and ease of reproduction.

We have already had two shootouts, 0.2 and 0.3.
Results and reproduction instructions of these tests are collected
in the shootout documentation in our Github repository.

---

# Shootout example: SNI support

| OS                             | python2-requests | python2-urllib2 | python3-urllib | go-nethttp   | java-https | java-net | php-file-get-contents  |
|------------------------------- | ---------------- | --------------- | -------------- | ------------ | ---------- | -------- | ---------------------- |
|[Alpine 3.1](alpine-3.1)        | YES              | YES             | N/A            | YES          | NO         | NO       | NO                     |
|[Alpine Edge](alpine-edge)      | YES              | YES             | YES            | YES          | YES        | YES      | NO                     |
|[CentOS 5.11](centos5)          | N/A              | N/A             | N/A            | N/A          | N/A        | N/A      | NO                     |
|[CentOS 6.8](centos6)           | NO               | N/A             | YES            | YES          | YES        | YES      | NO                     |
|[CentOS 7.2](centos7)           | YES              | YES             | YES            | YES          | YES        | YES      | NO                     |
|[Debian 7.11](debian-7)         | NO               | N/A             | YES            | NO           | YES        | YES      | NO                     |
|[Debian 8.5](debian-8)          | YES              | YES             | YES            | YES          | YES        | YES      | YES                    |
|[Fedora 24](fedora24)           | YES              | YES             | YES            | YES          | YES        | YES      | YES                    |
|[Ubuntu 12.04.5](ubuntu-12.04)  | N/A              | N/A             | YES            | N/A          | N/A        | N/A      | NO                     |
|[Ubuntu 14.04.5](ubuntu-14.04)  | NO               | N/A             | YES            | N/A          | YES        | YES      | NO                     |
|[Ubuntu 16.04.1](ubuntu-16.04)  | YES              | YES             | YES            | YES          | YES   

---

# Found issues

## OS X OpenSSL verification surprises

When using native Python shipped with OS X, the system default bundle will be
trusted even if instructed otherwise. This is troubling, as some organizations
do not want to trust the default bundles. Also, lately, the reputation of some
CAs have been brought into question.

## Shootout 0.3: Python vulnerabilities

It seems it may be unsafe to do TLS in some of the  common distros.
E.g. the native Python version in the distros varies wildly, and not all fixes have
been backported. In these cases Python still doesn't always have certificate
checking enabled by default. Administrators can use configuration tools to mitigate this somewhat.

---

# Who have we contacted?

* python-dev: Shootout 0.2 & 0.3 Python vulnerability reveal
* oss-security: Shootout 0.3 Python vulnerability reveal
* University of Michigan
* Software Engineering Institute
* Reddit: "Market speech"
 * Python
 * NetSec
 * Information_Security
