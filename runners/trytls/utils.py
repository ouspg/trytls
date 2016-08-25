from __future__ import print_function, unicode_literals

import os
import sys
import shutil
import platform
import tempfile
import functools
import contextlib

try:
    from shlex import quote as _quote
except ImportError:
    # shlex.quote was introduced in Python 3.3, use pipes.quote
    # for Python 2.7.
    from pipes import quote as _quote


def format_command(args):
    r"""
    Return a list of argument strings as one shell-escaped command.

    >>> import shlex
    >>> shlex.split(format_command(["echo", "Hello, World!", "'quoted'"]))
    ['echo', 'Hello, World!', "'quoted'"]
    """

    return " ".join(_quote(arg) for arg in args)


def python_info():
    r"""
    Return a human-readable name for the currently used Python version.
    """

    return platform.python_implementation() + " " + platform.python_version()


def platform_info():
    r"""
    Return a human-readable name for the currently used platform.
    """

    if sys.platform.startswith("linux"):
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
    r"""
    Return a memoized version of the given function.

    >>> @memoized
    ... def func():
    ...     print("First run!")
    ...     return 1
    >>> func()
    First run!
    1

    During the first call the function is executed and its return value gets
    memoized. Subsequent calls just return the value without re-executing the
    function.

    >>> func()
    1
    """

    value = []

    @functools.wraps(func)
    def _memoized():
        if not value:
            value.append(func())
        return value[0]

    return _memoized


@contextlib.contextmanager
def tmpfiles(first, *rest):
    r"""
    Return a tuple of paths to temporary files that containt the given input
    strings.

    >>> with tmpfiles(b"a", b"b") as (path_a, path_b):
    ...     open(path_a, "rb").read() == b"a"
    ...     open(path_b, "rb").read() == b"b"
    True
    True

    For convenience providing just one input string returns a plain path string
    instead of a tuple.

    >>> with tmpfiles(b"some data") as path:
    ...     open(path, "rb").read() == b"some data"
    True

    The files are removed after the with-block.

    >>> with tmpfiles(b"Hello, World!") as path:
    ...     pass
    >>> os.path.exists(path)
    False

    The returned pathname is absolute.

    >>> with tmpfiles(b"") as path:
    ...     os.path.isabs(path)
    True
    """

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


def decorator(decorator_func):
    """
    Return a decorator function.

    >>> @decorator
    ... def log_calls(func, *args, **keys):
    ...     print("calling", func.__name__)
    ...     return func(*args, **keys)
    ...
    >>> @log_calls
    ... def add(a, b):
    ...     return a + b
    ...
    >>> add(1, 2)
    calling add
    3
    """

    @functools.wraps(decorator_func)
    def _decorator(func):
        @functools.wraps(func)
        def __decorator(*args, **keys):
            return decorator_func(func, *args, **keys)
        return __decorator
    return _decorator
