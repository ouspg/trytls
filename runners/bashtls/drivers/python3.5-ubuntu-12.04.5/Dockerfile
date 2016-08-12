FROM ubuntu:12.04.5

RUN apt-get -y update && \
  apt-get -y install \
  software-properties-common

RUN add-apt-repository ppa:fkrull/deadsnakes
RUN apt-get -y update && \
  apt-get -y install \
  python3.5 \
  python-pip

CMD bash '/etc/shared/scripts/drive'
