from __future__ import print_function, unicode_literals

import sys
import argparse
import subprocess
import pkg_resources
from colorama import Fore, Back, Style


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


def output(format_string, **kwargs):
    keys = dict(Fore=Fore, Back=Back, Style=Style, RESET=Style.RESET_ALL)
    keys.update(kwargs)
    print(format_string.format(**keys) + Style.RESET_ALL)


def run_one(args, host, port, cafile=None):
    args = args + [host, str(port)]
    if cafile is not None:
        args.append(cafile)

    process = subprocess.Popen(
        args,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
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
    fail_count = 0
    error_count = 0

    for test in tests:
        with test() as (ok_expected, host, port, cafile):
            try:
                ok = run_one(list(args), host, port, cafile)
            except Unsupported:
                output("  {Style.DIM}SKIP {test}", test=test)
            except UnexpectedOutput as uo:
                error_count += 1
                output(
                    "  {Back.RED}{Fore.WHITE}ERROR{RESET}{Fore.RED} unexpected output:\n{Fore.DIM}{error}",
                    error=indent(uo.args[0].decode("ascii", "replace"), " " * 4)
                )
            except ProcessFailed as pf:
                error_count += 1

                output(
                    "  {Back.RED}{Fore.WHITE}ERROR{RESET}{Fore.RED} process exited with return code {code}",
                    code=pf.args[0]
                )
                if pf.args[1]:
                    output(
                        "{Fore.RED}{Style.DIM}{error}",
                        error=indent(pf.args[1], " " * 4).rstrip().decode("ascii", "replace")
                    )
            else:
                if bool(ok) == bool(ok_expected):
                    output("  {Fore.GREEN}PASS{RESET} {test}", test=test)
                else:
                    fail_count += 1
                    output("{Fore.RED}\u2717 FAIL {test}", test=test)

    return fail_count == 0 and error_count == 0


def main():
    def iter_bundles():
        for entry in pkg_resources.iter_entry_points("trytls.bundles"):
            yield entry.name

    def load_bundle(name):
        for entry in pkg_resources.iter_entry_points("trytls.bundles", name):
            return entry.load()
        return None

    parser = argparse.ArgumentParser(
        usage="%(prog)s BUNDLE COMMAND [ARG ...]"
    )
    parser.add_argument(
        "bundle",
        metavar="BUNDLE",
        default=None,
        nargs="?",
        type=load_bundle
    )
    parser.add_argument(
        "command",
        metavar="COMMAND",
        help="the command to run",
        default=None,
        nargs="?"
    )
    parser.add_argument(
        "args",
        metavar="ARG",
        nargs="*",
        help="additional argument for the command"
    )

    args = parser.parse_args()
    if args.bundle is None:
        bundles = sorted(iter_bundles())
        parser.error("missing the bundle argument\n\nValid bundle options:\n" + indent("\n".join(bundles), " " * 2))

    if args.command is None:
        parser.error("too few arguments, missing command")

    if not run([args.command] + args.args, args.bundle):
        # Return with a non-zero exit code if all tests were not successful. The
        # CPython interpreter exits with 1 when an unhandled exception occurs,
        # and with 2 when there is a problem with a command line parameter. The
        # argparse module also uses the code 2 for the same purpose. Therefore
        # the chosen return value here is 3.
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
