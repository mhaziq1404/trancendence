# Use Debian Bookworm Slim as the base image
FROM debian:bookworm-slim

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Download and install Vault
ENV VAULT_VERSION=1.7.5
RUN wget https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip && \
    unzip vault_${VAULT_VERSION}_linux_amd64.zip && \
    mv vault /usr/local/bin/ && \
    rm vault_${VAULT_VERSION}_linux_amd64.zip

# Expose the Vault port
EXPOSE 8200

# Run Vault in server mode
CMD ["vault", "server", "-dev"]