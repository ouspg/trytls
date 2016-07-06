#BadSSL services and reasons for usage/ignore

##Used

* expired: obsolete cert should not be valid
* wrong.host: wrong host should not be valid
* self-signed: who knows who signed? should not be valid
* sha256: should be valid to future proof
* 1000-sans: massive alternative names should be valid
* incomplete-chain: cert should have full proof of chain to trusted CA and hence this should not be valid
* superfish: super fishy CA should not be valid
* edellroot: rotten roots CA should not be valid
* dsdtestprovider: unproviding CA should not be valid

##Unused

* 10000-sans: massive-er alternative names, useful only for possible futureproofing
* pinning-test: only for Chrome
* rest of tests: out of scope (???)
