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
# TryTLS testing with Debian 7

\`\`\`console
docker run -ti --rm debian7
\`\`\`

EOF

myrun \# cat /etc/debian_version | sed -e 's/ *$//'

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

myrun \# python3.2 --version
myrun \# trytls https python3 python3-urllib/run.py

cat <<EOF
## go-nethttp

EOF

myrun \# go version
myrun \# trytls https go run go-nethttp/run.go

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

myrun \# php --version | sed -e 's/ *$//'
myrun \# trytls https php php-file-get-contents/run.php

cat <<EOF
<!-- markdownlint-enable MD013 -->
EOF
