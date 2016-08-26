from __future__ import absolute_import, print_function, unicode_literals

import sys
import contextlib
from colorama import Fore, Back, Style, init, AnsiToWin32

from .. import utils, results
from ._utils import indent


@contextlib.contextmanager
def formatter(stream):
    yield DefaultFormatter(stream)


class DefaultFormatter(object):
    def __init__(self, stream):
        # Initialize colorama without wrapping sys.stdout globally
        init(wrap=False)
        self._stream = AnsiToWin32(sys.stdout, autoreset=True).stream

    def _write(self, *strings):
        for s in strings:
            print(s, file=self._stream)

    def write_platform(self, platform):
        self._write(colorize("{Style.BRIGHT}platform:{RESET} {}", platform))

    def write_runner(self, runner):
        self._write(colorize("{Style.BRIGHT}runner:{RESET} {}", runner))

    def write_stub(self, args):
        self._write(colorize("{Style.BRIGHT}stub:{RESET} {}", utils.format_command(args)))

    @contextlib.contextmanager
    def tests(self):
        yield self

    def write_test(self, test, result):
        formatter = formats.get(result.type)
        if formatter is None:
            raise RuntimeError("unknown result type")
        self._write(formatter.format(test, result))


def colorize(format_string, *args, **kwargs):
    keys = dict(Fore=Fore, Back=Back, Style=Style, RESET=Style.RESET_ALL)
    keys.update(kwargs)
    return format_string.format(*args, **keys)


class Format(object):
    def __init__(self, base="", type="", reason="", details=""):
        self.base = base
        self.type = type
        self.reason = reason
        self.details = details

    def _colorize(self, format_string, *args, **kwargs):
        keys = dict(Formatter=self)
        keys.update(**kwargs)
        return colorize(format_string, *args, **keys)

    def format(self, test, res):
        result = self._colorize(
            "{Formatter.base}{Formatter.type}{result:>5}{RESET}{Formatter.base} {description} {Style.DIM}[{accept} {name}]",
            result=res.name,
            description=test.description,
            accept="accept" if test.accept else "reject",
            name=test.name
        )

        reason = res.reason.rstrip()
        if reason:
            result += self._colorize("{RESET}{Formatter.base}\n")
            result += indent("reason: ", by=6)
            result += indent(self._colorize("{Formatter.reason}{}", reason), by=14, first_line=False)

        details = res.details.rstrip()
        if details:
            result += self._colorize("{RESET}{Formatter.base}\n")
            result += indent("output: ", by=6)
            result += indent(self._colorize("{Formatter.details}{}", details), by=14, first_line=False)

        return result


formats = {
    results.Skip: Format(
        base=Style.DIM
    ),
    results.Error: Format(
        base=Fore.RED,
        type=Back.RED + Fore.WHITE,
        details=Style.DIM
    ),
    results.Fail: Format(
        base=Fore.RED,
        reason=Fore.RED + Style.DIM
    ),
    results.Pass: Format(
        type=Fore.GREEN,
        reason=Style.DIM,
        details=Style.DIM
    )
}
