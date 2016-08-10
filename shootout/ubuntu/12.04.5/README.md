**bash**

<pre>
bash-ubuntu-12.04.5_1  | [bash-curl:run][ PASS ][ACCEPT][ Valid cert ][google.com]
bash-ubuntu-12.04.5_1  | [bash-curl:run][ PASS ][REJECT][ OS X vulnerability ][www.ssllabs.com]
bash-ubuntu-12.04.5_1  | [bash-curl:run][ PASS ][REJECT][ Freak              ][www.ssllabs.com]
bash-ubuntu-12.04.5_1  | [bash-curl:run][ PASS ][REJECT][ Logjam             ][www.ssllabs.com]
bash-ubuntu-12.04.5_1  | [bash-curl:run][ PASS ][ACCEPT][ supports SNI                  ][badssl.com]
bash-ubuntu-12.04.5_1  | [bash-curl:run][ PASS ][REJECT][ expired                       ][expired.badssl.com]
bash-ubuntu-12.04.5_1  | [bash-curl:run][ PASS ][REJECT][ wrong host                    ][wrong.host.badssl.com]
bash-ubuntu-12.04.5_1  | [bash-curl:run][ PASS ][REJECT][ self-signed                   ][self-signed.badssl.com]
bash-ubuntu-12.04.5_1  | [bash-curl:run][ PASS ][ACCEPT][ sha-256                       ][sha256.badssl.com]
bash-ubuntu-12.04.5_1  | [bash-curl:run][ PASS ][ACCEPT][ 1000-sans                     ][1000-sans.badssl.com]
bash-ubuntu-12.04.5_1  | [bash-curl:run][ FAIL ][REJECT][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
bash-ubuntu-12.04.5_1  | [bash-curl:run][ PASS ][REJECT][ incomplete-chain              ][incomplete-chain.badssl.com]
bash-ubuntu-12.04.5_1  | [bash-curl:run][ OK?  ][ACCEPT][ pinning-test                  ][pinning-test.badssl.com]
bash-ubuntu-12.04.5_1  | [bash-curl:run][ PASS ][REJECT][ superfish                     ][superfish.badssl.com]
bash-ubuntu-12.04.5_1  | [bash-curl:run][ PASS ][REJECT][ edellroot                     ][edellroot.badssl.com]
bash-ubuntu-12.04.5_1  | [bash-curl:run][ PASS ][REJECT][ dsdtestprovider               ][dsdtestprovider.badssl.com]
bash-ubuntu-12.04.5_1  | [bash-curl:run][ FAIL ][ACCEPT][ disable ca-bundles            ][badssl.com]
</pre>

**python2**

<pre>
python2-ubuntu-12.04.5_1  | /usr/local/lib/python2.7/dist-packages/urllib3/util/ssl_.py:318: SNIMissingWarning: An HTTPS request has been made, but the SNI (Subject Name Indication) extension to TLS is not available on this platform. This may cause the server to present an incorrect TLS certificate, which can cause validation failures. You can upgrade to a newer version of Python to solve this. For more information, see https://urllib3.readthedocs.io/en/latest/security.html#snimissingwarning.
python2-ubuntu-12.04.5_1  |   SNIMissingWarning
python2-ubuntu-12.04.5_1  | /usr/local/lib/python2.7/dist-packages/urllib3/util/ssl_.py:122: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. You can upgrade to a newer version of Python to solve this. For more information, see https://urllib3.readthedocs.io/en/latest/security.html#insecureplatformwarning.
python2-ubuntu-12.04.5_1  |   InsecurePlatformWarning
python2-ubuntu-12.04.5_1  | /usr/local/lib/python2.7/dist-packages/urllib3/util/ssl_.py:122: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. You can upgrade to a newer version of Python to solve this. For more information, see https://urllib3.readthedocs.io/en/latest/security.html#insecureplatformwarning.
python2-ubuntu-12.04.5_1  |   InsecurePlatformWarning
python2-ubuntu-12.04.5_1  | [python-urllib3:run.py][ PASS ][ACCEPT][ Valid cert ][google.com]
python2-ubuntu-12.04.5_1  | [python-urllib3:run.py][ PASS ][REJECT][ OS X vulnerability ][www.ssllabs.com]
python2-ubuntu-12.04.5_1  | [python-urllib3:run.py][ PASS ][REJECT][ Freak              ][www.ssllabs.com]
python2-ubuntu-12.04.5_1  | [python-urllib3:run.py][ PASS ][REJECT][ Logjam             ][www.ssllabs.com]
python2-ubuntu-12.04.5_1  | [python-urllib3:run.py][ FAIL ][REJECT][-> SKIP badssl.com (till CONTINUE)    ][][badssl.com]
python2-ubuntu-12.04.5_1  | Traceback (most recent call last):
python2-ubuntu-12.04.5_1  |   File "run.py", line 14, in <module>
python2-ubuntu-12.04.5_1  |     except ssl.CertificateError:
python2-ubuntu-12.04.5_1  | AttributeError: 'module' object has no attribute 'CertificateError'
python2-ubuntu-12.04.5_1  | /usr/local/lib/python2.7/dist-packages/requests/packages/urllib3/util/ssl_.py:318: SNIMissingWarning: An HTTPS request has been made, but the SNI (Subject Name Indication) extension to TLS is not available on this platform. This may cause the server to present an incorrect TLS certificate, which can cause validation failures. You can upgrade to a newer version of Python to solve this. For more information, see https://urllib3.readthedocs.io/en/latest/security.html#snimissingwarning.
python2-ubuntu-12.04.5_1  |   SNIMissingWarning
python2-ubuntu-12.04.5_1  | /usr/local/lib/python2.7/dist-packages/requests/packages/urllib3/util/ssl_.py:122: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. You can upgrade to a newer version of Python to solve this. For more information, see https://urllib3.readthedocs.io/en/latest/security.html#insecureplatformwarning.
python2-ubuntu-12.04.5_1  |   InsecurePlatformWarning
python2-ubuntu-12.04.5_1  | /usr/local/lib/python2.7/dist-packages/requests/packages/urllib3/util/ssl_.py:122: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. You can upgrade to a newer version of Python to solve this. For more information, see https://urllib3.readthedocs.io/en/latest/security.html#insecureplatformwarning.
python2-ubuntu-12.04.5_1  |   InsecurePlatformWarning

python2-ubuntu-12.04.5_1  | [python-requests:run.py][ PASS ][ACCEPT][ Valid cert ][google.com]
python2-ubuntu-12.04.5_1  | [python-requests:run.py][ PASS ][REJECT][ OS X vulnerability ][www.ssllabs.com]
python2-ubuntu-12.04.5_1  | [python-requests:run.py][ PASS ][REJECT][ Freak              ][www.ssllabs.com]
python2-ubuntu-12.04.5_1  | [python-requests:run.py][ PASS ][REJECT][ Logjam             ][www.ssllabs.com]
python2-ubuntu-12.04.5_1  | [python-requests:run.py][ FAIL ][REJECT][-> SKIP badssl.com (till CONTINUE)    ][][badssl.com]
</pre>

**python3**

<pre>
python3-ubuntu-12.04.5_1  | [python3-urllib:run.py][ PASS ][ACCEPT][ Valid cert ][google.com]
python3-ubuntu-12.04.5_1  | [python3-urllib:run.py][ PASS ][REJECT][ OS X vulnerability ][www.ssllabs.com]
python3-ubuntu-12.04.5_1  | [python3-urllib:run.py][ PASS ][REJECT][ Freak              ][www.ssllabs.com]
python3-ubuntu-12.04.5_1  | [python3-urllib:run.py][ PASS ][REJECT][ Logjam             ][www.ssllabs.com]
python3-ubuntu-12.04.5_1  | [python3-urllib:run.py][ PASS ][ACCEPT][ supports SNI                  ][badssl.com]
python3-ubuntu-12.04.5_1  | [python3-urllib:run.py][ FAIL ][ACCEPT][ expired                       ][expired.badssl.com]
python3-ubuntu-12.04.5_1  | [python3-urllib:run.py][ FAIL ][ACCEPT][ wrong host                    ][wrong.host.badssl.com]
python3-ubuntu-12.04.5_1  | [python3-urllib:run.py][ FAIL ][ACCEPT][ self-signed                   ][self-signed.badssl.com]
python3-ubuntu-12.04.5_1  | [python3-urllib:run.py][ PASS ][ACCEPT][ sha-256                       ][sha256.badssl.com]
python3-ubuntu-12.04.5_1  | [python3-urllib:run.py][ PASS ][ACCEPT][ 1000-sans                     ][1000-sans.badssl.com]
python3-ubuntu-12.04.5_1  | [python3-urllib:run.py][ FAIL ][REJECT][ 10000-sans (Bad in ten years) ][10000-sans.badssl.com]
python3-ubuntu-12.04.5_1  | [python3-urllib:run.py][ FAIL ][ACCEPT][ incomplete-chain              ][incomplete-chain.badssl.com]
python3-ubuntu-12.04.5_1  | [python3-urllib:run.py][ OK?  ][ACCEPT][ pinning-test                  ][pinning-test.badssl.com]
python3-ubuntu-12.04.5_1  | [python3-urllib:run.py][ FAIL ][ACCEPT][ superfish                     ][superfish.badssl.com]
python3-ubuntu-12.04.5_1  | [python3-urllib:run.py][ FAIL ][ACCEPT][ edellroot                     ][edellroot.badssl.com]
python3-ubuntu-12.04.5_1  | [python3-urllib:run.py][ FAIL ][ACCEPT][ dsdtestprovider               ][dsdtestprovider.badssl.com]
python3-ubuntu-12.04.5_1  | [python3-urllib:run.py][ PASS ][REJECT][ disable ca-bundles            ][badssl.com]
</pre>

**java**

<pre>
Exception in thread "main" java.lang.UnsupportedClassVersionError: Run : Unsupported major.minor version 52.
</pre>
