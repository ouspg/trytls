FROM  php:latest

RUN   apt-get update -y && \
      apt-get install git \
      python-pip -y

RUN   git clone https://github.com/ouspg/trytls.git && \
      cd trytls && \
      pip install .
