FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    python3-dev \
    postgresql-dev \
    gdal-dev \
    geos-dev \
    proj-dev

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV GDAL_LIBRARY_PATH=/usr/lib/libgdal.so