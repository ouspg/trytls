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
# TryTLS testing with CentOS

We chose centos5, centos6 and centos7 for this TryTLS-shootout
based on the [CentOS End of Support Schedule](https://en.wikipedia.org/wiki/CentOS#End-of-support_schedule).

\`\`\`console
docker run -ti --rm centos6
\`\`\`

EOF

myrun \# cat /etc/redhat-release | sed -e 's/ *$//'

cat <<EOF
<!-- markdownlint-disable MD013 -->

OS         | python2-requests | python2-urllib2 | python3-urllib | go-nethttp | java-https | java-net | php-file-get-contents
---------- | ---------------- | --------------- | -------------- | ---------- | ---------- | -------- | ---------------------
CentOS 6.8 | ?                | ?               | ?              | ?          | ?          | ?        | ?

## python-requests

EOF

myrun \# python --version
myrun \# scl enable rh-python34 "trytls https /usr/bin/python python2-requests/run.py"

cat <<EOF
## python-urllib2

EOF

myrun \# python --version
myrun \# scl enable rh-python34 "trytls https /usr/bin/python python2-urllib2/run.py"

cat <<EOF
## python3-urllib

EOF

myrun \# scl enable rh-python34 "python --version"
myrun \# scl enable rh-python34 "trytls https python python3-urllib/run.py"

cat <<EOF
## go-nethttp

EOF

myrun \# go version
myrun \# scl enable rh-python34 "trytls https go-nethttp/run"

cat <<EOF
## java-https

EOF

myrun \# java -version
myrun \# scl enable rh-python34 "trytls https java -classpath java-https Run"

cat <<EOF
## java-net

EOF

myrun \# java -version
myrun \# scl enable rh-python34 "trytls https java -classpath java-net Run"

cat <<EOF
## php-file-get-contents

EOF

myrun \# php --version | sed -e 's/ *$//'
myrun \# scl enable rh-python34 "trytls https php php-file-get-contents/run.php"

cat <<EOF
<!-- markdownlint-enable MD013 -->
EOF
