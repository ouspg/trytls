FROM fedora:latest

RUN dnf -y update && \
  dnf -y install \
  python-pip \
  bash

RUN pip install --upgrade pip
RUN pip install \
  request \
  certifi

CMD cat /etc/issue; python3 -V;bash '/etc/shared/scripts/drive'
