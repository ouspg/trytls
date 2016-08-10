**python3.4.3**

<pre>
ubuntu:14.04
RUN apt-get -y update && \
  apt-get -y install \
  python3
</pre>

<pre>
either: urllib.request.urlopen("https://" + host + ":" + port, cafile=cafile, cadefault=False)
or:     urllib.request.urlopen("https://" + host + ":" + port, cafile=cafile)

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
urllib.request.urlopen("https://" + host + ":" + port, cafile=cafile, cadefault=True)

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
