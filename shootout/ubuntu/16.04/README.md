**bash**

driver: bash-ubuntu-latest
https://github.com/ouspg/trytls/blob/0a8c49e36746c9a36bef6bc99ed028244d1f23b3/runners/bashtls/drivers/bash-ubuntu-latest/Dockerfile

<pre>
bash-ubuntu-latest_1  | [bash-curl:run][ PASS ][ACCEPT][ Valid cert ][google.com]
bash-ubuntu-latest_1  | [bash-curl:run][ PASS ][REJECT][ OS X vulnerability ][www.ssllabs.com]
bash-ubuntu-latest_1  | [bash-curl:run][ PASS ][REJECT][ Freak              ][www.ssllabs.com]
bash-ubuntu-latest_1  | [bash-curl:run][ PASS ][REJECT][ Logjam             ][www.ssllabs.com]
bash-ubuntu-latest_1  | [bash-curl:run][ PASS ][ACCEPT][ supports SNI                  ][badssl.com]
bash-ubuntu-latest_1  | [bash-curl:run][ PASS ][REJECT][ expired                       ][expired.badssl.com]
bash-ubuntu-latest_1  | [bash-curl:run][ PASS ][REJECT][ wrong host                    ][wrong.host.badssl.com]
bash-ubuntu-latest_1  | [bash-curl:run][ PASS ][REJECT][ self-signed                   ][self-signed.badssl.com]
bash-ubuntu-latest_1  | [bash-curl:run][ PASS ][ACCEPT][ sha-256                       ][sha256.badssl.com]
bash-ubuntu-latest_1  | [bash-curl:run][ PASS ][ACCEPT][ 1000-sans                     ][1000-sans.badssl.com]
bash-ubuntu-latest_1  | [bash-curl:run][ FAIL ][REJECT][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
bash-ubuntu-latest_1  | [bash-curl:run][ PASS ][REJECT][ incomplete-chain              ][incomplete-chain.badssl.com]
bash-ubuntu-latest_1  | [bash-curl:run][ OK?  ][ACCEPT][ pinning-test                  ][pinning-test.badssl.com]
bash-ubuntu-latest_1  | [bash-curl:run][ PASS ][REJECT][ superfish                     ][superfish.badssl.com]
bash-ubuntu-latest_1  | [bash-curl:run][ PASS ][REJECT][ edellroot                     ][edellroot.badssl.com]
bash-ubuntu-latest_1  | [bash-curl:run][ PASS ][REJECT][ dsdtestprovider               ][dsdtestprovider.badssl.com]
bash-ubuntu-latest_1  | [bash-curl:run][ FAIL ][ACCEPT][ disable ca-bundles            ][badssl.com]
</pre>

**mono-complete with http://download.mono-project.com/repo/debian repo**

driver: mono-complete-latest-ubuntu-latest
https://github.com/ouspg/trytls/blob/0a8c49e36746c9a36bef6bc99ed028244d1f23b3/runners/bashtls/drivers/mono-complete-latest-ubuntu-latest/Dockerfile

<pre>
mono-complete-latest-ubuntu-latest_1  | [CSharp-Net:Run.exe][ PASS ][ACCEPT][ Valid cert ][google.com]
mono-complete-latest-ubuntu-latest_1  | [CSharp-Net:Run.exe][ PASS ][REJECT][ OS X vulnerability ][www.ssllabs.com]
mono-complete-latest-ubuntu-latest_1  | [CSharp-Net:Run.exe][ PASS ][REJECT][ Freak              ][www.ssllabs.com]
mono-complete-latest-ubuntu-latest_1  | [CSharp-Net:Run.exe][ PASS ][REJECT][ Logjam             ][www.ssllabs.com]
mono-complete-latest-ubuntu-latest_1  | [CSharp-Net:Run.exe][ PASS ][ACCEPT][ supports SNI                  ][badssl.com]
mono-complete-latest-ubuntu-latest_1  | [CSharp-Net:Run.exe][ PASS ][REJECT][ expired                       ][expired.badssl.com]
mono-complete-latest-ubuntu-latest_1  | [CSharp-Net:Run.exe][ PASS ][REJECT][ wrong host                    ][wrong.host.badssl.com]
mono-complete-latest-ubuntu-latest_1  | [CSharp-Net:Run.exe][ PASS ][REJECT][ self-signed                   ][self-signed.badssl.com]
mono-complete-latest-ubuntu-latest_1  | [CSharp-Net:Run.exe][ PASS ][ACCEPT][ sha-256                       ][sha256.badssl.com]
mono-complete-latest-ubuntu-latest_1  | [CSharp-Net:Run.exe][ FAIL ][REJECT][ 1000-sans                     ][1000-sans.badssl.com]
mono-complete-latest-ubuntu-latest_1  | [CSharp-Net:Run.exe][ FAIL ][REJECT][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
mono-complete-latest-ubuntu-latest_1  | [CSharp-Net:Run.exe][ PASS ][REJECT][ incomplete-chain              ][incomplete-chain.badssl.com]
mono-complete-latest-ubuntu-latest_1  | [CSharp-Net:Run.exe][ OK?  ][ACCEPT][ pinning-test                  ][pinning-test.badssl.com]
mono-complete-latest-ubuntu-latest_1  | [CSharp-Net:Run.exe][ PASS ][REJECT][ superfish                     ][superfish.badssl.com]
mono-complete-latest-ubuntu-latest_1  | [CSharp-Net:Run.exe][ PASS ][REJECT][ edellroot                     ][edellroot.badssl.com]
mono-complete-latest-ubuntu-latest_1  | [CSharp-Net:Run.exe][ PASS ][REJECT][ dsdtestprovider               ][dsdtestprovider.badssl.com]
mono-complete-latest-ubuntu-latest_1  | [CSharp-Net:Run.exe][ OK?  ][ UNSUPPORTED  ][ disable ca-bundles            ][badssl.com]

mono-complete-latest-ubuntu-latest_1  | [VB-Net:Run.exe][ PASS ][ACCEPT][ Valid cert ][google.com]
mono-complete-latest-ubuntu-latest_1  | [VB-Net:Run.exe][ PASS ][REJECT][ OS X vulnerability ][www.ssllabs.com]
mono-complete-latest-ubuntu-latest_1  | [VB-Net:Run.exe][ PASS ][REJECT][ Freak              ][www.ssllabs.com]
mono-complete-latest-ubuntu-latest_1  | [VB-Net:Run.exe][ PASS ][REJECT][ Logjam             ][www.ssllabs.com]
mono-complete-latest-ubuntu-latest_1  | [VB-Net:Run.exe][ PASS ][ACCEPT][ supports SNI                  ][badssl.com]
mono-complete-latest-ubuntu-latest_1  | [VB-Net:Run.exe][ PASS ][REJECT][ expired                       ][expired.badssl.com]
mono-complete-latest-ubuntu-latest_1  | [VB-Net:Run.exe][ PASS ][REJECT][ wrong host                    ][wrong.host.badssl.com]
mono-complete-latest-ubuntu-latest_1  | [VB-Net:Run.exe][ PASS ][REJECT][ self-signed                   ][self-signed.badssl.com]
mono-complete-latest-ubuntu-latest_1  | [VB-Net:Run.exe][ PASS ][ACCEPT][ sha-256                       ][sha256.badssl.com]
mono-complete-latest-ubuntu-latest_1  | [VB-Net:Run.exe][ FAIL ][REJECT][ 1000-sans                     ][1000-sans.badssl.com]
mono-complete-latest-ubuntu-latest_1  | [VB-Net:Run.exe][ FAIL ][REJECT][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
mono-complete-latest-ubuntu-latest_1  | [VB-Net:Run.exe][ PASS ][REJECT][ incomplete-chain              ][incomplete-chain.badssl.com]
mono-complete-latest-ubuntu-latest_1  | [VB-Net:Run.exe][ OK?  ][ACCEPT][ pinning-test                  ][pinning-test.badssl.com]
mono-complete-latest-ubuntu-latest_1  | [VB-Net:Run.exe][ PASS ][REJECT][ superfish                     ][superfish.badssl.com]
mono-complete-latest-ubuntu-latest_1  | [VB-Net:Run.exe][ PASS ][REJECT][ edellroot                     ][edellroot.badssl.com]
mono-complete-latest-ubuntu-latest_1  | [VB-Net:Run.exe][ PASS ][REJECT][ dsdtestprovider               ][dsdtestprovider.badssl.com]
mono-complete-latest-ubuntu-latest_1  | [VB-Net:Run.exe][ OK?  ][ UNSUPPORTED  ][ disable ca-bundles            ][badssl.com]
</pre>

**mono-complete without http://download.mono-project.com/repo/debian repo**

driver: mono-complete-latest
https://github.com/ouspg/trytls/blob/0a8c49e36746c9a36bef6bc99ed028244d1f23b3/runners/bashtls/drivers/mono-complete-latest/Dockerfile

<pre>
mono-complete-ubuntu-latest_1  | [CSharp-Net:Run.exe][ PASS ][ACCEPT][ Valid cert ][google.com]
mono-complete-ubuntu-latest_1  | [CSharp-Net:Run.exe][ PASS ][REJECT][ OS X vulnerability ][www.ssllabs.com]
mono-complete-ubuntu-latest_1  | [CSharp-Net:Run.exe][ PASS ][REJECT][ Freak              ][www.ssllabs.com]
mono-complete-ubuntu-latest_1  | [CSharp-Net:Run.exe][ PASS ][REJECT][ Logjam             ][www.ssllabs.com]
mono-complete-ubuntu-latest_1  | [CSharp-Net:Run.exe][ PASS ][ACCEPT][ supports SNI                  ][badssl.com]
mono-complete-ubuntu-latest_1  | [CSharp-Net:Run.exe][ FAIL ][ACCEPT][ expired                       ][expired.badssl.com]
mono-complete-ubuntu-latest_1  | [CSharp-Net:Run.exe][ PASS ][REJECT][ wrong host                    ][wrong.host.badssl.com]
mono-complete-ubuntu-latest_1  | [CSharp-Net:Run.exe][ PASS ][REJECT][ self-signed                   ][self-signed.badssl.com]
mono-complete-ubuntu-latest_1  | [CSharp-Net:Run.exe][ PASS ][ACCEPT][ sha-256                       ][sha256.badssl.com]
mono-complete-ubuntu-latest_1  | [CSharp-Net:Run.exe][ FAIL ][REJECT][ 1000-sans                     ][1000-sans.badssl.com]
mono-complete-ubuntu-latest_1  | [CSharp-Net:Run.exe][ FAIL ][REJECT][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
mono-complete-ubuntu-latest_1  | [CSharp-Net:Run.exe][ PASS ][REJECT][ incomplete-chain              ][incomplete-chain.badssl.com]
mono-complete-ubuntu-latest_1  | [CSharp-Net:Run.exe][ OK?  ][ACCEPT][ pinning-test                  ][pinning-test.badssl.com]
mono-complete-ubuntu-latest_1  | [CSharp-Net:Run.exe][ PASS ][REJECT][ superfish                     ][superfish.badssl.com]
mono-complete-ubuntu-latest_1  | [CSharp-Net:Run.exe][ PASS ][REJECT][ edellroot                     ][edellroot.badssl.com]
mono-complete-ubuntu-latest_1  | [CSharp-Net:Run.exe][ PASS ][REJECT][ dsdtestprovider               ][dsdtestprovider.badssl.com]
mono-complete-ubuntu-latest_1  | [CSharp-Net:Run.exe][ OK?  ][ UNSUPPORTED  ][ disable ca-bundles            ][badssl.com]

mono-complete-ubuntu-latest_1  | [VB-Net:Run.exe][ PASS ][ACCEPT][ Valid cert ][google.com]
mono-complete-ubuntu-latest_1  | [VB-Net:Run.exe][ PASS ][REJECT][ OS X vulnerability ][www.ssllabs.com]
mono-complete-ubuntu-latest_1  | [VB-Net:Run.exe][ PASS ][REJECT][ Freak              ][www.ssllabs.com]
mono-complete-ubuntu-latest_1  | [VB-Net:Run.exe][ PASS ][REJECT][ Logjam             ][www.ssllabs.com]
mono-complete-ubuntu-latest_1  | [VB-Net:Run.exe][ PASS ][ACCEPT][ supports SNI                  ][badssl.com]
mono-complete-ubuntu-latest_1  | [VB-Net:Run.exe][ FAIL ][ACCEPT][ expired                       ][expired.badssl.com]
mono-complete-ubuntu-latest_1  | [VB-Net:Run.exe][ PASS ][REJECT][ wrong host                    ][wrong.host.badssl.com]
mono-complete-ubuntu-latest_1  | [VB-Net:Run.exe][ PASS ][REJECT][ self-signed                   ][self-signed.badssl.com]
mono-complete-ubuntu-latest_1  | [VB-Net:Run.exe][ PASS ][ACCEPT][ sha-256                       ][sha256.badssl.com]
mono-complete-ubuntu-latest_1  | [VB-Net:Run.exe][ FAIL ][REJECT][ 1000-sans                     ][1000-sans.badssl.com]
mono-complete-ubuntu-latest_1  | [VB-Net:Run.exe][ FAIL ][REJECT][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
mono-complete-ubuntu-latest_1  | [VB-Net:Run.exe][ PASS ][REJECT][ incomplete-chain              ][incomplete-chain.badssl.com]
mono-complete-ubuntu-latest_1  | [VB-Net:Run.exe][ OK?  ][ACCEPT][ pinning-test                  ][pinning-test.badssl.com]
mono-complete-ubuntu-latest_1  | [VB-Net:Run.exe][ PASS ][REJECT][ superfish                     ][superfish.badssl.com]
mono-complete-ubuntu-latest_1  | [VB-Net:Run.exe][ PASS ][REJECT][ edellroot                     ][edellroot.badssl.com]
mono-complete-ubuntu-latest_1  | [VB-Net:Run.exe][ PASS ][REJECT][ dsdtestprovider               ][dsdtestprovider.badssl.com]
mono-complete-ubuntu-latest_1  | [VB-Net:Run.exe][ OK?  ][ UNSUPPORTED  ][ disable ca-bundles            ][badssl.com]
</pre>

**python2**

driver: python2-ubuntu-latest
https://github.com/ouspg/trytls/blob/0a8c49e36746c9a36bef6bc99ed028244d1f23b3/runners/bashtls/drivers/python2-ubuntu-latest/Dockerfile

<pre>
python2-ubuntu-latest_1  | [python-urllib3:run.py][ PASS ][ACCEPT][ Valid cert ][google.com]
python2-ubuntu-latest_1  | [python-urllib3:run.py][ PASS ][REJECT][ OS X vulnerability ][www.ssllabs.com]
python2-ubuntu-latest_1  | [python-urllib3:run.py][ PASS ][REJECT][ Freak              ][www.ssllabs.com]
python2-ubuntu-latest_1  | [python-urllib3:run.py][ PASS ][REJECT][ Logjam             ][www.ssllabs.com]
python2-ubuntu-latest_1  | [python-urllib3:run.py][ PASS ][ACCEPT][ supports SNI                  ][badssl.com]
python2-ubuntu-latest_1  | [python-urllib3:run.py][ PASS ][REJECT][ expired                       ][expired.badssl.com]
python2-ubuntu-latest_1  | [python-urllib3:run.py][ PASS ][REJECT][ wrong host                    ][wrong.host.badssl.com]
python2-ubuntu-latest_1  | [python-urllib3:run.py][ PASS ][REJECT][ self-signed                   ][self-signed.badssl.com]
python2-ubuntu-latest_1  | [python-urllib3:run.py][ PASS ][ACCEPT][ sha-256                       ][sha256.badssl.com]
python2-ubuntu-latest_1  | [python-urllib3:run.py][ PASS ][ACCEPT][ 1000-sans                     ][1000-sans.badssl.com]
python2-ubuntu-latest_1  | [python-urllib3:run.py][ FAIL ][REJECT][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
python2-ubuntu-latest_1  | [python-urllib3:run.py][ PASS ][REJECT][ incomplete-chain              ][incomplete-chain.badssl.com]
python2-ubuntu-latest_1  | [python-urllib3:run.py][ OK?  ][ACCEPT][ pinning-test                  ][pinning-test.badssl.com]
python2-ubuntu-latest_1  | [python-urllib3:run.py][ PASS ][REJECT][ superfish                     ][superfish.badssl.com]
python2-ubuntu-latest_1  | [python-urllib3:run.py][ PASS ][REJECT][ edellroot                     ][edellroot.badssl.com]
python2-ubuntu-latest_1  | [python-urllib3:run.py][ PASS ][REJECT][ dsdtestprovider               ][dsdtestprovider.badssl.com]
python2-ubuntu-latest_1  | [python-urllib3:run.py][ PASS ][REJECT][ disable ca-bundles            ][badssl.com]

python2-ubuntu-latest_1  | [python-urllib2:run.py][ PASS ][ACCEPT][ Valid cert ][google.com]
python2-ubuntu-latest_1  | [python-urllib2:run.py][ PASS ][REJECT][ OS X vulnerability ][www.ssllabs.com]
python2-ubuntu-latest_1  | [python-urllib2:run.py][ PASS ][REJECT][ Freak              ][www.ssllabs.com]
python2-ubuntu-latest_1  | [python-urllib2:run.py][ PASS ][REJECT][ Logjam             ][www.ssllabs.com]
python2-ubuntu-latest_1  | [python-urllib2:run.py][ PASS ][ACCEPT][ supports SNI                  ][badssl.com]
python2-ubuntu-latest_1  | [python-urllib2:run.py][ PASS ][REJECT][ expired                       ][expired.badssl.com]
python2-ubuntu-latest_1  | [python-urllib2:run.py][ PASS ][REJECT][ wrong host                    ][wrong.host.badssl.com]
python2-ubuntu-latest_1  | [python-urllib2:run.py][ PASS ][REJECT][ self-signed                   ][self-signed.badssl.com]
python2-ubuntu-latest_1  | [python-urllib2:run.py][ PASS ][ACCEPT][ sha-256                       ][sha256.badssl.com]
python2-ubuntu-latest_1  | [python-urllib2:run.py][ PASS ][ACCEPT][ 1000-sans                     ][1000-sans.badssl.com]
python2-ubuntu-latest_1  | [python-urllib2:run.py][ FAIL ][REJECT][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
python2-ubuntu-latest_1  | [python-urllib2:run.py][ PASS ][REJECT][ incomplete-chain              ][incomplete-chain.badssl.com]
python2-ubuntu-latest_1  | [python-urllib2:run.py][ OK?  ][ACCEPT][ pinning-test                  ][pinning-test.badssl.com]
python2-ubuntu-latest_1  | [python-urllib2:run.py][ PASS ][REJECT][ superfish                     ][superfish.badssl.com]
python2-ubuntu-latest_1  | [python-urllib2:run.py][ PASS ][REJECT][ edellroot                     ][edellroot.badssl.com]
python2-ubuntu-latest_1  | [python-urllib2:run.py][ PASS ][REJECT][ dsdtestprovider               ][dsdtestprovider.badssl.com]
python2-ubuntu-latest_1  | [python-urllib2:run.py][ PASS ][REJECT][ disable ca-bundles            ][badssl.com]

python2-ubuntu-latest_1  | [python-requests:run.py][ PASS ][ACCEPT][ Valid cert ][google.com]
python2-ubuntu-latest_1  | [python-requests:run.py][ PASS ][REJECT][ OS X vulnerability ][www.ssllabs.com]
python2-ubuntu-latest_1  | [python-requests:run.py][ PASS ][REJECT][ Freak              ][www.ssllabs.com]
python2-ubuntu-latest_1  | [python-requests:run.py][ PASS ][REJECT][ Logjam             ][www.ssllabs.com]
python2-ubuntu-latest_1  | [python-requests:run.py][ PASS ][ACCEPT][ supports SNI                  ][badssl.com]
python2-ubuntu-latest_1  | [python-requests:run.py][ PASS ][REJECT][ expired                       ][expired.badssl.com]
python2-ubuntu-latest_1  | [python-requests:run.py][ PASS ][REJECT][ wrong host                    ][wrong.host.badssl.com]
python2-ubuntu-latest_1  | [python-requests:run.py][ PASS ][REJECT][ self-signed                   ][self-signed.badssl.com]
python2-ubuntu-latest_1  | [python-requests:run.py][ PASS ][ACCEPT][ sha-256                       ][sha256.badssl.com]
python2-ubuntu-latest_1  | [python-requests:run.py][ PASS ][ACCEPT][ 1000-sans                     ][1000-sans.badssl.com]
python2-ubuntu-latest_1  | [python-requests:run.py][ FAIL ][REJECT][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
python2-ubuntu-latest_1  | [python-requests:run.py][ PASS ][REJECT][ incomplete-chain              ][incomplete-chain.badssl.com]
python2-ubuntu-latest_1  | [python-requests:run.py][ OK?  ][ACCEPT][ pinning-test                  ][pinning-test.badssl.com]
python2-ubuntu-latest_1  | [python-requests:run.py][ PASS ][REJECT][ superfish                     ][superfish.badssl.com]
python2-ubuntu-latest_1  | [python-requests:run.py][ PASS ][REJECT][ edellroot                     ][edellroot.badssl.com]
python2-ubuntu-latest_1  | [python-requests:run.py][ PASS ][REJECT][ dsdtestprovider               ][dsdtestprovider.badssl.com]
python2-ubuntu-latest_1  | [python-requests:run.py][ PASS ][REJECT][ disable ca-bundles            ][badssl.com]
</pre>

**python3**

driver: python3-ubuntu-latest
https://github.com/ouspg/trytls/blob/0a8c49e36746c9a36bef6bc99ed028244d1f23b3/runners/bashtls/drivers/python3-ubuntu-latest/Dockerfile

<pre>
python3-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][ACCEPT][ Valid cert ][google.com]
python3-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ OS X vulnerability ][www.ssllabs.com]
python3-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ Freak              ][www.ssllabs.com]
python3-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ Logjam             ][www.ssllabs.com]
python3-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][ACCEPT][ supports SNI                  ][badssl.com]
python3-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ expired                       ][expired.badssl.com]
python3-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ wrong host                    ][wrong.host.badssl.com]
python3-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ self-signed                   ][self-signed.badssl.com]
python3-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][ACCEPT][ sha-256                       ][sha256.badssl.com]
python3-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][ACCEPT][ 1000-sans                     ][1000-sans.badssl.com]
python3-ubuntu-latest_1  | [python3-urllib:run.py][ FAIL ][REJECT][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
python3-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ incomplete-chain              ][incomplete-chain.badssl.com]
python3-ubuntu-latest_1  | [python3-urllib:run.py][ OK?  ][ACCEPT][ pinning-test                  ][pinning-test.badssl.com]
python3-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ superfish                     ][superfish.badssl.com]
python3-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ edellroot                     ][edellroot.badssl.com]
python3-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ dsdtestprovider               ][dsdtestprovider.badssl.com]
python3-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ disable ca-bundles            ][badssl.com]
</pre>

**python3.5**

driver: python3-ubuntu-latest
https://github.com/ouspg/trytls/blob/0a8c49e36746c9a36bef6bc99ed028244d1f23b3/runners/bashtls/drivers/python3.5-ubuntu-latest/Dockerfile

<pre>
python3.5-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][ACCEPT][ Valid cert ][google.com]
python3.5-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ OS X vulnerability ][www.ssllabs.com]
python3.5-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ Freak              ][www.ssllabs.com]
python3.5-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ Logjam             ][www.ssllabs.com]
python3.5-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][ACCEPT][ supports SNI                  ][badssl.com]
python3.5-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ expired                       ][expired.badssl.com]
python3.5-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ wrong host                    ][wrong.host.badssl.com]
python3.5-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ self-signed                   ][self-signed.badssl.com]
python3.5-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][ACCEPT][ sha-256                       ][sha256.badssl.com]
python3.5-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][ACCEPT][ 1000-sans                     ][1000-sans.badssl.com]
python3.5-ubuntu-latest_1  | [python3-urllib:run.py][ FAIL ][REJECT][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
python3.5-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ incomplete-chain              ][incomplete-chain.badssl.com]
python3.5-ubuntu-latest_1  | [python3-urllib:run.py][ OK?  ][ACCEPT][ pinning-test                  ][pinning-test.badssl.com]
python3.5-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ superfish                     ][superfish.badssl.com]
python3.5-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ edellroot                     ][edellroot.badssl.com]
python3.5-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ dsdtestprovider               ][dsdtestprovider.badssl.com]
python3.5-ubuntu-latest_1  | [python3-urllib:run.py][ PASS ][REJECT][ disable ca-bundles            ][badssl.com]
</pre>

**java**

driver: java-default-ubuntu-latest
https://github.com/ouspg/trytls/blob/0a8c49e36746c9a36bef6bc99ed028244d1f23b3/runners/bashtls/drivers/java-default-ubuntu-latest/Dockerfile

<pre>
java-default-ubuntu-latest_1  | [java-https:Run][ PASS ][ACCEPT][ Valid cert ][google.com]
java-default-ubuntu-latest_1  | [java-https:Run][ PASS ][REJECT][ OS X vulnerability ][www.ssllabs.com]
java-default-ubuntu-latest_1  | [java-https:Run][ PASS ][REJECT][ Freak              ][www.ssllabs.com]
java-default-ubuntu-latest_1  | [java-https:Run][ PASS ][REJECT][ Logjam             ][www.ssllabs.com]
java-default-ubuntu-latest_1  | [java-https:Run][ PASS ][ACCEPT][ supports SNI                  ][badssl.com]
java-default-ubuntu-latest_1  | [java-https:Run][ PASS ][REJECT][ expired                       ][expired.badssl.com]
java-default-ubuntu-latest_1  | [java-https:Run][ PASS ][REJECT][ wrong host                    ][wrong.host.badssl.com]
java-default-ubuntu-latest_1  | [java-https:Run][ PASS ][REJECT][ self-signed                   ][self-signed.badssl.com]
java-default-ubuntu-latest_1  | [java-https:Run][ PASS ][ACCEPT][ sha-256                       ][sha256.badssl.com]
java-default-ubuntu-latest_1  | [java-https:Run][ PASS ][ACCEPT][ 1000-sans                     ][1000-sans.badssl.com]
java-default-ubuntu-latest_1  | [java-https:Run][ PASS ][ACCEPT][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
java-default-ubuntu-latest_1  | [java-https:Run][ PASS ][REJECT][ incomplete-chain              ][incomplete-chain.badssl.com]
java-default-ubuntu-latest_1  | [java-https:Run][ OK?  ][ACCEPT][ pinning-test                  ][pinning-test.badssl.com]
java-default-ubuntu-latest_1  | [java-https:Run][ PASS ][REJECT][ superfish                     ][superfish.badssl.com]
java-default-ubuntu-latest_1  | [java-https:Run][ PASS ][REJECT][ edellroot                     ][edellroot.badssl.com]
java-default-ubuntu-latest_1  | [java-https:Run][ PASS ][REJECT][ dsdtestprovider               ][dsdtestprovider.badssl.com]
java-default-ubuntu-latest_1  | [java-https:Run][ OK?  ][ UNSUPPORTED  ][ disable ca-bundles            ][badssl.com]

java-default-ubuntu-latest_1  | [java-net:Run][ PASS ][ACCEPT][ Valid cert ][google.com]
java-default-ubuntu-latest_1  | [java-net:Run][ PASS ][REJECT][ OS X vulnerability ][www.ssllabs.com]
java-default-ubuntu-latest_1  | [java-net:Run][ PASS ][REJECT][ Freak              ][www.ssllabs.com]
java-default-ubuntu-latest_1  | [java-net:Run][ PASS ][REJECT][ Logjam             ][www.ssllabs.com]
java-default-ubuntu-latest_1  | [java-net:Run][ PASS ][ACCEPT][ supports SNI                  ][badssl.com]
java-default-ubuntu-latest_1  | [java-net:Run][ PASS ][REJECT][ expired                       ][expired.badssl.com]
java-default-ubuntu-latest_1  | [java-net:Run][ PASS ][REJECT][ wrong host                    ][wrong.host.badssl.com]
java-default-ubuntu-latest_1  | [java-net:Run][ PASS ][REJECT][ self-signed                   ][self-signed.badssl.com]
java-default-ubuntu-latest_1  | [java-net:Run][ PASS ][ACCEPT][ sha-256                       ][sha256.badssl.com]
java-default-ubuntu-latest_1  | [java-net:Run][ PASS ][ACCEPT][ 1000-sans                     ][1000-sans.badssl.com]
java-default-ubuntu-latest_1  | [java-net:Run][ PASS ][ACCEPT][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
java-default-ubuntu-latest_1  | [java-net:Run][ PASS ][REJECT][ incomplete-chain              ][incomplete-chain.badssl.com]
java-default-ubuntu-latest_1  | [java-net:Run][ OK?  ][ACCEPT][ pinning-test                  ][pinning-test.badssl.com]
java-default-ubuntu-latest_1  | [java-net:Run][ PASS ][REJECT][ superfish                     ][superfish.badssl.com]
java-default-ubuntu-latest_1  | [java-net:Run][ PASS ][REJECT][ edellroot                     ][edellroot.badssl.com]
java-default-ubuntu-latest_1  | [java-net:Run][ PASS ][REJECT][ dsdtestprovider               ][dsdtestprovider.badssl.com]
java-default-ubuntu-latest_1  | [java-net:Run][ OK?  ][ UNSUPPORTED  ][ disable ca-bundles            ][badssl.com]
</pre>

**php**

driver: php-ubuntu-latest
https://github.com/ouspg/trytls/blob/0a8c49e36746c9a36bef6bc99ed028244d1f23b3/runners/bashtls/drivers/php-ubuntu-latest/Dockerfile

<pre>
php-ubuntu-latest_1  | [php-file-get-contents:run.php][ PASS ][ACCEPT][ Valid cert ][google.com]
php-ubuntu-latest_1  | [php-file-get-contents:run.php][ PASS ][REJECT][ OS X vulnerability ][www.ssllabs.com]
php-ubuntu-latest_1  | [php-file-get-contents:run.php][ PASS ][REJECT][ Freak              ][www.ssllabs.com]
php-ubuntu-latest_1  | [php-file-get-contents:run.php][ PASS ][REJECT][ Logjam             ][www.ssllabs.com]
php-ubuntu-latest_1  | [php-file-get-contents:run.php][ PASS ][ACCEPT][ supports SNI                  ][badssl.com]
php-ubuntu-latest_1  | [php-file-get-contents:run.php][ PASS ][REJECT][ expired                       ][expired.badssl.com]
php-ubuntu-latest_1  | [php-file-get-contents:run.php][ PASS ][REJECT][ wrong host                    ][wrong.host.badssl.com]
php-ubuntu-latest_1  | [php-file-get-contents:run.php][ PASS ][REJECT][ self-signed                   ][self-signed.badssl.com]
php-ubuntu-latest_1  | [php-file-get-contents:run.php][ PASS ][ACCEPT][ sha-256                       ][sha256.badssl.com]
php-ubuntu-latest_1  | [php-file-get-contents:run.php][ PASS ][ACCEPT][ 1000-sans                     ][1000-sans.badssl.com]
php-ubuntu-latest_1  | [php-file-get-contents:run.php][ FAIL ][REJECT][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
php-ubuntu-latest_1  | [php-file-get-contents:run.php][ PASS ][REJECT][ incomplete-chain              ][incomplete-chain.badssl.com]
php-ubuntu-latest_1  | [php-file-get-contents:run.php][ OK?  ][ACCEPT][ pinning-test                  ][pinning-test.badssl.com]
php-ubuntu-latest_1  | [php-file-get-contents:run.php][ PASS ][REJECT][ superfish                     ][superfish.badssl.com]
php-ubuntu-latest_1  | [php-file-get-contents:run.php][ PASS ][REJECT][ edellroot                     ][edellroot.badssl.com]
php-ubuntu-latest_1  | [php-file-get-contents:run.php][ PASS ][REJECT][ dsdtestprovider               ][dsdtestprovider.badssl.com]
php-ubuntu-latest_1  | [php-file-get-contents:run.php][ OK?  ][ UNSUPPORTED  ][ disable ca-bundles            ][badssl.com]
</pre>
