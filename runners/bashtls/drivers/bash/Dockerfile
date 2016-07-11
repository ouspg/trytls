FROM ubuntu:16.04

RUN apt-get -y update && \
  apt-get -y install \
  curl

#language = bash
#driver = bash
#stubs = bash.stubs = language.stubs
#run = run
#confs = bash = driver

CMD bash '/etc/shared/scripts/run' '/etc/shared/simplerunner/stubs/bash.stubs' \
  'bash' 'run' 'default' '/etc/shared/simplerunner/certs'
