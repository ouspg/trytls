FROM debian:8
WORKDIR /root
ENV VERSION 0.2.1
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y -o acquire::retries=10 install \
        python python-pip curl vim \
        python3-requests python-requests php5 default-jdk golang-go && \
    pip install trytls==${VERSION} && \
    curl -Lo- https://github.com/ouspg/trytls/archive/v${VERSION}.tar.gz \
        | zcat - | tar xvf - trytls-${VERSION}/stubs/ && \
    javac trytls-${VERSION}/stubs/java-https/Run.java  && \
    javac trytls-${VERSION}/stubs/java-net/Run.java

COPY shootout.sh /root/
