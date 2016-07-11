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
        netbase \
        git

ENV PATH /opt/ghc/${GHC_VERSION}/bin/:/opt/cabal/${CABAL_VERSION}/bin/:${PATH}

RUN useradd -c "Curry Monad" -m haskell
USER haskell
ENV HOME /home/haskell

WORKDIR ${HOME}

# Install customized x509 packages
RUN cabal update
RUN git clone -b custom-ca-bundle-reading --depth=1 \
    https://github.com/oherrala/hs-certificate && \
    cd hs-certificate && \
    for i in x509 x509-store x509-system x509-validation; do (cd $i; cabal install --force-reinstall); done

# Install `wreq` so changes don't trigger the full rebuild of all
# dependencies
RUN cabal update && cabal install wreq

WORKDIR ${HOME}
COPY . ${HOME}
RUN cabal install

ENV PATH ${HOME}/.cabal/bin:${PATH}

ENTRYPOINT ["test-http-client-tls"]
