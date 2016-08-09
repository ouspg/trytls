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

WORKDIR /tmp
RUN curl -Lo- https://github.com/ouspg/trytls/archive/v0.2.0.tar.gz | gunzip -c - | tar xvf - trytls-0.2.0/stubs/

# Go
RUN apk add go
WORKDIR /tmp/trytls-0.2.0/stubs/go-nethttp
RUN go build run.go

# Java
RUN apk add openjdk8
WORKDIR /tmp/trytls-0.2.0/stubs/java-https
RUN /usr/lib/jvm/java-1.8-openjdk/bin/javac Run.java
WORKDIR /tmp/trytls-0.2.0/stubs/java-net
RUN /usr/lib/jvm/java-1.8-openjdk/bin/javac Run.java

# Python 3
RUN apk add python3

# PHP 5
RUN apk add php5
