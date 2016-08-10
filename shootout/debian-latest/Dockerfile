FROM debian:latest
WORKDIR /root
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y -o acquire::retries=10 install \
        python python-pip git \
        python3-requests python-requests php5 default-jdk && \
    pip install trytls && \
    git clone https://github.com/ouspg/trytls.git
