from __future__ import print_function

import argparse
import importlib
import subprocess

from . import bundles


class Unsupported(Exception):
    pass


class ProcessFailed(Exception):
    pass


class UnexpectedOutput(Exception):
    pass


def indent(text, indent):
    r"""
    >>> indent("a\nb\nc", indent="    ")
    '    a\n    b\n    c'
    """

    lines = text.splitlines(True)
    return "".join(indent + line for line in lines)


def run_one(args, host, port, cafile=None):
    args = args + [host, str(port)]
    if cafile is not None:
        args.append(cafile)

    process = subprocess.Popen(
        args,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        raise ProcessFailed(process.returncode, stderr)

    output = stdout.strip()
    if output == b"VERIFY SUCCESS":
        return True
    if output == b"VERIFY FAILURE":
        return False
    if output == b"UNSUPPORTED":
        raise Unsupported()
    raise UnexpectedOutput(output)


def run(args, tests):
    for test in tests:
        with test() as (ok_expected, host, port, cafile):
            try:
                ok = run_one(list(args), host, port, cafile)
            except Unsupported:
                print("SKIP", test)
            except UnexpectedOutput as uo:
                output = uo.args[0].decode("ascii", "replace")
                print("ERROR unexpected output:\n{}".format(indent(output, " " * 4)))
            except ProcessFailed as pf:
                print("ERROR process exited with return code {}".format(pf.args[0]))
                stderr = pf.args[1]
                if stderr:
                    print(indent(stderr, " " * 4).decode("ascii", "replace"))
            else:
                if bool(ok) == bool(ok_expected):
                    print("PASS", test)
                else:
                    print("FAIL", test)


def module_path(string):
    string = string.strip()
    if string.startswith("."):
        string = bundles.__name__ + string

    pieces = string.split(".")
    name = pieces.pop()
    path = ".".join(pieces)
    try:
        module = importlib.import_module(path, package=__package__)
    except ImportError as err:
        raise argparse.ArgumentTypeError(str(err))

    try:
        return getattr(module, name)
    except AttributeError as err:
        raise argparse.ArgumentTypeError(str(err))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "command",
        metavar="COMMAND",
        help="the command to run"
    )
    parser.add_argument(
        "args",
        metavar="ARG",
        nargs="*",
        help="additional argument for the command"
    )
    parser.add_argument(
        "-t",
        "--test-bundle",
        metavar="BUNDLE",
        default=".handshake.all_tests",
        type=module_path,
        help="path to the bundle of tests to run"
    )
    args = parser.parse_args()

    run([args.command] + args.args, args.test_bundle)


if __name__ == "__main__":
    main()
