##Info

This is to be a part of the maybe to be runner.
This can also be ran itself.

#Get started

##Installation:

```console
-> edit sr(-script) as instructed inside of it
-> cp sr ../bin/ if you want to
```

usage(run-script):
```console
$ bash run <language> <stub> <conf> [certs] [curpath] [stubname] [timeout(in seconds)]

if ( you want to set some of the aguments to default) {
  replace the arguments with '_' characters.
}
```

usage(sr-script):
```console
$ sr <certspath> <command> <run-path> <stub> <backends>
```

##Example usage:

### sr-script (simplerunner)

```
example 1:
$ cd ../stubs/[stub]              #move to the stub folder you want to run
$ sr                              #execute sr-script -> run simplerunner against default backends

example 2:
$ sr -- -- -- -- trytls-localhost

example 3:
$ sr -- java -- -- java-https:Run badssl-all

example 4(for example: linux, c-openssl):
$ sr /etc/ssl/certs/ca-certificates.crt

```


### Run-script (run, sr and bashtls use this)


against badssl (run the code on your computer and you will see the colorcoded version)
* Green/Blue = Good
* Red = Bad
* White = Middle/OK?
* Others = Can't say (but not bad, either good or middle)

```console
$ bash run mono '../trytls/stubs/cSharp-Net/run.exe' 'conf/badssl-all' _ _ CSharp-Net | sort

[cSharp-Net][ PASS ][VERIFY FAILURE][ dh480                         ][dh480.badssl.com]
[cSharp-Net][ PASS ][VERIFY FAILURE][ dsdtestprovider               ][dsdtestprovider.badssl.com]
[cSharp-Net][ PASS ][VERIFY FAILURE][ edellroot                     ][edellroot.badssl.com]
[cSharp-Net][ PASS ][VERIFY FAILURE][ self-signed                   ][self-signed.badssl.com]
[cSharp-Net][ PASS ][VERIFY FAILURE][ superfish                     ][superfish.badssl.com]
[cSharp-Net][ PASS ][VERIFY FAILURE][ untrusted-root                ][untrusted-root.badssl.com]
[cSharp-Net][ PASS ][VERIFY FAILURE][ wrong host                    ][wrong.host.badssl.com]
[cSharp-Net][ PASS ][VERIFY SUCCESS][ sha-256                       ][sha256.badssl.com]
[cSharp-Net][ PASS ][VERIFY SUCCESS][ supports SNI                  ][badssl.com]
[cSharp-Net][ OK?  ][ UNSUPPORTED  ][ disable ca-bundles            ][badssl.com]
[cSharp-Net][ OK?  ][VERIFY FAILURE][ dh1024                        ][dh1024.badssl.com]
[cSharp-Net][ OK?  ][VERIFY FAILURE][ dh-small-subgroup             ][dh-small-subgroup.badssl.com]
[cSharp-Net][ OK?  ][VERIFY FAILURE][ incomplete-chain              ][incomplete-chain.badssl.com]
[cSharp-Net][ OK?  ][VERIFY FAILURE][ mozilla-intermediate          ][mozilla-intermidiate.badssl.com]
[cSharp-Net][ OK?  ][VERIFY FAILURE][ mozilla-modern                ][mozilla-modern.badssl.com]
[cSharp-Net][ OK?  ][VERIFY FAILURE][ subdomain.preloaded-hsts      ][subdomain.preloaded-hsts.badssl.com]
[cSharp-Net][ OK?  ][VERIFY SUCCESS][ cbc                           ][cbc.badssl.com]
[cSharp-Net][ OK?  ][VERIFY SUCCESS][ hsts                          ][hsts.badssl.com]
[cSharp-Net][ OK?  ][VERIFY SUCCESS][ mixed                         ][mixed.badssl.com]
[cSharp-Net][ OK?  ][VERIFY SUCCESS][ mixed-favicon                 ][mixed-favicon.badssl.com]
[cSharp-Net][ OK?  ][VERIFY SUCCESS][ mixed-script                  ][mixed-script.badssl.com]
[cSharp-Net][ OK?  ][VERIFY SUCCESS][ mozilla-old                   ][mozilla-old.badssl.com]
[cSharp-Net][ OK?  ][VERIFY SUCCESS][ pinning-test                  ][pinning-test.badssl.com]
[cSharp-Net][ OK?  ][VERIFY SUCCESS][ preloaded-hsts                ][preloaded-hsts.badssl.com]
[cSharp-Net][ OK?  ][VERIFY SUCCESS][ rc4                           ][rc4.badssl.com]
[cSharp-Net][ OK?  ][VERIFY SUCCESS][ rsa8192                       ][rsa8192.badssl.com]
[cSharp-Net][ OK?  ][VERIFY SUCCESS][ sha1-2016                     ][sha1-2016.badssl.com]
[cSharp-Net][ OK?  ][VERIFY SUCCESS][ sha1-2017                     ][sha1-2017.badssl.com]
[cSharp-Net][ OK?  ][VERIFY SUCCESS][ upgrade                       ][upgrade.badssl.com]
[cSharp-Net][ OK?  ][VERIFY SUCCESS][ very                          ][very.badssl.com]
[cSharp-Net][ FAIL ][VERIFY FAILURE][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
[cSharp-Net][ FAIL ][VERIFY FAILURE][ 1000-sans                     ][1000-sans.badssl.com]
[cSharp-Net][ FAIL ][VERIFY FAILURE][ dh2048                        ][dh2048.badssl.com]
[cSharp-Net][ FAIL ][VERIFY SUCCESS][ expired                       ][expired.badssl.com]


...
```

agains trytls backend
```console
$ bash run python3 '../trytls/stubs/python3-urllib/run.py' '../trytls/backends/trytls/tmp/conf' ../trytls/backends/trytls/tmp/certs

or 

$ bash run mono '../trytls/stubs/vb-Net/run.exe' '../trytls/backends/trytls/tmp/conf-nocerts'

or

$ bash run python3 '../trytls/stubs/python3-urllib/run.py' 'conf/trytls-localhost' ../trytls/backends/trytls/tmp/certs
* if 

or

$ bash run mono '../trytls/stubs/FSharp-Net/run.exe' 'conf/trytls-localhost-nocerts'
...
```
