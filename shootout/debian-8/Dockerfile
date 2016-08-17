FROM debian:8
WORKDIR /root
ENV VERSION 0.3.3
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y -o acquire::retries=10 install \
        python python-pip curl vim \
        python3-requests python-requests php5 default-jdk golang-go && \
    pip install trytls==${VERSION} && \
    curl -Lo- https://github.com/ouspg/trytls/archive/v${VERSION}.tar.gz \
        | zcat - | tar --strip-components=1 -xvf - trytls-${VERSION}/stubs &&\
    cd /root/stubs/go-nethttp/ && \
    go build run.go && \
    javac /root/stubs/java-https/Run.java  && \
    javac /root/stubs/java-net/Run.java


WORKDIR /root/stubs
COPY shootout.sh /root/stubs/
