# TryTLS shootouts

## 0.2 shootout results

We ran TryTLS tests on major and still supported distributions.
For this shootout we limited ourselves to the official Docker images
of the distributions. Our objective was to check that the bundled
languages and libraries are safe to use with TLS. TryTLS focuses
on making sure that the certificates are checked properly.

### Main Observations

* The same Python code produced different results in different distributions.
  Due to this, we should reach out Python gurus, are we doing something wrong
  or is running apparently correct Python code in some major distributions
  actually dangerous.

* Java stubs had issues we need to investigate and possibly fix before next
  shootout. Due to this, some Java results are not available.

* We were surprised to see the lack of SNI support in many of the still
  supported distributions. In next study we might investigate SNI support
  separately to get more directly security related results.

### Results

Detailed results are available in subdirectories. Summarised results are in the
table below.

<!-- markdownlint-disable MD013 -->

| OS                             | python-requests | python-urllib2 | python3-urllib | go-nethttp   | java-https | java-net | php-file-get-contents  |
|------------------------------- | --------------- | -------------- | -------------- | ------------ | ---------- | ---------|------------------------|
|[Alpine 3.1](alpine-3.1)        | FAIL            | FAIL           | N/A            | PASS         | NO SNI     | NO SNI   | NO SNI |
|[Alpine Edge](alpine-edge)      | FAIL            | FAIL           | FAIL           | PASS         | PASS       | PASS     | NO SNI |
|[CentOS 5.11](centos5)          | N/A             | N/A            | N/A            | N/A          | N/A        | N/A      | N/A    |
|[CentOS 6.8](centos6)           | NO SNI          | N/A            | PASS           | PASS         | N/A        | N/A      | NO SNI |
|[CentOS 7.2](centos7)           | PASS            | FAIL           | PASS           | PASS         | N/A        | N/A      | NO SNI |
|[Debian 7.11](debian-7)         | NO SNI          | N/A            | FAIL           | N/A          | N/A        | N/A      | NO SNI |
|[Debian 8.5](debian-8)          | PASS            | PASS           | FAIL           | PASS         | N/A        | N/A      | PASS   |
|[Fedora 24](fedora24)           | PASS            | PASS           | N/A            | PASS         | PASS       | PASS     | PASS   |
|[Ubuntu 12.04.5](ubuntu-12.04)  | NO SNI          | N/A            | FAIL           | NO SNI       | N/A        | N/A      | NO SNI |
|[Ubuntu 14.04.5](ubuntu-14.04)  | NO SNI          | N/A            | FAIL           | NO SNI       | N/A        | N/A      | NO SNI |
|[Ubuntu 16.04.1](ubuntu-16.04)  | PASS            | PASS           | PASS           | PASS         | PASS       | PASS     | PASS   |

Legend:

* PASS: None of the verdicts belong to any of the other categories
* FAIL: One or more tests failed, e.g. the implementation acted against
  expectation. For example the library establishes connection, even though
   it should not.
* NO SNI: SNI not supported
* N/A: test subject was not available in target distribution, or stub behavior
  requires investigation
