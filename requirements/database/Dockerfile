FROM debian:bookworm-slim

# Install PostgreSQL
RUN apt-get update && apt-get install -y postgresql postgresql-contrib

# Create a directory for initialization scripts
RUN mkdir -p /docker-entrypoint-initdb.d

# Copy your initialization script (if needed)
# COPY init.sql /docker-entrypoint-initdb.d/

# Expose the PostgreSQL port
EXPOSE 5432

# Start PostgreSQL service
CMD ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"]