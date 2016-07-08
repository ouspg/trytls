FROM ubuntu:16.04

RUN apt-get -y update && \
  apt-get -y install \
  python3 \
  python-pip


#language = python3
#driver = python3_1
#stubs = python3.stubs = language.stubs
#run = run.py
#confs = python3_1 = driver

CMD bash '/etc/shared/scripts/run' '/etc/shared/simplerunner/stubs/python3.stubs' \
  'python3' 'run.py' 'default' '/etc/shared/simplerunner/certs'
