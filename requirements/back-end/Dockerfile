FROM debian:bookworm-slim

# Install necessary packages
RUN apt-get update \
    && apt-get install -y python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install django psycopg2-binary

RUN mkdir transcendence

RUN files/ transcendence/

WORKDIR /transcendence

# python manage.py runserver
CMD ["python3", "manage.py", "runserver"]