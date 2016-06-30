FROM ubuntu:latest

ENV GHC_VERSION 8.0.1
ENV CABAL_VERSION 1.24

# https://launchpad.net/~hvr/+archive/ubuntu/ghc
COPY docker/hvr-ghc.list /etc/apt/sources.list.d/
COPY docker/hvr-ghc.key /tmp
RUN apt-key add /tmp/hvr-ghc.key && rm /tmp/hvr-ghc.key

# GHC and requirements
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install \
        cabal-install-${CABAL_VERSION} \
        ghc-${GHC_VERSION} \
        ca-certificates \
        libz-dev \
        netbase

ENV PATH /opt/ghc/${GHC_VERSION}/bin/:/opt/cabal/${CABAL_VERSION}/bin/:${PATH}

RUN useradd -c "Curry Monad" -m haskell
USER haskell
ENV HOME /home/haskell

# Install `wreq` so changes don't trigger the full rebuild of all
# dependencies
RUN cabal update && cabal install wreq

WORKDIR ${HOME}
COPY . ${HOME}
RUN cabal install

ENV PATH ${HOME}/.cabal/bin:${PATH}

ENTRYPOINT ["test-wreq"]
