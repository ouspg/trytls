import contextlib


class _TestEnv(object):
    def __init__(self, func, args, kwargs):
        self._func = func
        self._args = args
        self._kwargs = kwargs

    def __repr__(self):
        """
        Return a readable representation of the wrapped function and its
        call arguments.

        >>> def mytest(a, b):
        ...     pass
        >>> repr(_TestEnv(mytest, [1], {"b": 2}))
        'mytest(1, b=2)'
        """

        params = []
        if self._args:
            params.extend("{v!r}".format(v=v) for v in self._args)
        if self._kwargs:
            params.extend("{k}={v!r}".format(k=k, v=v) for (k, v) in self._kwargs.items())
        return "{name}({params})".format(name=self._func.__name__, params=", ".join(params))

    def __call__(self):
        return contextlib.contextmanager(self._func)(*self._args, **self._kwargs)


def testenv(func):
    def _testenv(*args, **keys):
        return _TestEnv(func, args, keys)
    return _testenv


@testenv
def constant(ok_expected, host, port, cafile=None):
    yield ok_expected, host, port, cafile
