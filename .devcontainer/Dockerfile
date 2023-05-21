ARG VARIANT=2
FROM mcr.microsoft.com/devcontainers/universal:${VARIANT}

# Install mamba for faster install
ENV MAMBA_EXE="/opt/mambaforge/bin/mamba"
RUN cd /tmp \
    && curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh" \
    && sudo bash Mambaforge-$(uname)-$(uname -m).sh -b -p /opt/mambaforge

# Create the conda environment
COPY environment.yml /tmp/conda-tmp/
RUN umask 0002 && $MAMBA_EXE env create --file /tmp/conda-tmp/environment.yml && $MAMBA_EXE init
