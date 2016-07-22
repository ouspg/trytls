#!/bin/sh

stack --version 2>&1 >/dev/null
if [ $? -gt 0 ]; then
    echo "Stack not found. Please install https://haskellstack.org/"
    echo "Then run ./build.sh"
    exit 1
fi

set -e

stack exec test-http-client-tls $*
