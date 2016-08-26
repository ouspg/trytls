from __future__ import absolute_import, print_function, unicode_literals

import json
import contextlib

from ._utils import indent


@contextlib.contextmanager
def formatter(stream):
    stream.write("{\n")
    yield JSONFormatter(stream)
    stream.write("\n}\n")
    stream.flush()


class JSONFormatter(object):
    def __init__(self, stream):
        self._stream = stream
        self._open = False

    def _open_property(self, name):
        if self._open:
            self._stream.write(",\n")
        self._stream.write("    " + json.dumps(name) + ": ")
        self._open = True

    def _write_property(self, name, value):
        self._open_property(name)
        self._stream.write(json.dumps(value))

    def write_platform(self, platform):
        self._write_property("platform", platform)

    def write_runner(self, runner):
        self._write_property("runner", runner)

    def write_stub(self, args):
        self._write_property("stub", args)

    @contextlib.contextmanager
    def tests(self):
        self._open_property("tests")
        self._stream.write("[\n")
        yield JSONFormatter(self._stream)
        self._stream.write("\n    ]")

    def write_test(self, test, result):
        if self._open:
            self._stream.write(",\n")
            self._stream.flush()

        obj = {
            "result": result.name,
            "description": test.description,
            "target": "{} {}".format("accept" if test.accept else "reject", test.name),
        }
        reason = result.reason.rstrip()
        if reason:
            obj["reason"] = reason
        details = result.details.rstrip()
        if details:
            obj["details"] = details

        self._stream.write(indent(json.dumps(obj, indent=4), 8))
        self._stream.flush()
        self._open = True
