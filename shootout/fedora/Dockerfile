FROM fedora:latest

RUN dnf install git-all tar -y
RUN pip install trytls

WORKDIR /tmp
RUN git clone https://github.com/ouspg/trytls.git

# Go
RUN dnf install go -y
WORKDIR /tmp/trytls-0.2.0/stubs/go-nethttp
RUN go build run.go


# Python 3
RUN dnf install python3 -y

# PHP 5
RUN dnf install php5 -y
