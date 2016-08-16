FROM ubuntu:12.04

ENV VERSION 0.3.0
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install curl

# Stubs
WORKDIR /root
RUN curl -Lo- https://github.com/ouspg/trytls/archive/v${VERSION}.tar.gz | \
  zcat | tar --strip-components=1 -xvf - trytls-${VERSION}/stubs

# Go
RUN apt-get -y install golang-go
WORKDIR /root/stubs/go-nethttp
RUN go build run.go

# Java too old to compile the stubs in Ubuntu 12.04 LTS

# Python 2
RUN apt-get -y install python-requests

# Python 3
RUN apt-get -y install python3

# PHP
RUN apt-get -y install php5

# Default workdir for easier manual stub testing
WORKDIR /root/stubs/
