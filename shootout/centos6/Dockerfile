FROM centos:centos6

ENV VERSION 0.3.4
RUN yum -y update && \
    yum -y install epel-release && \
    yum -y install python-pip && \
    yum -y install openssl && \
    yum clean all

# trytls pip install deferred to python3 due to argparse requirement

# Stubs
WORKDIR /root
RUN curl -Lo- https://github.com/ouspg/trytls/archive/v${VERSION}.tar.gz | \
  zcat | tar --strip-components=1 -xvf - trytls-${VERSION}/stubs

# Go
RUN yum -y install go
WORKDIR /root/stubs/go-nethttp
RUN go build run.go

# Java
RUN yum -y install java-sdk
WORKDIR /root/stubs/java-https
RUN javac Run.java
WORKDIR /root/stubs/java-net
RUN javac Run.java

# Python 2
RUN yum -y install python-requests

# Python 3
RUN yum -y install centos-release-scl scl-utils
RUN yum -y install rh-python34 && \
      scl enable rh-python34 "pip install trytls==${VERSION}"

# PHP
RUN yum -y install php

# Default workdir & script for easier manual stub testing
WORKDIR /root/stubs/
COPY shootout.sh /root/stubs/
