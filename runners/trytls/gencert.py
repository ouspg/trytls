from __future__ import absolute_import, unicode_literals

from oscrypto import asymmetric
from certbuilder import CertificateBuilder, pem_armor_certificate

from .utils import memoized


def _dump_cert(cert):
    return pem_armor_certificate(cert)


def _dump_private(key):
    return asymmetric.dump_private_key(key, None)


def _dump_public(key):
    return asymmetric.dump_public_key(key)


def _load_cert(data):
    return asymmetric.load_certificate(data)


def _load_public(data):
    return asymmetric.load_public_key(data)


def _load_private(data):
    return asymmetric.load_private_key(data)


def _gen_key(bits=4096):
    return asymmetric.generate_pair("rsa", bits)


@memoized
def _cert_key():
    public, private = _gen_key()
    return _dump_public(public), _dump_private(private)


@memoized
def _gen_ca():
    public, private = _gen_key()
    builder = CertificateBuilder(
        {
            "organization_name": "Fake Certificate Authority"
        },
        public
    )
    builder.self_signed = True
    builder.ca = True
    return (
        _dump_cert(builder.build(private)),
        _dump_private(private)
    )


def gencert(name):
    ca_cert_data, ca_private_data = _gen_ca()
    public_data, private_data = _cert_key()

    builder = CertificateBuilder(
        {
            "common_name": name
        },
        _load_public(public_data)
    )
    builder.issuer = _load_cert(ca_cert_data)
    builder.subject_alt_domains = [name]
    cert = builder.build(_load_private(ca_private_data))
    return (
        _dump_cert(cert),
        private_data,
        ca_cert_data
    )
