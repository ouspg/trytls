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
# TryTLS testing with Alpine

We chose Alpine 3.6 release for this TryTLS-shootout
based on the [Alpine Releases](https://wiki.alpinelinux.org/wiki/Alpine_Linux:Releases).

\`\`\`console
docker run -ti --rm alpine-3.6
\`\`\`

EOF

myrun \# cat /etc/os-release


cat <<EOF
<!-- markdownlint-disable MD013 -->

python2-requests | python2-urllib2 | python3-urllib | go-nethttp | java-https | java-net | php-file-get-contents
---------------- | --------------- | -------------- | ---------- | ---------- | -------- | ---------------------
?                | ?               | ?              | ?          | ?          | ?        | ?

## python2-requests

EOF

myrun \# python --version
myrun \# trytls https python python2-requests/run.py


cat <<EOF
## python2-urllib2

EOF

myrun \# python --version
myrun \# trytls https python python2-urllib2/run.py

cat <<EOF
## python3-urllib

EOF

myrun \# python3 --version
myrun \# trytls https python3 python3-urllib/run.py

cat <<EOF
## go-nethttp

EOF

myrun \# go version
myrun \# trytls https go-nethttp/run

cat <<EOF
## java-https

EOF

myrun \# java -version
myrun \# trytls https java -classpath java-https Run

cat <<EOF
## java-net

EOF

myrun \# java -version
myrun \# trytls https java -classpath java-net Run

cat <<EOF
## php-file-get-contents

EOF

myrun \# php5 --version | sed -e 's/ *$//'
myrun \# trytls https php5 php-file-get-contents/run.php

cat <<EOF
<!-- markdownlint-enable MD013 -->
EOF
