FROM debian:bookworm-slim

# Install PostgreSQL and other necessary packages
RUN apt-get update && \
    apt-get install -y postgresql postgresql-contrib && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Adjust PostgreSQL configuration to listen on all addresses
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/*/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/*/main/postgresql.conf

# Set environment variables
ENV POSTGRES_USER ponguser
ENV POSTGRES_PASSWORD pongpassword
ENV POSTGRES_DB pongdb

# Expose PostgreSQL port
EXPOSE 5432

# Start PostgreSQL service
CMD ["postgres", "-c", "config_file=/etc/postgresql/*/main/postgresql.conf"]