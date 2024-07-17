FROM debian:bookworm-slim

# Install PostgreSQL and other necessary packages
RUN apt-get update && \
    apt-get install -y postgresql postgresql-contrib && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV POSTGRES_USER ponguser
ENV POSTGRES_PASSWORD pongpassword
ENV POSTGRES_DB pongdb

# Expose PostgreSQL port
EXPOSE 5432

# Add PostgreSQL's binaries to the PATH
ENV PATH="/usr/lib/postgresql/15/bin:${PATH}"

# Run the PostgreSQL server
ENTRYPOINT ["postgres"]
CMD ["-c", "config_file=/etc/postgresql/postgresql.conf"]
