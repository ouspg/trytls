import ssl
import socket
import contextlib
import multiprocessing
from .utils import tmpfiles
from .gencert import gencert


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
def badssl(ok_expected, name):
    yield ok_expected, name + ".badssl.com", 443, None


def raw_callback(conn, certfile, keyfile):
    ssl.wrap_socket(conn, server_side=True, certfile=certfile, keyfile=keyfile)


def https_callback(conn, certfile, keyfile):
    s = ssl.wrap_socket(conn, server_side=True, certfile=certfile, keyfile=keyfile)
    s.sendall(b"HTTP/1.0 200 OK\r\nContent-Length: 0\r\n\r\n")


@contextlib.contextmanager
def mock_server(certdata, keydata, host="localhost", port=0, callback=raw_callback):
    def serve(connection, certdata, keydata, host, port, callback):
        sock = socket.socket()
        try:
            sock.bind((host, port))
            sock.listen(1)

            _, port = sock.getsockname()
            connection.send((host, port))

            conn, addr = sock.accept()
        finally:
            sock.close()

        try:
            with tmpfiles(certdata, keydata) as (certfile, keyfile):
                callback(conn, certfile, keyfile)
        finally:
            conn.close()

    reader, writer = multiprocessing.Pipe(duplex=False)
    process = multiprocessing.Process(
        target=serve,
        args=[writer, certdata, keydata, host, port, callback]
    )
    process.start()
    try:
        host, port = reader.recv()
        yield host, port
    finally:
        process.terminate()
        process.join()


@testenv
def local(ok_expected, cn, callback=https_callback):
    certdata, keydata, cadata = gencert(cn)

    with mock_server(certdata, keydata, callback=callback) as (host, port):
        with tmpfiles(cadata) as cafile:
            yield ok_expected, host, port, cafile
