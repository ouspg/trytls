FROM ubuntu:14.04

RUN apt-get -y update && \
  apt-get -y install \
  lua5.1 \
  luarocks \
  openssl \
  libssl-dev \
  git

RUN luarocks install luasocket
RUN luarocks install luasec

CMD bash '/etc/shared/scripts/drive'
