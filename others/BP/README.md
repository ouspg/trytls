# Usage:

## Intro

This script can be used with trytls-runner.
It allows you to run also the stubs that cannot be ran without ca-bundle.
Currently (for example):
  * lua5.1-luasec
  * c-openssl

## Setup

Move the bp-script into /bin folder.

```
$ trytls https bp "python3 run.py" /etc/ssl/certs/ca-certificates.crt
...

$ trytls https bp "lua5.1 run.lua" /etc/ssl/certs/ca-certificates.crt
...
```
