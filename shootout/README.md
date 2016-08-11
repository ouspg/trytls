# Directory for shootout results

## 0.2 shootout results (WIP)

To reach the status "PASS", the implementation must meet the following criteria:

<!-- markdownlint-disable MD013 -->

* ERROR: should not be present in any of the tests verdicts
  (ERROR means bug in stub or some other issue),
* FAIL: should not be present in any of the tests
  (exmample: the library establishes connection even though it should not),
* NO SNI:  SNI support should exists, and
* N/A: the library should be available to install from the distribution's
  package manager.

| OS         | python-requests | python-urllib2 | python3-urllib | (python3) python-requests | go-nethttp   | java-https | java-net | php-file-get-contents  |
|---------- | --------------- | -------------- | -------------- | --------------------------| ------------ | ---------- | ---------|------------------------|
|Alpine 3.1  | PASS            | PASS           | N/A            | N/A                       | PASS         | ERROR(2)   | ?        | NO SNI |
|Alpine Edge | PASS            | PASS           | PASS           | PASS                      | PASS         | PASS       | PASS     | NO SNI |
|CentOS 5.11 | N/A             | N/A            | N/A            | N/A                       | N/A          | N/A        | N/A      | N/A    |
|CentOS 6.8  | NO SNI          | ERROR          | PASS           | N/A                       | PASS         | ERROR(1)   | ERROR(1) | NO SNI |
|CentOS 7.2  | PASS            | FAIL           | PASS           | N/A                       | PASS         | ERROR(1)   | ERROR(1) | NO SNI |
|Debian 8.5  | PASS            | PASS           | FAIL           | PASS                      | ERROR(1)     | ERROR(1)   | ERROR(1) | PASS   |
|Fedora 24   | PASS            | PASS           | ?              | PASS                      | PASS         | PASS       | PASS     | PASS   |
