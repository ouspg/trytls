FROM debian:7
WORKDIR /root
ENV VERSION 0.3.4
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y -o acquire::retries=10 install \
        python python-pip python3-pip curl vim \
        python3-requests python-requests php5 default-jdk golang-go && \
    mkdir src && \
    cd src && \
    curl https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz \
        >Python-3.5.2.tgz && \
    tar -xzvf Python-3.5.2.tgz && \
    cd Python-3.5.2 && \
    ./configure && \
    make && \
    make install && \
    pip3.5 install --upgrade pip && \
    pip3.5 install trytls==v${VERSION} && \
    cd /root && \
    curl -Lo- https://github.com/ouspg/trytls/archive/v${VERSION}.tar.gz \
        | zcat - | tar --strip-components=1 -xvf - trytls-${VERSION}/stubs && \
    cd /root/stubs/go-nethttp/ && \
    go build run.go && \
    javac /root/stubs/java-https/Run.java  && \
    javac /root/stubs/java-net/Run.java

WORKDIR /root/stubs
COPY shootout.sh /root/stubs/
