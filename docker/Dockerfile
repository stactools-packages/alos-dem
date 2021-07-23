ARG STACTOOLS_VERSION=latest
FROM ghcr.io/stac-utils/stactools:$STACTOOLS_VERSION

WORKDIR /opt/stactools-alos-dem

# For caching purposes, install dependencies but remove the actual package
COPY pyproject.toml setup.cfg ./
COPY src/stactools/alos_dem/__init__.py src/stactools/alos_dem/
RUN pip install . \
    && rm -r /opt/conda/lib/python3.8/site-packages/stactools/alos_dem

COPY src ./src
RUN pip install .
