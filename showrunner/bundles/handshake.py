from ..testenv import badssl, local


badssl_tests = [
    badssl(True, "sha1-2016"),
    badssl(False, "expired")
]


local_tests = [
    local(True, "localhost"),
    local(False, "nothing")
]


all_tests = badssl_tests + local_tests
