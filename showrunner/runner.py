from __future__ import print_function

import subprocess


class ProcessFailed(Exception):
    pass


class UnexpectedOutput(Exception):
    pass


def run_one(args, host, port, ca_cert=None):
    args = args + [host, str(port)]
    if ca_cert is not None:
        args.append(ca_cert)

    process = subprocess.Popen(
        args,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    stdout, _ = process.communicate()

    if process.returncode != 0:
        raise ProcessFailed()

    if stdout.strip() == "OK":
        return True
    if stdout.strip() == "FAIL":
        return False
    raise UnexpectedOutput()


def run(args, tests):
    for test in tests:
        with test() as (ok_expected, host, port, ca_cert):
            ok = run_one(list(args), host, port, ca_cert)
            if bool(ok) == bool(ok_expected):
                print("PASS", test)
            else:
                print("ERROR", test)


def main():
    import argparse
    from .testenv import badssl

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
        badssl(False, "expired")
    ])
