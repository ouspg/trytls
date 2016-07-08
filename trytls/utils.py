import os
import shutil
import tempfile
import functools
import contextlib


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
