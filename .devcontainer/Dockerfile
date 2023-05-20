# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.245.0/containers/python-3-miniconda/.devcontainer/base.Dockerfile

FROM mcr.microsoft.com/vscode/devcontainers/miniconda:0-3

# [Choice] Node.js version: none, lts/*, 16, 14, 12, 10
ARG NODE_VERSION="none"
RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

# Install mamba for faster install
ENV MAMBA_EXE="/opt/mambaforge/bin/mamba"
RUN cd /tmp \
    && curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh" \
    && sudo bash Mambaforge-$(uname)-$(uname -m).sh -b -p /opt/mambaforge

# Create the conda environment
COPY environment.yml* /tmp/conda-tmp/
RUN umask 0002 && /opt/mambaforge/bin/mamba env create --file /tmp/conda-tmp/environment.yml

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
