FROM ubuntu:14.04

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install python-pip curl && \
    pip install trytls==0.3.0

# Stubs
WORKDIR /root
RUN curl -Lo- https://github.com/ouspg/trytls/archive/v0.3.0.tar.gz | \
  zcat | tar --strip-components=1 -xvf - trytls-0.3.0/stubs

# Go
RUN apt-get -y install golang-go
WORKDIR /root/stubs/go-nethttp
RUN go build run.go

# Java
RUN apt-get -y install default-jdk
WORKDIR /root/stubs/java-https
RUN javac Run.java
WORKDIR /root/stubs/java-net
RUN javac Run.java

# Python 2
RUN apt-get -y install python-requests

# Python 3
RUN apt-get -y install python3

# PHP
RUN apt-get -y install php5

# Default workdir for easier manual stub testing
WORKDIR /root/stubs/
