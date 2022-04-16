FROM debian:unstable-slim

WORKDIR /app

ARG DEBIAN_FRONTEND=noninteractive
ARG DEBCONF_NOWARNINGS="yes"

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    python3-rich

COPY ./src /app

ENTRYPOINT ["python3", "app.py"]
