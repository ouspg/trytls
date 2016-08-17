#!/bin/sh

myrun() {
  echo '```console'
  echo "$@"
  shift 1
  "$@"
  echo '```'
  echo
}

cat <<EOF
# TryTLS testing with Ubuntu

We chose Ubuntu 12.04, 14.04 and 16.04 LTS releases for this TryTLS-shootout
based on the [Ubuntu release end of life](http://www.ubuntu.com/info/release-end-of-life).

EOF

cat <<EOF
<!-- markdownlint-disable MD013 -->

python2-requests | python2-urllib2 | python3-urllib | go-nethttp | java-https | java-net | php-file-get-contents
---------------- | --------------- | -------------- | ---------- | ---------- | -------- | ---------------------
?                | ?               | ?              | ?          | ?          | ?        | ?

## python2-requests

EOF

myrun \# trytls https docker run -i --rm shootout-ubuntu12.04 python /root/stubs/python2-requests/run.py

cat <<EOF
## python2-urllib2

EOF

myrun \# trytls https docker run -i --rm shootout-ubuntu12.04 python /root/stubs/python2-urllib2/run.py

cat <<EOF
## python3-urllib

EOF

myrun \# trytls https docker run -i --rm shootout-ubuntu12.04 python3 /root/stubs/python3-urllib/run.py

cat <<EOF
## go-nethttp

EOF

myrun \# trytls https docker run -i --rm shootout-ubuntu12.04 /root/stubs/go-nethttp/run | expand

cat <<EOF
## java-https

Java too old to compile this stub in Ubuntu 12.04 LTS.

## java-net

Java too old to compile this stub in Ubuntu 12.04 LTS.

EOF

cat <<EOF
## php-file-get-contents

EOF

myrun \# trytls https docker run -i --rm shootout-ubuntu12.04 php /root/stubs/php-file-get-contents/run.php

cat <<EOF
<!-- markdownlint-enable MD013 -->
EOF
