FROM ubuntu:16.04

RUN apt-get -y update && \
  apt-get -y install \
  default-jre

#language = java
#driver = java
#stubs = java.stubs
#run = Run(.class)
#confs = java = driver

COPY scripts /scripts

CMD bash scripts/init; bash '/etc/shared/scripts/run' '/etc/shared/simplerunner/stubs/java.stubs' \
  'java' 'Run' 'default' '_' 'cd' 30
