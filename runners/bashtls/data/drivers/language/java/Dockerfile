FROM java:latest

copy init and run scripts into the image

COPY scripts /scripts

execute program (javac, etc..)
RUN bash scripts/init

#loop (java ..)
CMD bash scripts/run
