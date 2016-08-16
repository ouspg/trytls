FROM fedora:24

RUN dnf install git-all tar -y
RUN pip install trytls

WORKDIR /root
ENV VERSION 0.3.0
RUN curl -Lo- https://github.com/ouspg/trytls/archive/v${VERSION}.tar.gz | zcat - | tar xvf - trytls-${VERSION}/stubs/
RUN mv trytls-${VERSION} trytls

# Go
RUN dnf install go -y
WORKDIR /root/trytls/stubs/go-nethttp
RUN go build run.go

# Java

RUN dnf install java-1.8.0-openjdk-devel -y
WORKDIR /root/trytls/stubs/java-https
RUN javac Run.java
WORKDIR /root/trytls/stubs/java-net
RUN javac Run.java

# Python 2
RUN dnf install python-requests -y

# Python 3
RUN dnf install python3 python3-requests -y

# PHP 5
RUN dnf install php -y

WORKDIR /root/trytls/stubs/
