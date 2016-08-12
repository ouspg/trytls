FROM ubuntu:12.04.5

RUN apt-get -y update && \
  apt-get -y install \
  python \
  python-pip

RUN pip install \
  requests \
  urllib3 \
  certifi

CMD bash '/etc/shared/scripts/drive'
#CMD cat /stubs/python3-urllib/run.py
