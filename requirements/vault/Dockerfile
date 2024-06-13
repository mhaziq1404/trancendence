FROM debian:buster

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    gnupg \
    lsb-release \
    && rm -rf /var/lib/apt/lists/*

# Download and install Vault
RUN wget https://releases.hashicorp.com/vault/1.10.0/vault_1.10.0_linux_amd64.zip -O /tmp/vault.zip \
    && unzip /tmp/vault.zip -d /usr/local/bin/ \
    && rm /tmp/vault.zip

# Create Vault user and directories
RUN useradd --system --home /etc/vault.d --shell /bin/false vault \
    && mkdir --parents /etc/vault.d \
    && mkdir --parents /opt/vault \
    && chown --recursive vault:vault /etc/vault.d /opt/vault

# Copy Vault configuration file
COPY ./vault-config.hcl /etc/vault.d/vault-config.hcl
RUN chown vault:vault /etc/vault.d/vault-config.hcl

# Expose Vault HTTP port
EXPOSE 8200

# Run Vault
USER vault
CMD ["vault", "server", "-config=/etc/vault.d/vault-config.hcl"]

