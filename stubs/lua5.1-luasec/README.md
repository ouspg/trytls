
# How to run:

lua5.1 run.lua <url> <port> [ca_file]

For example:

```
$ lua5.1 stubs/lua5.1-luasec/run.lua sha256.badssl.com 443
REJECT
```

# Dependencies:

Lua 5.1 or newer installed
Luarocks installed and used to install
* luasec 0.6-1 or newer (`luarocks install luasec` to command line)
* luasocket (`luarocks install luasocket` to command line)

Tested on Ubuntu 16.04

# Credits

http://notebook.kulchenko.com/programming/https-ssl-calls-with-lua-and-luasec
https://github.com/brunoos/luasec/pull/49/commits/cde151739e4f7d9262dcea462a2e58d708501ad8

# Luasec License

LuaSec 0.5 license
Copyright (C) 2006-2013 Bruno Silvestre, UFG

Permission is hereby granted, free  of charge, to any person obtaining
a  copy  of this  software  and  associated  documentation files  (the
"Software"), to  deal in  the Software without  restriction, including
without limitation  the rights to  use, copy, modify,  merge, publish,
distribute,  sublicense, and/or sell  copies of  the Software,  and to
permit persons to whom the Software  is furnished to do so, subject to
the following conditions:

The  above  copyright  notice  and  this permission  notice  shall  be
included in all copies or substantial portions of the Software.

THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
