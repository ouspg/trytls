**Python 3.4.3**

driver: python3-ubuntu-14.04
https://github.com/ouspg/trytls/blob/e8d4ffabeb4cfdb206e9802e5ea19fc01113d418/runners/bashtls/drivers/python3-ubuntu-14.04/Dockerfile

<pre>
ubuntu:14.04
RUN apt-get -y update && \
  apt-get -y install \
  python3
</pre>

<pre>
1. urllib.request.urlopen("https://" + host + ":" + port, cafile=cafile, cadefault=False)
2. urllib.request.urlopen("https://" + host + ":" + port, cafile=cafile)
3. urllib.request.urlopen("https://" + host + ":" + port)

python3-ubuntu-14.04_1  | [python3-urllib:run.py][ PASS ][ACCEPT][ supports SNI                  ][badssl.com]
python3-ubuntu-14.04_1  | [python3-urllib:run.py][ FAIL ][ACCEPT][ expired                       ][expired.badssl.com]
python3-ubuntu-14.04_1  | [python3-urllib:run.py][ FAIL ][ACCEPT][ wrong host                    ][wrong.host.badssl.com]
python3-ubuntu-14.04_1  | [python3-urllib:run.py][ FAIL ][ACCEPT][ self-signed                   ][self-signed.badssl.com]
python3-ubuntu-14.04_1  | [python3-urllib:run.py][ PASS ][ACCEPT][ sha-256                       ][sha256.badssl.com]
python3-ubuntu-14.04_1  | [python3-urllib:run.py][ PASS ][ACCEPT][ 1000-sans                     ][1000-sans.badssl.com]
python3-ubuntu-14.04_1  | [python3-urllib:run.py][ FAIL ][REJECT][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
python3-ubuntu-14.04_1  | [python3-urllib:run.py][ FAIL ][ACCEPT][ incomplete-chain              ][incomplete-chain.badssl.com]
python3-ubuntu-14.04_1  | [python3-urllib:run.py][ OK?  ][ACCEPT][ pinning-test                  ][pinning-test.badssl.com]
python3-ubuntu-14.04_1  | [python3-urllib:run.py][ FAIL ][ACCEPT][ superfish                     ][superfish.badssl.com]
python3-ubuntu-14.04_1  | [python3-urllib:run.py][ FAIL ][ACCEPT][ edellroot                     ][edellroot.badssl.com]
python3-ubuntu-14.04_1  | [python3-urllib:run.py][ FAIL ][ACCEPT][ dsdtestprovider               ][dsdtestprovider.badssl.com]
python3-ubuntu-14.04_1  | [python3-urllib:run.py][ PASS ][REJECT][ disable ca-bundles            ][badssl.com]
</pre>

<pre>
1. urllib.request.urlopen("https://" + host + ":" + port, cafile=cafile, cadefault=True)
2. urllib.request.urlopen("https://" + host + ":" + port, cadefault=True)

python3-ubuntu-14.04_1  | [python3-urllib:run.py][ PASS ][ACCEPT][ supports SNI                  ][badssl.com]
python3-ubuntu-14.04_1  | [python3-urllib:run.py][ PASS ][REJECT][ expired                       ][expired.badssl.com]
python3-ubuntu-14.04_1  | [python3-urllib:run.py][ PASS ][REJECT][ wrong host                    ][wrong.host.badssl.com]
python3-ubuntu-14.04_1  | [python3-urllib:run.py][ PASS ][REJECT][ self-signed                   ][self-signed.badssl.com]
python3-ubuntu-14.04_1  | [python3-urllib:run.py][ PASS ][ACCEPT][ sha-256                       ][sha256.badssl.com]
python3-ubuntu-14.04_1  | [python3-urllib:run.py][ PASS ][ACCEPT][ 1000-sans                     ][1000-sans.badssl.com]
python3-ubuntu-14.04_1  | [python3-urllib:run.py][ FAIL ][REJECT][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
python3-ubuntu-14.04_1  | [python3-urllib:run.py][ PASS ][REJECT][ incomplete-chain              ][incomplete-chain.badssl.com]
python3-ubuntu-14.04_1  | [python3-urllib:run.py][ OK?  ][ACCEPT][ pinning-test                  ][pinning-test.badssl.com]
python3-ubuntu-14.04_1  | [python3-urllib:run.py][ PASS ][REJECT][ superfish                     ][superfish.badssl.com]
python3-ubuntu-14.04_1  | [python3-urllib:run.py][ PASS ][REJECT][ edellroot                     ][edellroot.badssl.com]
python3-ubuntu-14.04_1  | [python3-urllib:run.py][ PASS ][REJECT][ dsdtestprovider               ][dsdtestprovider.badssl.com]
python3-ubuntu-14.04_1  | [python3-urllib:run.py][ PASS ][REJECT][ disable ca-bundles            ][badssl.com]
</pre>


**Python 2.7.10**

driver: python2-ubuntu-14.04
https://github.com/ouspg/trytls/blob/667fc5f8aafaaa4f7d04b7cd6320b9feeabefb4e/runners/bashtls/drivers/python2-ubuntu-14.04/Dockerfile

python2-ubuntu-14.04_1  | [python-requests:run.py][ PASS ][ACCEPT][ supports SNI                  ][badssl.com]
python2-ubuntu-14.04_1  | [python-requests:run.py][ PASS ][REJECT][ expired                       ][expired.badssl.com]
python2-ubuntu-14.04_1  | [python-requests:run.py][ PASS ][REJECT][ wrong host                    ][wrong.host.badssl.com]
python2-ubuntu-14.04_1  | [python-requests:run.py][ PASS ][REJECT][ self-signed                   ][self-signed.badssl.com]
python2-ubuntu-14.04_1  | [python-requests:run.py][ PASS ][ACCEPT][ sha-256                       ][sha256.badssl.com]
python2-ubuntu-14.04_1  | [python-requests:run.py][ PASS ][ACCEPT][ 1000-sans                     ][1000-sans.badssl.com]
python2-ubuntu-14.04_1  | [python-requests:run.py][ FAIL ][REJECT][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
python2-ubuntu-14.04_1  | [python-requests:run.py][ PASS ][REJECT][ incomplete-chain              ][incomplete-chain.badssl.com]
python2-ubuntu-14.04_1  | [python-requests:run.py][ OK?  ][ACCEPT][ pinning-test                  ][pinning-test.badssl.com]
python2-ubuntu-14.04_1  | [python-requests:run.py][ PASS ][REJECT][ superfish                     ][superfish.badssl.com]
python2-ubuntu-14.04_1  | [python-requests:run.py][ PASS ][REJECT][ edellroot                     ][edellroot.badssl.com]
python2-ubuntu-14.04_1  | [python-requests:run.py][ PASS ][REJECT][ dsdtestprovider               ][dsdtestprovider.badssl.com]
python2-ubuntu-14.04_1  | [python-requests:run.py][ PASS ][REJECT][ disable ca-bundles            ][badssl.com]
python2-ubuntu-14.04_1  | [python-requests:run.py][ PASS ][REJECT][ OS X vulnerability ][www.ssllabs.com]
python2-ubuntu-14.04_1  | [python-requests:run.py][ PASS ][REJECT][ Freak              ][www.ssllabs.com]
python2-ubuntu-14.04_1  | [python-requests:run.py][ PASS ][REJECT][ Logjam             ][www.ssllabs.com]
python2-ubuntu-14.04_1  | [python-requests:run.py][ PASS ][ACCEPT][ Valid cert ][google.com]

python2-ubuntu-14.04_1  | [python-urllib2:run.py][ PASS ][ACCEPT][ supports SNI                  ][badssl.com]
python2-ubuntu-14.04_1  | [python-urllib2:run.py][ PASS ][REJECT][ expired                       ][expired.badssl.com]
python2-ubuntu-14.04_1  | [python-urllib2:run.py][ PASS ][REJECT][ wrong host                    ][wrong.host.badssl.com]
python2-ubuntu-14.04_1  | [python-urllib2:run.py][ PASS ][REJECT][ self-signed                   ][self-signed.badssl.com]
python2-ubuntu-14.04_1  | [python-urllib2:run.py][ PASS ][ACCEPT][ sha-256                       ][sha256.badssl.com]
python2-ubuntu-14.04_1  | [python-urllib2:run.py][ PASS ][ACCEPT][ 1000-sans                     ][1000-sans.badssl.com]
python2-ubuntu-14.04_1  | [python-urllib2:run.py][ FAIL ][REJECT][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
python2-ubuntu-14.04_1  | [python-urllib2:run.py][ PASS ][REJECT][ incomplete-chain              ][incomplete-chain.badssl.com]
python2-ubuntu-14.04_1  | [python-urllib2:run.py][ OK?  ][ACCEPT][ pinning-test                  ][pinning-test.badssl.com]
python2-ubuntu-14.04_1  | [python-urllib2:run.py][ PASS ][REJECT][ superfish                     ][superfish.badssl.com]
python2-ubuntu-14.04_1  | [python-urllib2:run.py][ PASS ][REJECT][ edellroot                     ][edellroot.badssl.com]
python2-ubuntu-14.04_1  | [python-urllib2:run.py][ PASS ][REJECT][ dsdtestprovider               ][dsdtestprovider.badssl.com]
python2-ubuntu-14.04_1  | [python-urllib2:run.py][ PASS ][REJECT][ disable ca-bundles            ][badssl.com]
python2-ubuntu-14.04_1  | [python-urllib2:run.py][ PASS ][REJECT][ OS X vulnerability ][www.ssllabs.com]
python2-ubuntu-14.04_1  | [python-urllib2:run.py][ PASS ][REJECT][ Freak              ][www.ssllabs.com]
python2-ubuntu-14.04_1  | [python-urllib2:run.py][ PASS ][REJECT][ Logjam             ][www.ssllabs.com]
python2-ubuntu-14.04_1  | [python-urllib2:run.py][ PASS ][ACCEPT][ Valid cert ][google.com]

**java**

driver: javac-default-ubuntu-14.04
https://github.com/ouspg/trytls/blob/667fc5f8aafaaa4f7d04b7cd6320b9feeabefb4e/runners/bashtls/drivers/javac-default-ubuntu-14.04/Dockerfile

javac-default-ubuntu-14.04_1  | [java-https:Run][ PASS ][ACCEPT][ supports SNI                  ][badssl.com]
javac-default-ubuntu-14.04_1  | [java-https:Run][ PASS ][REJECT][ expired                       ][expired.badssl.com]
javac-default-ubuntu-14.04_1  | [java-https:Run][ PASS ][REJECT][ wrong host                    ][wrong.host.badssl.com]
javac-default-ubuntu-14.04_1  | [java-https:Run][ PASS ][REJECT][ self-signed                   ][self-signed.badssl.com]
javac-default-ubuntu-14.04_1  | [java-https:Run][ PASS ][ACCEPT][ sha-256                       ][sha256.badssl.com]
javac-default-ubuntu-14.04_1  | [java-https:Run][ PASS ][ACCEPT][ 1000-sans                     ][1000-sans.badssl.com]
javac-default-ubuntu-14.04_1  | [java-https:Run][ PASS ][ACCEPT][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
javac-default-ubuntu-14.04_1  | [java-https:Run][ PASS ][REJECT][ incomplete-chain              ][incomplete-chain.badssl.com]
javac-default-ubuntu-14.04_1  | [java-https:Run][ OK?  ][ACCEPT][ pinning-test                  ][pinning-test.badssl.com]
javac-default-ubuntu-14.04_1  | [java-https:Run][ PASS ][REJECT][ superfish                     ][superfish.badssl.com]
javac-default-ubuntu-14.04_1  | [java-https:Run][ PASS ][REJECT][ edellroot                     ][edellroot.badssl.com]
javac-default-ubuntu-14.04_1  | [java-https:Run][ PASS ][REJECT][ dsdtestprovider               ][dsdtestprovider.badssl.com]
javac-default-ubuntu-14.04_1  | [java-https:Run][ OK?  ][ UNSUPPORTED  ][ disable ca-bundles            ][badssl.com]
javac-default-ubuntu-14.04_1  | [java-https:Run][ PASS ][REJECT][ OS X vulnerability ][www.ssllabs.com]
javac-default-ubuntu-14.04_1  | [java-https:Run][ PASS ][REJECT][ Freak              ][www.ssllabs.com]
javac-default-ubuntu-14.04_1  | [java-https:Run][ PASS ][REJECT][ Logjam             ][www.ssllabs.com]
javac-default-ubuntu-14.04_1  | [java-https:Run][ PASS ][ACCEPT][ Valid cert ][google.com]

javac-default-ubuntu-14.04_1  | [java-net:Run][ PASS ][ACCEPT][ supports SNI                  ][badssl.com]
javac-default-ubuntu-14.04_1  | [java-net:Run][ PASS ][REJECT][ expired                       ][expired.badssl.com]
javac-default-ubuntu-14.04_1  | [java-net:Run][ PASS ][REJECT][ wrong host                    ][wrong.host.badssl.com]
javac-default-ubuntu-14.04_1  | [java-net:Run][ PASS ][REJECT][ self-signed                   ][self-signed.badssl.com]
javac-default-ubuntu-14.04_1  | [java-net:Run][ PASS ][ACCEPT][ sha-256                       ][sha256.badssl.com]
javac-default-ubuntu-14.04_1  | [java-net:Run][ PASS ][ACCEPT][ 1000-sans                     ][1000-sans.badssl.com]
javac-default-ubuntu-14.04_1  | [java-net:Run][ PASS ][ACCEPT][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
javac-default-ubuntu-14.04_1  | [java-net:Run][ PASS ][REJECT][ incomplete-chain              ][incomplete-chain.badssl.com]
javac-default-ubuntu-14.04_1  | [java-net:Run][ OK?  ][ACCEPT][ pinning-test                  ][pinning-test.badssl.com]
javac-default-ubuntu-14.04_1  | [java-net:Run][ PASS ][REJECT][ superfish                     ][superfish.badssl.com]
javac-default-ubuntu-14.04_1  | [java-net:Run][ PASS ][REJECT][ edellroot                     ][edellroot.badssl.com]
javac-default-ubuntu-14.04_1  | [java-net:Run][ PASS ][REJECT][ dsdtestprovider               ][dsdtestprovider.badssl.com]
javac-default-ubuntu-14.04_1  | [java-net:Run][ OK?  ][ UNSUPPORTED  ][ disable ca-bundles            ][badssl.com]
javac-default-ubuntu-14.04_1  | [java-net:Run][ PASS ][REJECT][ OS X vulnerability ][www.ssllabs.com]
javac-default-ubuntu-14.04_1  | [java-net:Run][ PASS ][REJECT][ Freak              ][www.ssllabs.com]
javac-default-ubuntu-14.04_1  | [java-net:Run][ PASS ][REJECT][ Logjam             ][www.ssllabs.com]
javac-default-ubuntu-14.04_1  | [java-net:Run][ PASS ][ACCEPT][ Valid cert ][google.com]
