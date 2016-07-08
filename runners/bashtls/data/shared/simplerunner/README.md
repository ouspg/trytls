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
$ bash run <language> <stub> <conf> [certs] [curpath] [stubname]
```
example:
* language = python3
* stub = ../run.py
* conf = badssl
* certs = ../certs
* curpath = ../simplerunner
* stubname = python3-urllib


##Example usage:

against badssl (run the code on your computer and you will see the colorcoded version)
* Green/Blue = Good
* Red = Bad
* White = Middle/OK?
* Others = Can't say (but not bad, either good or middle)

```console
$ bash run python3 '../trytls/stubs/python3-urllib/run.py' 'conf/const/badssl_https_conf' | sort
python3_1  | [python3-urllib][SUCCESS] VERIFY FAILURE: wrong host [wrong.host.badssl.com]
python3_1  | [python3-urllib][SUCCESS] VERIFY FAILURE: edellroot [edellroot.badssl.com]

...
```

agains trytls backend
```console
$ bash run python3 '../trytls/stubs/python3-urllib/run.py' '../trytls/backends/trytls/tmp/conf' ../trytls/backends/trytls/tmp/certs
...
```
