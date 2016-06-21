from __future__ import print_function

import sys
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
    from .testenv import badssl

    run(sys.argv[1:], [
        badssl(True, "sha1-2016"),
        badssl(False, "expired")
    ])
