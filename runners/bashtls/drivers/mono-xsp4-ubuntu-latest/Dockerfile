FROM ubuntu:latest

RUN apt-get -y --allow-unauthenticated update && \
  apt-get -y  --allow-unauthenticated install \
  mono-xsp4

COPY scripts /scripts

CMD bash scripts/init; bash '/etc/shared/scripts/drive'
