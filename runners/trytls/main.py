import sys
from . import __version__

_main = sys.modules.get("__main__", None)
if _main is not None and not hasattr(_main, "__requires__"):
    _main.__requires__ = "trytls==" + __version__

import pkg_resources

for name in tuple(sys.modules):
    if name.split(".")[0] in ("pkg_resources", "setuptools"):
        del sys.modules[name]

from runner import main
