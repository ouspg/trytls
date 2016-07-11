FROM fpco/stack-build

ENV HOME /home/_stack

WORKDIR /builder
COPY . /builder/
RUN chown -R stack:stack ${HOME} /builder
USER stack

RUN stack setup
RUN stack build

ENTRYPOINT ["stack", "exec", "test-http-client-tls"]
