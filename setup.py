import os
import imp
import sys
from setuptools import setup, find_packages

# Check the Python version
if sys.version_info < (3,):
    py_required = (2, 7, 9)
else:
    py_required = (3, 4, 0)

if sys.version_info < py_required:
    def format_version(version_info):
        return ".".join(str(x) for x in version_info[:3])

    sys.exit("ERROR: Python {0} or later required (you have {1})".format(
        format_version(py_required),
        format_version(sys.version_info)
    ))


install_requires=[
    "colorama",
    "oscrypto",
    "certbuilder"
]

# Python 3.8 removed the deprecated `platform.linux_distribution` function,
# recommending use of the 'distro' module for this purpose.
if sys.version_info > (3, 8, 0):
    install_requires.extend(["distro"])

# Import the local version of the package
found = imp.find_module("trytls", [os.path.join(os.path.dirname(__file__), "runners")])
trytls = imp.load_module("trytls", *found)

setup(
    name="trytls",
    version=trytls.__version__,
    license="MIT",
    description="Does your library check TLS certificates properly?",
    url="https://github.com/ouspg/trytls",
    package_dir={"": "./runners"},
    packages=find_packages("./runners"),
    entry_points={
        "console_scripts": [
            "trytls=trytls.runner:main"
        ],
        "trytls.bundles": [
            "https=trytls.bundles.https:all_tests"
        ],
        "trytls.formatters": [
            "default=trytls.formatters.default:formatter",
            "json=trytls.formatters.json:formatter"
        ]
    },
    install_requires=install_requires
)
