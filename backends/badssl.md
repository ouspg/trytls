# BadSSL services and reasons for usage/ignore

## Used

* `expired`: Expired cert should not be valid
* `wrong.host`: Wrong host should not be valid
* `self-signed`: Who knows who signed? Should not be valid
* `sha256`: Should be valid to future proof
* `1000-sans`: Massive amount of alternative names should be valid
* `incomplete-chain`: Cert should have full proof of chain to trusted CA and hence this should not be valid
* `superfish`: Super fishy CA should not be valid
* `edellroot`: Rotten roots CA should not be valid
* `dsdtestprovider`: Unproviding CA should not be valid

## Unused

* `sha1-2016`: Maybe invalid after 2016
* `sha1-2017`: Maybe invalid after 2017
* `10000-sans`: Gargantuan amount of alternative names, it is useful only for possible futureproofing if valid
* `rsa8192`: Not compulsory, but if one wants to future proof, make valid
* `pinning-test`: Should be invalid, but only used for Chrome
* **other tests**: Out of scope
