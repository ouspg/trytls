from __future__ import print_function

import textwrap
import subprocess


class ProcessFailed(Exception):
    pass


class UnexpectedOutput(Exception):
    pass


def run_one(args, host, port, cafile=None):
    args = args + [host, str(port)]
    if cafile is not None:
        args.append(cafile)

    process = subprocess.Popen(
        args,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    stdout, _ = process.communicate()

    if process.returncode != 0:
        raise ProcessFailed(process.returncode)

    output = stdout.strip()
    if output == b"OK":
        return True
    if output == b"FAIL":
        return False
    raise UnexpectedOutput(output)


def run(args, tests):
    for test in tests:
        with test() as (ok_expected, host, port, cafile):
            try:
                ok = run_one(list(args), host, port, cafile)
            except UnexpectedOutput as uo:
                output = uo.args[0].decode("ascii", "backslashreplace")
                print("ERROR unexpected output:\n{}".format(textwrap.indent(output, " " * 4)))
            except ProcessFailed as pf:
                print("ERROR process exited with return code {}".format(pf.args[0]))
            else:
                if bool(ok) == bool(ok_expected):
                    print("PASS", test)
                else:
                    print("FAIL", test)


def main():
    import argparse
    from .testenv import badssl, local

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
    args = parser.parse_args()

    run([args.command] + args.args, [
        badssl(True, "sha1-2016"),
        badssl(False, "expired"),
        local(True, "localhost"),
        local(False, "nothing")
    ])
