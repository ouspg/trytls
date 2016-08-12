FROM ubuntu:12.04.5

RUN apt-get -y update && \
  apt-get -y install \
  default-jre

COPY scripts /scripts

CMD bash scripts/init; bash '/etc/shared/scripts/drive'
