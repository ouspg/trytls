FROM ubuntu:16.04

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install python-pip curl

WORKDIR /root
RUN apt-get -y install git
RUN git clone https://github.com/ouspg/trytls.git

WORKDIR /root/trytls
RUN pip install .

# Go
RUN apt-get -y install golang-go
WORKDIR /root/trytls/stubs/go-nethttp
RUN go build run.go

# Java
RUN apt-get -y install default-jdk
WORKDIR /root/trytls/stubs/java-https
RUN javac Run.java
WORKDIR /root/trytls/stubs/java-net
RUN javac Run.java

# Python 2
RUN apt-get -y install python-requests

# Python 3
RUN apt-get -y install python3

# PHP
RUN apt-get -y install php

# Default workdir for easier manual stub testing
WORKDIR /root/trytls/stubs/
