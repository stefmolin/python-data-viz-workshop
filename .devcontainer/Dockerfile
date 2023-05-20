# Change variant to 3-bullseye for local arm64/Apple Silicon https://github.com/devcontainers/templates/blob/main/src/python/README.md
ARG VARIANT=3
FROM mcr.microsoft.com/devcontainers/python:${VARIANT}

# Install mamba for faster install
ENV MAMBA_EXE="/opt/mambaforge/bin/mamba"
RUN cd /tmp \
    && curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh" \
    && bash Mambaforge-$(uname)-$(uname -m).sh -b -p /opt/mambaforge

# Create the conda environment
COPY environment.yml /tmp/conda-tmp/
RUN umask 0002 && $MAMBA_EXE env create --file /tmp/conda-tmp/environment.yml
