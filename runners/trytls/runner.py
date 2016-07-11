from __future__ import print_function, unicode_literals

import sys
import gencert
import platform
import argparse
import subprocess
import pkg_resources
from colorama import Fore, Back, Style, init, AnsiToWin32

try:
    from shlex import quote as shlex_quote
except ImportError:
    def shlex_quote(string):
        if string.isalnum():
            return string
        return "'" + string.replace("'", "\\'") + "'"

from . import __version__


# Initialize colorama without wrapping sys.stdout globally
init(wrap=False)
wrapped_stdout = AnsiToWin32(sys.stdout, autoreset=True).stream


def output(format_string="", **kwargs):
    keys = dict(Fore=Fore, Back=Back, Style=Style, RESET=Style.RESET_ALL)
    keys.update(kwargs)
    print(format_string.format(**keys), file=wrapped_stdout)


class Unsupported(Exception):
    pass


class ProcessFailed(Exception):
    pass


class UnexpectedOutput(Exception):
    pass


def indent(text, by=4):
    r"""
    >>> indent("a\nb\nc", by=1) == ' a\n b\n c'
    True
    """

    spaces = " " * by
    lines = text.splitlines(True)
    return "".join(spaces + line for line in lines)


def python_info():
    return platform.python_implementation() + " " + platform.python_version()


def platform_info():
    if sys.platform == "linux2":
        distname, version, _ = platform.linux_distribution()
        if not distname:
            return "Linux"
        if not version:
            return "Linux ({})".format(distname)
        return "Linux ({} {})".format(distname, version)
    elif sys.platform == "darwin":
        version, _, _ = platform.mac_ver()
        if version.startswith("10."):
            return "OS X {}".format(version)
        return "Darwin"
    return platform.system()


def format_command(args):
    return " ".join(map(shlex_quote, args))


def output_info(args, openssl_version, runner_name="trytls"):
    output(
        "{Style.BRIGHT}platform:{RESET} {platform}",
        platform=platform_info()
    )
    output(
        "{Style.BRIGHT}runner:{RESET} {runner} {version} ({python}, {openssl})",
        runner=runner_name,
        version=__version__,
        python=python_info(),
        openssl=openssl_version
    )
    output(
        "{Style.BRIGHT}stub:{RESET} {command}",
        command=format_command(args)
    )


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
                    "  {Back.RED}{Fore.WHITE}ERROR{RESET}{Fore.RED} unexpected output:\n{Style.DIM}{error}",
                    error=indent(uo.args[0].decode("ascii", "replace"))
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
                        error=indent(pf.args[1]).rstrip().decode("ascii", "replace")
                    )
            else:
                if bool(ok) == bool(ok_expected):
                    output("  {Fore.GREEN}PASS{RESET} {test}", test=test)
                else:
                    fail_count += 1
                    output("{Fore.RED}x FAIL {test}", test=test)

    return fail_count == 0 and error_count == 0


def main():
    def iter_bundles():
        for entry in pkg_resources.iter_entry_points("trytls.bundles"):
            yield entry.name

    def load_bundle(name):
        for entry in pkg_resources.iter_entry_points("trytls.bundles", name):
            return entry.load()
        return None

    try:
        openssl_version = gencert.openssl_version()
    except gencert.OpenSSLNotFound as err:
        output("{Back.RED}{Fore.WHITE}ERROR:{RESET} {error}", error=err)
        return 1

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
        parser.error("missing the bundle argument\n\nValid bundle options:\n" + indent("\n".join(bundles), 2))

    if args.command is None:
        parser.error("too few arguments, missing command")

    output_info([args.command] + args.args, openssl_version=openssl_version)
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
