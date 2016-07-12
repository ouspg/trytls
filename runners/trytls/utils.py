import os
import sys
import shutil
import platform
import tempfile
import functools
import contextlib

try:
    from shlex import quote as _shlex_quote
except ImportError:
    def _shlex_quote(string):
        if string.isalnum():
            return string
        return "'" + string.replace("'", "\\'") + "'"


def format_command(args):
    return " ".join(_shlex_quote(arg) for arg in args)


def python_info():
    return platform.python_implementation() + " " + platform.python_version()


def platform_info():
    if sys.platform == "linux2":
        distname, version, _ = platform.linux_distribution()
        if not distname:
            return "Linux"
        if not version:
            return "Linux ({})".format(distname)
        return "Linux ({} {})".format(distname, version)
    elif sys.platform == "darwin":
        version, _, _ = platform.mac_ver()
        if version.startswith("10."):
            return "OS X {}".format(version)
        return "Darwin"
    return platform.system()


def memoized(func):
    value = []

    @functools.wraps(func)
    def _memoized():
        if not value:
            value.append(func())
        return value[0]

    return _memoized


@contextlib.contextmanager
def tmpfiles(first, *rest):
    datas = [first] + list(rest)

    tmp = tempfile.mkdtemp()
    try:
        filenames = []

        for index, data in enumerate(datas):
            filename = os.path.join(tmp, str(index))
            with open(filename, "wb") as fileobj:
                fileobj.write(data)
                fileobj.flush()
            filenames.append(filename)

        if not rest:
            yield filenames[0]
        else:
            yield filenames
    finally:
        shutil.rmtree(tmp)
