from __future__ import absolute_import, unicode_literals

import uuid
import datetime

from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa

from .utils import memoized


def _dump_cert(cert):
    return cert.public_bytes(serialization.Encoding.PEM)


def _dump_private_key(key):
    return key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )


def _load_private_key(data):
    return serialization.load_pem_private_key(data, None, default_backend())


def _gen_key(bits=4096):
    # Return the private key as PEM data to work around an issue with Python 3.5
    # and the "cryptography" package. Memoizing the private key objects causes
    # messages to be written to STDERR during the interpreter shutdown.
    # See https://github.com/pyca/cryptography/issues/2913.
    return _dump_private_key(
        rsa.generate_private_key(
            public_exponent=65537,
            key_size=bits,
            backend=default_backend()
        )
    )
_ca_key = memoized(_gen_key)
_cert_key = memoized(_gen_key)


def _ca_cert(private_key):
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My Company")
    ])

    return x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        private_key.public_key()
    ).not_valid_before(
        datetime.datetime.utcnow() - datetime.timedelta(days=356)
    ).not_valid_after(
        datetime.datetime.utcnow() + datetime.timedelta(days=356)
    ).serial_number(
        int(uuid.uuid4())
    ).add_extension(
        x509.BasicConstraints(True, None),
        critical=True
    ).sign(private_key, hashes.SHA256(), default_backend())


def gencert(cn):
    ca_key = _load_private_key(_ca_key())
    ca_cert = _ca_cert(ca_key)

    cert_key = _load_private_key(_cert_key())
    cert = x509.CertificateBuilder().subject_name(
        x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, cn)
        ])
    ).issuer_name(
        ca_cert.subject
    ).public_key(
        cert_key.public_key()
    ).not_valid_before(
        datetime.datetime.utcnow() - datetime.timedelta(days=356)
    ).not_valid_after(
        datetime.datetime.utcnow() + datetime.timedelta(days=356)
    ).serial_number(
        int(uuid.uuid4())
    ).sign(ca_key, hashes.SHA256(), default_backend())

    return _dump_cert(cert), _dump_private_key(cert_key), _dump_cert(ca_cert)
