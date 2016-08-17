FROM alpine:edge

RUN apk -U upgrade && \
    apk add \
        build-base \
        curl \
        openssl \
        py-pip \
        python \
    && \
    pip install trytls

WORKDIR /root
ENV VERSION 0.3.3
RUN curl -Lo- https://github.com/ouspg/trytls/archive/v${VERSION}.tar.gz | zcat - | tar xvf - trytls-${VERSION}/stubs/
RUN mv trytls-${VERSION} trytls

# Go
RUN apk add go
WORKDIR /root/trytls/stubs/go-nethttp
RUN go build run.go

# Java
RUN apk add openjdk8
WORKDIR /root/trytls/stubs/java-https
RUN /usr/lib/jvm/java-1.8-openjdk/bin/javac Run.java
WORKDIR /root/trytls/stubs/java-net
RUN /usr/lib/jvm/java-1.8-openjdk/bin/javac Run.java

# Python 2
RUN apk add py-requests

# Python 3
RUN apk add python3 && \
    pip3 install requests

# PHP 5
RUN apk add php5

# Default workdir for easier manual stub testing
WORKDIR /root/trytls/stubs/
