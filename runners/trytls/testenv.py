from .utils import decorator


class Test(object):
    def __init__(self, accept, description, host, port, cafile=None, name=None, forced_result=None):
        self.accept = accept
        self.description = description
        self.host = host
        self.port = port
        self.cafile = cafile

        if name is None:
            name = "{}:{}".format(self.host, self.port)
        self.name = name
        self.forced_result = forced_result


def run(gen, callback, *args, **keys):
    if callable(gen):
        gen = gen()
    stack = [gen]
    result = None

    while stack:
        try:
            value = stack[-1].send(result)
        except StopIteration as stop:
            # Interpret the generator's "return value" as described in PEP 380.
            # See: https://www.python.org/dev/peps/pep-0380/#enhancements-to-stopiteration
            result = stop.args[0] if stop.args else None
            stack.pop()
            continue

        if isinstance(value, Test):
            if value.forced_result is None:
                result = callback(value, *args, **keys)
            else:
                result = value.forced_result
            yield value, result
            continue

        if callable(value):
            value = value()
        result = None
        stack.append(value)


@decorator
def testenv(func, *args, **keys):
    def _testenv():
        return func(*args, **keys)
    return _testenv


@testenv
def testgroup(*funcs):
    for func in funcs:
        yield func
