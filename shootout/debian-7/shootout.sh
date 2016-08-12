#!/bin/sh
VERSION=0.2.1

cat <<EOF
# TryTLS testing with Debian 7

\`\`\`console

# cat /etc/debian_version
EOF

cat /etc/debian_version

cat <<EOF

\`\`\`

## Python 2

The stub will be executed with python2.7, as that launches the version provided
by the distribution. python3.5 was manually installed for executing the
TryTLS runner itself (not the stub).

\`\`\`console
# python --version
EOF
python --version

cat <<EOF
\`\`\`

### python-requests

\`\`\`console

# trytls https python2.7 trytls-${VERSION}/stubs/python-requests/run.py
EOF

trytls https python2.7 trytls-${VERSION}/stubs/python-requests/run.py

cat <<EOF

\`\`\`

### python-urllib2

\`\`\`console

# trytls https python2.7 trytls-${VERSION}/stubs/python-urllib2/run.py
EOF

trytls https python2.7 trytls-${VERSION}/stubs/python-urllib2/run.py

cat <<EOF

\`\`\`

## Python 3

The stub will be executed with python3.2, as that launches the version provided
by the distribution. python3.5 was manually installed for executing the
TryTLS runner itself (not the stub).

\`\`\`console

# python3.2 --version
EOF
python3.2 --version

cat <<EOF

\`\`\`

<!-- markdownlint-disable MD024 -->

### python-requests

<!-- markdownlint-enable MD024 -->

\`\`\`console

# trytls https python3.2 trytls-${VERSION}/stubs/python-requests/run.py
EOF

trytls https python3.2 trytls-${VERSION}/stubs/python-requests/run.py
cat <<EOF

\`\`\`

### python-urllib

\`\`\`console

# trytls https python3.2 trytls-${VERSION}/stubs/python3-urllib/run.py
EOF

trytls https python3.2 trytls-${VERSION}/stubs/python3-urllib/run.py

cat <<EOF

\`\`\`

## Java

\`\`\`console
java -version
EOF
java -version

cat <<EOF

\`\`\`

### java-https

\`\`\`console

# trytls https java -classpath trytls-${VERSION}/stubs/java-https/ Run
EOF

trytls https java -classpath trytls-${VERSION}/stubs/java-https/ Run

cat <<EOF

\`\`\`

### java-net

\`\`\`console

# trytls https java -classpath trytls-${VERSION}/stubs/java-net/ Run
EOF

trytls https java -classpath trytls-${VERSION}/stubs/java-net/ Run

cat <<EOF

\`\`\`

## Go

\`\`\`console

# go version
EOF

go version

cat <<EOF

\`\`\`

### go-nethttp

\`\`\`console

# trytls https go run trytls-${VERSION}/stubs/go-nethttp/run.go
EOF

trytls https go run trytls-${VERSION}/stubs/go-nethttp/run.go

cat <<EOF

\`\`\`

## PHP

\`\`\`console
php -v
EOF
php -v

cat <<EOF

\`\`\`

### php-file-get-contents

\`\`\`console
# trytls https php trytls-${VERSION}/stubs/php-file-get-contents/run.php
EOF

trytls https php trytls-${VERSION}/stubs/php-file-get-contents/run.php

cat <<EOF

\`\`\`
EOF
