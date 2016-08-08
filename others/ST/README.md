## Get started

```
$ ./st <<command> <file>> [tests] [ca-bundle]

[tests]
  * support   -> test ca-bundle support
  * --          -> all

```


### Examples

```

$ ./st "python3 ../trytls/stubs/python3-urllib/run.py"
ok!

$ ./st "python3 ../trytls/stubs/python3-urllib/run.py" -- "/etc/ssl/certs/ca-certificates.crt"
ok!

$ ./st ../trytls/stubs/c-openssl/run
Error: the stub does not support being without ca-bundles

$ ../trytls/others/ST/st "java Run" -- /etc/ssl/certs/ca-certificates
Error: the stub does not support ca-bundles

$ ./st ../trytls/stubs/c-openssl/run -- /etc/ssl/certs/ca-certificates
ok!

$ ../trytls/others/ST/st "java Run"
ok!

$ ./st "python3 ../trytls/stubs/test/i-do-not-work.py" -- "/etc/ssl/certs/ca-certificates.crt"
"Error: Does not care about the number of parameters, exits always with process value 0"

$ ./st "python3 ../trytls/stubs/python3-urllib/run.py" -- ca-bundle
"Error: no such file or directory: ca-bundle"

$ bash ../trytls/others/ST/st "./run" "support" /etc/ssl/certs/ca-certificates.crt
ok!

$ bash ../trytls/others/ST/st "./run" "support"
Error: the stub does not support being without ca-bundles
There were some errors

$ bash ../trytls/others/ST/st "mono Run.exe" "support" /etc/ssl/certs/ca-certificates.crt
Error: the stub does not support ca-bundles
There were some errors

```
