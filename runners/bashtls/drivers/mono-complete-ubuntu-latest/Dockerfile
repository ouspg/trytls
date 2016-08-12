FROM ubuntu:16.04

RUN apt-get -y update && \
  apt-get -y install \
  mono-complete

COPY scripts /scripts

CMD bash scripts/init; bash '/etc/shared/scripts/drive'
