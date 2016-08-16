FROM debian:7
WORKDIR /root
ENV VERSION 0.3.0
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
    pip3.5 install https://github.com/ouspg/trytls/archive/v${VERSION}.tar.gz && \
    cd /root && \
    curl -Lo- https://github.com/ouspg/trytls/archive/v${VERSION}.tar.gz \
        | zcat - | tar xvf - trytls-${VERSION}/stubs/ && \
    javac trytls-${VERSION}/stubs/java-https/Run.java  && \
    javac trytls-${VERSION}/stubs/java-net/Run.java

COPY shootout.sh /root/
