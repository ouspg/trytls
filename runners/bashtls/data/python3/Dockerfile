FROM ubuntu:16.04

RUN apt-get -y update && \
  apt-get -y install \
  python3

CMD bash /etc/shared/scripts/run /etc/shared/simplerunner/stubs/python3.stubs run.py badssl_https_conf
