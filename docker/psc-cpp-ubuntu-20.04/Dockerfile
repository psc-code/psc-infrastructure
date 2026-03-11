# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.166.1/containers/cpp/.devcontainer/base.Dockerfile

# [Choice] Debian / Ubuntu version: debian-10, debian-9, ubuntu-20.04, ubuntu-18.04
ARG VARIANT="ubuntu-20.04"
FROM mcr.microsoft.com/vscode/devcontainers/cpp:0-${VARIANT}

# [Optional] Uncomment this section to install additional packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    libopenmpi-dev ninja-build \
    apt-transport-https ca-certificates gnupg software-properties-common wget \
    libhdf5-openmpi-dev \
    libadios2-mpi-c++11-dev libadios2-mpi-c-dev

# cmake version 3.21 is gtensor's lower bound as of March 11 2026;
# it would probably work just as well to use the "latest" cmake, but
# Docker caches RUN commands and will use the cached "latest" cmake indefinitely
RUN wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc  \
    | gpg --dearmor - > /etc/apt/trusted.gpg.d/kitware.gpg \
    && apt-add-repository 'deb https://apt.kitware.com/ubuntu/ focal main' \
    && apt-get update \
# if cmake needs to be updated, this shows the available versions:
    # && apt-cache madison cmake \
    && apt-get -y install --no-install-recommends cmake=4.2.3-0kitware1ubuntu20.04.1

