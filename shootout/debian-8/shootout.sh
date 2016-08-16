#!/bin/sh
VERSION=0.3.0

# 002

cat <<EOF
# TryTLS testing with Debian 8

\`\`\`console

# cat /etc/debian_version
EOF

cat /etc/debian_version

cat <<EOF

\`\`\`

\`\`\`console
# python --version
EOF
python --version

cat <<EOF
\`\`\`

## python-requests

\`\`\`console

# trytls https python trytls-${VERSION}/stubs/python2-requests/run.py
EOF

trytls https python trytls-${VERSION}/stubs/python2-requests/run.py

cat <<EOF

\`\`\`

## python-urllib2

\`\`\`console

# trytls https python trytls-${VERSION}/stubs/python2-urllib2/run.py
EOF

trytls https python trytls-${VERSION}/stubs/python2-urllib2/run.py

cat <<EOF

\`\`\`

\`\`\`console

# python3 --version
EOF
python3 --version

cat <<EOF

\`\`\`

## python3-urllib

\`\`\`console

# trytls https python3 trytls-${VERSION}/stubs/python3-urllib/run.py
EOF

trytls https python3 trytls-${VERSION}/stubs/python3-urllib/run.py

cat <<EOF

\`\`\`

## Java

\`\`\`console
java -version
EOF
java -version

cat <<EOF

\`\`\`

## java-https

\`\`\`console

# trytls https java -classpath trytls-${VERSION}/stubs/java-https/ Run
EOF

trytls https java -classpath trytls-${VERSION}/stubs/java-https/ Run

cat <<EOF

\`\`\`

## java-net

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

## go-nethttp

\`\`\`console

# trytls https go run trytls-${VERSION}/stubs/go-nethttp/run.go
EOF

trytls https go run trytls-${VERSION}/stubs/go-nethttp/run.go

cat <<EOF

\`\`\`

### php-file-get-contents

\`\`\`console
php -v
EOF
php -v

cat <<EOF

\`\`\`console
# trytls https php trytls-${VERSION}/stubs/php-file-get-contents/run.php
EOF

trytls https php trytls-${VERSION}/stubs/php-file-get-contents/run.php

cat <<EOF

\`\`\`
EOF
