# Directory for shootout results

## 0.2 shootout results (WIP)

To reach the status "PASS", the implementation must meet the following criteria:

<!-- markdownlint-disable MD013 -->

* ERROR: should not be present in any of the test verdicts
  (ERROR means bug in stub or some other issue),
* FAIL: should not be present in any of the test verdicts
  (exmample: the library establishes connection even though it should not),
* NO SNI:  SNI support should exists, and
* N/A: the library should be available to install from the distribution's
  package manager.

| OS                        | python-requests | python-urllib2 | python3-urllib | (python3) python-requests | go-nethttp   | java-https | java-net | php-file-get-contents  |
|---------------------------| --------------- | -------------- | -------------- | --------------------------| ------------ | ---------- | ---------|------------------------|
|[Alpine 3.1](alpine-3.1)   | PASS            | PASS           | N/A            | N/A                       | PASS         | ERROR(2)   | ?        | NO SNI |
|[Alpine Edge](alpine-edge) | PASS            | PASS           | PASS           | PASS                      | PASS         | PASS       | PASS     | NO SNI |
|[CentOS 5.11](centos5) | N/A             | N/A            | N/A            | N/A                       | N/A          | N/A        | N/A      | N/A    |
|[CentOS 6.8](centos6)  | NO SNI          | ERROR          | PASS           | N/A                       | PASS         | ERROR(1)   | ERROR(1) | NO SNI |
|[CentOS 7.2](centos7)  | PASS            | FAIL           | PASS           | N/A                       | PASS         | ERROR(1)   | ERROR(1) | NO SNI |
|[Debian 8.5](debian-latest) | PASS            | PASS           | FAIL           | PASS                      | ERROR(1)     | ERROR(1)   | ERROR(1) | PASS   |
|[Fedora 24](fedora)   | PASS            | PASS           | ?              | PASS                      | PASS         | PASS       | PASS     | PASS   |
|[Ubuntu 16.04](ubuntu/16.04)| PASS            | PASS           | PASS           | N/A                       | PASS         | PASS       | PASS     | PASS   |
|[Ubuntu 14.04](ubuntu/14.04)| PASS            | PASS           | FAIL           | N/A                       | ?            | PASS       | PASS     | N/A    |
|[Ubuntu 12.04.5](ubuntu/12.04.5)| NO SNI        | N/A            | FAIL           | N/A                       | ?            | ERROR      | ERROR    | N/A    |
