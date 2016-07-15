FROM  php:latest

RUN   apt-get update -y && \
      apt-get install git \
      python-pip -y

RUN   git clone https://github.com/ouspg/trytls.git --depth=1 && \
      cd trytls && \
      pip install .

COPY  run.php .
CMD trytls https php run.php
