import subprocess
from .utils import tmpfiles, memoized


def openssl(args, input=None):
    process = subprocess.Popen(
        ["openssl"] + list(args),
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, _ = process.communicate(input)
    if process.returncode != 0:
        raise RuntimeError()
    return stdout


@memoized
def _ca_key():
    return openssl(["genrsa", "4096"])


@memoized
def _cert_key():
    return openssl(["genrsa", "4096"])


def gencert(cn):
    subj = "/CN=" + cn
    ca_key = _ca_key()
    cert_key = _cert_key()

    # Generate the CA
    with tmpfiles(ca_key) as ca_keyfile:
        ca_data = openssl(["req", "-new", "-key", ca_keyfile, "-x509", "-subj", "/"])

    # Generate a certificate signing request
    with tmpfiles(cert_key) as cert_keyfile:
        cert_csr = openssl(["req", "-new", "-subj", subj, "-key", cert_keyfile])

    # Sign the certificate with the CA
    with tmpfiles(ca_key, ca_data) as (ca_keyfile, ca_file):
        cert_data = openssl(
            ["x509", "-req", "-CA", ca_file, "-CAkey", ca_keyfile, "-set_serial", "01"],
            input=cert_csr
        )

    return cert_data, cert_key, ca_data
