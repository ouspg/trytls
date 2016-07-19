#!/bin/sh

stack --version 2>/dev/null
if [ $? -gt 0 ]; then
    echo "Stack not found. Please install https://haskellstack.org/"
    exit 1
fi

set -e

stack build
stack exec test-wreq $*
