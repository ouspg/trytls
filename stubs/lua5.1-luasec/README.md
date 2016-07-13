# How to run:

lua5.1 run.lua (url) (port) (ca_file)

For example:

```
$ lua5.1 stubs/lua5.1-luasec/run.lua sha256.badssl.com 443
VERIFY FAILURE
```

# Dependencies:

Lua 5.1 or newer installed
Luarocks installed and used to install
* luasec 0.6-1 or newer (`luarocks install luasec` to command line)
* luasocket (`luarocks install luasocket` to command line)

Tested on Ubuntu 16.04
