# Directory for shootout results

## 0.2 shootout (WIP)

 <!-- markdownlint-disable MD013 -->

 OS         | python-requests | python-urllib2 | python3-urllib | (python3) python-requests | go-nethttp   | java-https | java-net | php-file-get-contents  |
 ---------- | --------------- | -------------- | -------------- | --------------------------| ------------ | ---------- | ---------|------------------------|
Alpine 3.1  | PASS            | PASS           | N/A            | N/A                       | PASS         | ERROR(2)   | ?        | NO SNI
Alpine Edge | PASS            | PASS           | PASS           | PASS                      | PASS         | PASS       | PASS     | NO SNI
CentOS 7.2  | PASS            | FAIL           | PASS           | N/A                       | PASS         | ERROR(1)   | ERROR(1) | NO SNI
Debian 8.5  | PASS            | PASS           | FAIL           | PASS                      | ERROR(1)     | ERROR(1)   | ERROR(1) |
Fedora 24   | PASS            | PASS           | ?              | PASS                      | PASS         | PASS       | PASS     | PASS
