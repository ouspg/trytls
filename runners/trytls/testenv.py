class Test(object):
    def __init__(self, accept, description, host, port, cafile=None, name=None, skip=None):
        self.accept = accept
        self.description = description
        self.host = host
        self.port = port
        self.cafile = cafile

        if name is None:
            name = "{}:{}".format(self.host, self.port)
        self.name = name
        self.skip = skip


def testenv(func):
    def _testenv(*args, **keys):
        def __testenv():
            gen = func(*args, **keys)
            try:
                value = yield gen.next()
                while True:
                    value = yield gen.send(value)
            except StopIteration:
                pass
            finally:
                gen.close()
        return __testenv
    return _testenv


@testenv
def testgroup(*funcs):
    for func in funcs:
        gen = func()
        try:
            value = yield gen.next()
            while True:
                value = yield gen.send(value)
        except StopIteration:
            pass
        finally:
            gen.close()
