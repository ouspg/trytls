##Info

This is to be a part of the maybe to be runner.
This can also be ran itself.

#Get started

##Installation:

```console
Make sure you have bash installed.
You can't run stubs for which you do not have the needed dependencies installed on your computer.
```
usage:
```console
$ bash run <language> <stub> <conf> [certs]
```


##Example usage:

against badssl (run the code on your computer and you will see the colorcoded version)
* Green/Blue = Good
* Red = Bad
* White = Middle
```console
$ bash run python3 '../trytls/stubs/python3-urllib/run.py' 'conf/const/badssl_https_conf' | sort
VERIFY FAILURE: dsdtestprovider 
VERIFY FAILURE: edellroot 
VERIFY FAILURE: expired 
...
```

agains trytls backend
```console
$ bash run python3 '../trytls/stubs/python3-urllib/run.py' '../trytls/backends/trytls/tmp/conf' ../trytls/backends/trytls/tmp/certs
...
```




