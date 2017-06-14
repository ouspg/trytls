FROM hhvm/hhvm

RUN apt-get -y update && \
    apt-get -y install \
        git \
        python-pip

RUN git clone https://github.com/ouspg/trytls.git --depth=1 && \
    cd trytls && \
    pip install .

COPY run.php .
CMD trytls https hhvm run.php
