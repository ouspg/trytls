import sys
from setuptools import setup, find_packages


def format_version(version_info):
    return ".".join(str(x) for x in version_info[:3])

if sys.version_info < (3,):
    py_required = (2, 7, 9)
else:
    py_required = (3, 4, 0)

if sys.version_info < py_required:
    sys.exit("ERROR: Python {0} or later required (you have {1})".format(
        format_version(py_required),
        format_version(sys.version_info)
    ))

setup(
    name="trytls",
    version="0.0.4",
    package_dir={"": "./runners"},
    packages=find_packages("./runners"),
    entry_points={
        "console_scripts": [
            "trytls=trytls.runner:main"
        ],
        "trytls.bundles": [
            "handshake=trytls.bundles.handshake:all_tests",
            "https=trytls.bundles.https:all_tests",
            "imap=trytls.bundles.imap:all_tests"
        ]
    },
    install_requires=[
        "colorama"
    ]
)
