import contextlib


class Test(object):
    def __init__(self, accept, description, host, port, cafile=None, name=None):
        self.accept = accept
        self.description = description
        self.host = host
        self.port = port
        self.cafile = cafile

        if name is None:
            name = "{}:{}".format(self.host, self.port)
        self.name = name


class _TestEnv(object):
    def __init__(self, func, args, kwargs):
        self._func = func
        self._args = args
        self._kwargs = kwargs

    def __call__(self):
        return contextlib.contextmanager(self._func)(*self._args, **self._kwargs)


def testenv(func):
    def _testenv(*args, **keys):
        return _TestEnv(func, args, keys)
    return _testenv
