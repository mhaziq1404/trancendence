FROM debian:bookworm-slim

# Install necessary packages
RUN apt-get update \
    && apt-get install -y python3 python3-pip python3.11-venv \
    && rm -rf /var/lib/apt/lists/*

# Create and set up the application directory
RUN mkdir /transcendence
COPY files/* /transcendence/
WORKDIR /transcendence

# Create virtual environment
RUN python3 -m venv myappvenv

# Install dependencies
RUN /bin/bash -c "source myappvenv/bin/activate && pip3 install django psycopg2-binary"

# Expose the Django development server port
EXPOSE 8000

# Command to run the server
CMD ["myappvenv/bin/python3", "manage.py", "runserver", "0.0.0.0:8000"]
