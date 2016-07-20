#!/bin/sh

stack --version 2>&1 >/dev/null
if [ $? -gt 0 ]; then
    echo "Stack not found. Please install https://haskellstack.org/"
    exit 1
fi

set -e

stack build
