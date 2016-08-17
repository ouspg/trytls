FROM fedora:24

ENV VERSION 0.3.4
RUN dnf install tar openssl python-pip -y && \
  pip install trytls==${VERSION}

WORKDIR /root
RUN curl -Lo- https://github.com/ouspg/trytls/archive/v${VERSION}.tar.gz | \
  zcat - | tar --strip-components=1 -xvf - trytls-${VERSION}/stubs/

# Go
RUN dnf install go -y
WORKDIR /root/stubs/go-nethttp
RUN go build run.go

# Java

RUN dnf install java-1.8.0-openjdk-devel -y
WORKDIR /root/stubs/java-https
RUN javac Run.java
WORKDIR /root/stubs/java-net
RUN javac Run.java

# Python 2
RUN dnf install python-requests -y

# Python 3
RUN dnf install python3 python3-requests -y

# PHP 5
RUN dnf install php -y

# Default workdir & script for easier manual stub testing
WORKDIR /root/stubs/
COPY shootout.sh /root/stubs/
