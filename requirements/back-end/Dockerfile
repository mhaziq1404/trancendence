FROM debian:bookworm-slim

# Install necessary packages
RUN apt-get update \
    && apt-get install -y python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir transcendence

RUN files/ transcendence/

WORKDIR /transcendence

RUN python3 -m venv myappvenv

RUN source myappvenv/bin/activate

RUN pip3 install django psycopg2-binary

# python manage.py runserver
CMD ["python3", "manage.py", "runserver"]