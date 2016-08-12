FROM debian:latest

RUN apt-get -y update && \
  apt-get -y install \
  python3 \
  python-pip

CMD python3 -V;bash '/etc/shared/scripts/drive'
