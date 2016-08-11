# TryTLS testing with CentOS

We chose centos5, centos6 and centos7 for this TryTLS-shootout
based on the [CentOS End of Support Schedule](https://en.wikipedia.org/wiki/CentOS#End-of-support_schedule).

```console
$ docker run -ti --rm centos6

# cat /etc/redhat-release
CentOS release 5.11 (Final)
```

<!-- markdownlint-disable MD013 -->

OS          | python-requests | python-urllib2 | python3-urllib | go-nethttp | java-https | java-net | php-file-get-contents
---------- | --------------- | -------------- | -------------- | ---------- | ---------- | -------- | ---------------------
CentOS 5.11 | N/A            | N/A            | N/A            | N/A        | N/A        | N/A      | N/A

## python-requests

No python 2.7+ or 3+ which are required to run the TryTLS runner.

## python-urllib2

No python 2.7+ or 3+ which are required to run the TryTLS runner.

## python3-urllib

No Python 3 available for CentOS 5.

## go-nethttp

No Go in CentOS 5.

## java-https

Java too old to compile this stub in CentOS 5.

## java-net

Java too old to compile this stub in CentOS 5.

## php-file-get-contents

No python 2.7+ or 3+ which are required to run the TryTLS runner.

<!-- markdownlint-enable MD013 -->
