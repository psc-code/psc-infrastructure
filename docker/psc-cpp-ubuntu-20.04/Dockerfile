FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get -y install --no-install-recommends \
    libopenmpi-dev ninja-build \
    apt-transport-https ca-certificates gnupg software-properties-common wget \
    libhdf5-openmpi-dev \
    libadios2-mpi-c++11-dev libadios2-mpi-c-dev \
    cmake
