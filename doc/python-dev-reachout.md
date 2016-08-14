# Mail to the python-dev list

<!-- markdownlint-disable MD013 -->

```text

Hello,

We are experimenting with a tool for inspecting how well languages and
libraries support server certificate verification when establishing TLS
connections.

We are getting rather confusing results in our first major shootout of
bundled CPython 2 and 3 versions in major, still supported OS
distributions. We would love to get any insight into the test stubs and
results. Maybe we are doing something horribly wrong?

## Python 2 with Requests

Our stub code:
https://github.com/ouspg/trytls/blob/v0.2.1/stubs/python-requests/run.py

This is good news. All major distributions successfully check the TLS
certificates in all corner cases tested by the TryTLS. It was good news
that most distros also support SNI with this combination, the only
exceptions being CentOS 6.8, Ubuntu 12.04.5 and Ubuntu 14.04.

## Python 2 with urllib2

Our stub code:
https://github.com/ouspg/trytls/blob/v0.2.1/stubs/python-urllib2/run.py

Alpine Edge, Alpine 3.1, Debian 8.5, Fedora 24 and Ubuntu 16.04 pass
with flying colors.

On the other hand on CentOS 7.2 the test code accepts expired certificates,
wrong hostnames, self-signed certificates and incomplete chains of trust.
For CentOS 7.2 results see
https://github.com/ouspg/trytls/tree/shootout-0.2/shootout/centos7#python-urllib2

It's worth noting that when any CA-bundle is given the situation improves.
However, since the stub works on the most distributions as expected, this
might be overlooked by the developers?

## Python 3 with urllib

Our stub code:
https://github.com/ouspg/trytls/blob/v0.2.1/stubs/python3-urllib/run.py

Alpine Edge, CentOS 6.8, CentOS 7.2 and Ubuntu 16.04 pass with flying
colors.

On Debian 8.5, Ubuntu 14.04 and Ubuntu 12.04 the test code accepts
expired certificates, wrong hostnames, self-signed certificates and
incomplete chains of trust. For Debian 8.5 results see
https://github.com/ouspg/trytls/tree/shootout-0.2/shootout/debian-latest#python3-urllib

Again it is worth noting that if any CA-bundle is given then situation
improves. Some experimentation we did with the test code suggests
that:


urllib.request.urlopen("https://" + host + ":" + port, cafile=None) -> DANGEROUS?
urllib.request.urlopen("https://" + host + ":" + port) -> DANGEROUS?
urllib.request.urlopen("https://" + host + ":" + port, cafile=None, cadefault=False) -> DANGEROUS?
urllib.request.urlopen("https://" + host + ":" + port, cafile="/anyfile", cadefault=False) -> SAFE
urllib.request.urlopen("https://" + host + ":" + port, cafile=None, cadefault=True) -> SAFE
urllib.request.urlopen("https://" + host + ":" + port, cadefault=True) -> SAFE
urllib.request.urlopen("https://" + host + ":" + port, cafile="/anyfile") -> SAFE

## Summary

Our results overview is available from:
https://github.com/ouspg/trytls/tree/shootout-0.2/shootout

People developing Python code that uses TLS might bump into nasty
surprises with how differently bundled Python versions behave between
some still modern and supported distribution. Or are we just simply
doing something horribly wrong?

Any feedback would be very welcome, we will try to do an updated
shootout with new TryTLS version next week and would love to get
as fair, clean and comparable results as possible. Moreover, if you
can recommend any docs on proper Do's and Don'ts we'd love to link
to them.

Thank you very much,

```
