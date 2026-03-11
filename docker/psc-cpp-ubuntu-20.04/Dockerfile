FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get -y install --no-install-recommends \
    # apt-transport-https \
    # ca-certificates \
    # gnupg \
    # wget \
    # software-properties-common \
    cmake \
    ninja-build \
    gcc g++ \
    libopenmpi-dev \
    libhdf5-openmpi-dev \
    libadios2-mpi-c++11-dev libadios2-mpi-c-dev \
    && rm -rf /var/lib/apt/lists/*
