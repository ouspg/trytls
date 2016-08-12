FROM ubuntu:14.04

RUN apt-get -y update && \
  apt-get -y install \
  python \
  python-pip

RUN pip install \
  requests \
  urllib3 \
  certifi


CMD python -V;bash '/etc/shared/scripts/drive'
