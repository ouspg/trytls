FROM centos:centos5

RUN yum -y update && \
    yum -y install epel-release && \
    yum -y install python-pip && \
    yum -y install openssl && \
    yum -y install curl && \
    yum clean all

# trytls pip install deferred to python3 due to argparse requirement

# Stubs
WORKDIR /root
RUN curl -Lo- https://github.com/ouspg/trytls/archive/v0.2.1.tar.gz | \
  zcat | tar --strip-components=1 -xvf - trytls-0.2.1/stubs

# No Go in CentOS 5

# Java too old to compile the stubs in CentOS 5

# Python 2
RUN yum -y install python-requests

# No Python 3 in CentOS 5

# PHP
RUN yum -y install php

# Default workdir for easier manual stub testing
WORKDIR /root/stubs/
