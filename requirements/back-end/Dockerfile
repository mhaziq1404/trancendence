FROM debian:bookworm-slim

# Install necessary packages
RUN apt-get update \
    && apt-get install -y python3 python3-pip python3.11-venv \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /transcendence

COPY files/* /transcendence/

WORKDIR /transcendence

RUN python3 -m venv myappvenv \
    && myappvenv/bin/pip install django psycopg2-binary

CMD ["myappvenv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
