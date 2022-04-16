FROM debian:unstable-slim

WORKDIR /app

ARG DEBIAN_FRONTEND=noninteractive
ARG DEBCONF_NOWARNINGS="yes"

EXPOSE 8521

RUN apt-get update && \
  apt-get install --no-install-recommends -y \
  python3-pip

RUN pip install mesa matplotlib jupyter numpy

COPY ./src /app

ENTRYPOINT ["mesa", "runserver"]
