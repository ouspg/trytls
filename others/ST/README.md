## Get started

```
$ ./st <<command> <file>> [ca-bundle]
```


### Examples

```

$ ./st "python3 ../trytls/stubs/python3-urllib/run.py"
ok!

$ ./st "python3 ../trytls/stubs/python3-urllib/run.py" "/etc/ssl/certs/ca-certificates.crt"
ok!

$ ./st ../trytls/stubs/c-openssl/run
HOX! the stub does not support being without ca-bundles
stub UNSUPPORTS calling convention, you sure it is working correctly?
There were some errors

$ ../trytls/others/ST/st "java Run" /etc/ssl/certs/ca-certificates
HOX! the stub does not support ca-bundles
ok!


$ ./st ../trytls/stubs/c-openssl/run /etc/ssl/certs/ca-certificates
ok!

$ ../trytls/others/ST/st "java Run"
ok!

$ ./st "python3 ../trytls/stubs/test/i-do-not-work.py" "/etc/ssl/certs/ca-certificates.crt"
"stub exited with value 0 even though it should not have (too few arguments)"

$ ./st "python3 ../trytls/stubs/python3-urllib/run.p"
No such file found: /home/klasila/Työpöytä/git-repos/trytls/stubs/python3-urllib/run.p



```
