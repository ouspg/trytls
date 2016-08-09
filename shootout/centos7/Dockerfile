FROM centos:centos7

RUN yum -y update && \
    yum -y install epel-release && \
    yum -y install python-pip && \
    yum -y install openssl && \
    yum clean all && \
    pip install trytls

# Stubs
WORKDIR /root
RUN curl -Lo- https://github.com/ouspg/trytls/archive/v0.2.0.tar.gz | \
  zcat | tar --strip-components=1 -xvf - trytls-0.2.0/stubs

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
RUN yum -y install centos-release-scl scl-utils rh-python35

# PHP
RUN yum -y install php

# Default workdir for easier manual stub testing
WORKDIR /root/stubs/
