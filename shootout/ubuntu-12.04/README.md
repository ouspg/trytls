# TryTLS testing with CentOS

We chose Ubuntu 12.04, 14.04 and 16.04 LTS releases for this TryTLS-shootout
based on the [CentOS End of Support Schedule](http://www.ubuntu.com/info/release-end-of-life).

```console
$ docker run -ti --rm ubuntu-12.04

# grep DISTRIB_DESCRIPTION /etc/lsb-release
DISTRIB_DESCRIPTION="Ubuntu 12.04.5 LTS"
```

<!-- markdownlint-disable MD013 -->

OS                 | python-requests | python-urllib2 | python3-urllib | go-nethttp | java-https | java-net | php-file-get-contents
------------------ | --------------- | -------------- | -------------- | ---------- | ---------- | -------- | ---------------------
Ubuntu 12.04.5 LTS | ?               | ?              | ?              | ?          | N/A        | N/A      | ?

## python-requests

```console
# python --version
Python 2.7.3

# trytls https python python-requests/run.py
FIXME
```

## python-urllib2

```console
# python --version
Python 2.7.3

# trytls https python python-urllib2/run.py
FIXME

```

## python3-urllib

```console
# python3 --version
Python 3.2.3

# trytls https python3 python3-urllib/run.py
FIXME
```

## go-nethttp

```console
# go version
go version go1

# trytls https go-nethttp/run
FIXME
```

## java-https

Java too old to compile this stub in Ubuntu 12.04 LTS.

## java-net

Java too old to compile this stub in Ubuntu 12.04 LTS.

## php-file-get-contents

```console
# php --version
PHP 5.3.10-1ubuntu3.24 with Suhosin-Patch (cli) (built: Aug  1 2016 20:32:15)
Copyright (c) 1997-2012 The PHP Group
Zend Engine v2.3.0, Copyright (c) 1998-2012 Zend Technologies

# trytls https php php-file-get-contents/run.php
FIXME
```

<!-- markdownlint-enable MD013 -->
