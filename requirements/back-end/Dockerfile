FROM debian:bookworm-slim

# Install necessary packages
RUN apt-get update \
    && apt-get install -y python3 python3-pip postgresql-client \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install django psycopg2-binary

WORKDIR /trancendence

RUN django-admin startproject trancendence