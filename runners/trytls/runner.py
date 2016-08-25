from __future__ import print_function, unicode_literals

import re
import os
import sys
import string
import argparse
import subprocess

from . import __version__, utils, results, bundles, testenv, formatters


class Unsupported(Exception):
    pass


class ProcessFailed(Exception):
    pass


class UnexpectedOutput(Exception):
    pass


def output_info(formatter, args, runner_name="trytls"):
    formatter.write_platform(utils.platform_info())
    formatter.write_runner("{runner} {version} ({python})".format(
        runner=runner_name,
        version=__version__,
        python=utils.python_info()
    ))
    formatter.write_stub(args)


# A regex that matches to any byte that is not a 7-bit ASCII printable.
_NON_PRINTABLE_REX = re.compile(
    b"[^" + b"".join(re.escape(x).encode("ascii") for x in string.printable) + b"]"
)


def _escape_match(match):
    return "\\x{:02x}".format(ord(match.group(0))).encode("ascii")


def _escape_non_printable(byte_string):
    r"""
    Return the byte string, escaping all bytes outside printable
    7-bit ASCII.

    >>> _escape_non_printable(b"Hello, World!") == b"Hello, World!"
    True

    Non-printables are \xNN-escaped.

    >>> _escape_non_printable(b"\x00\xff") == b"\\x00\\xff"
    True
    """

    return _NON_PRINTABLE_REX.sub(_escape_match, byte_string)


def run_stub(args, host, port, cafile=None):
    args = args + [host, str(port)]
    if cafile is not None:
        args.append(cafile)

    try:
        process = subprocess.Popen(
            args,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
    except OSError as ose:
        raise ProcessFailed("failed to launch the stub", os.strerror(ose.errno))

    out, _ = process.communicate()
    out = _escape_non_printable(out).decode("ascii")

    if process.returncode != 0:
        raise ProcessFailed("stub exited with return code {}".format(process.returncode), out)

    out = out.rstrip()
    lines = out.splitlines()
    if lines:
        verdict = lines.pop()
        if verdict == "ACCEPT":
            return True, "".join(lines)
        elif verdict == "REJECT":
            return False, "".join(lines)
        elif verdict == "UNSUPPORTED":
            raise Unsupported("".join(lines))
    raise UnexpectedOutput(out)


def collect(test, args):
    try:
        accept, details = run_stub(list(args), test.host, test.port, test.cafile)
    except Unsupported as us:
        return results.Skip(
            reason="the stub couldn't implement the requested behaviour (e.g. setting CA certificate bundle)",
            details=us.args[0])
    except UnexpectedOutput as uo:
        output = uo.args[0].strip()
        if output:
            return results.Error("unexpected output", output)
        return results.Error("no output")
    except ProcessFailed as pf:
        return results.Error(pf.args[0], pf.args[1])

    if accept and test.accept:
        return results.Pass(details=details)
    elif not accept and not test.accept:
        return results.Pass(details=details)
    elif not accept and test.accept:
        return results.Fail(details=details)
    else:
        return results.Fail(details=details)


def run(formatter, args, tests):
    fail_count = 0
    error_count = 0

    with formatter.tests() as writer:
        for test, result in testenv.run(tests, collect, args):
            writer.write_test(test, result)

            if result.type == results.Fail:
                fail_count += 1
            elif result.type == results.Error:
                error_count += 1

    return fail_count == 0 and error_count == 0


def main():
    parser = argparse.ArgumentParser(
        usage="%(prog)s bundle command [arg ...]"
    )
    parser.add_argument(
        "remainder",
        help=argparse.SUPPRESS,
        nargs=argparse.REMAINDER
    )

    args = parser.parse_args()
    if args.remainder and args.remainder[0] == "--":
        args.remainder.pop(0)
    bundle_name = args.remainder[0] if args.remainder else None

    parser.add_argument(
        "--formatter",
        help="formatter",
        default="default"
    )
    args = parser.parse_args(args.remainder[1:], args)
    if args.remainder and args.remainder[0] == "--":
        args.remainder.pop(0)
    command = args.remainder

    create_formatter = formatters.load_formatter(args.formatter)
    if create_formatter is None:
        formatter_list = ["  " + x for x in sorted(formatters.iter_formatters())]
        parser.error(
            "unknown formatter '{}'\n\n".format(args.formatter) +
            "Valid formatter options:\n" + "\n".join(formatter_list)
        )

    if bundle_name is None:
        bundle_list = ["  " + x for x in sorted(bundles.iter_bundles())]
        parser.error(
            "missing the bundle argument\n\n" +
            "Valid bundle options:\n" + "\n".join(bundle_list)
        )

    bundle = bundles.load_bundle(bundle_name)
    if bundle is None:
        parser.error("unknown bundle '{}'".format(bundle_name))

    if not command:
        parser.error("too few arguments, missing command")

    with create_formatter(sys.stdout) as formatter:
        output_info(formatter, command)
        if not run(formatter, command, bundle):
            # Return with a non-zero exit code if all tests were not successful. The
            # CPython interpreter exits with 1 when an unhandled exception occurs,
            # and with 2 when there is a problem with a command line parameter. The
            # argparse module also uses the code 2 for the same purpose. Therefore
            # the chosen return value here is 3.
            return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
