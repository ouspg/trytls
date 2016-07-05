##Info

This is to be a part of the maybe to be runner.
This can also be ran itself.

#Get started

##Installation:

```console
Make sure you have bash installed
```
usage:
```console
$ bash run <language> <stub> <conf> [certs]
```


##Example usage:

against badssl
```console
$ bash run python3 '../trytls/stubs/python3-urllib/run.py' 'conf/const/badssl_https_conf'
...
```

agains trytls backend
```console
$ bash run python3 '../trytls/stubs/python3-urllib/run.py' '../trytls/backends/trytls/tmp/conf' ../trytls/backends/trytls/tmp/certs
...
```




