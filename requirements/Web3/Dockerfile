FROM debian:bookworm-slim

# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    software-properties-common \
    lsb-release \
    gnupg

# Add Ethereum repository and install Ethereum
RUN curl -fsSL https://gethstore.blob.core.windows.net/builds/ethereum-go-linux-arm64-1.10.16-ffea7d24.tar.gz | tar -xzv \
    && mv ethereum-go-linux-arm64-1.10.16-ffea7d24/geth /usr/local/bin/ \
    && rm -rf ethereum-go-linux-arm64-1.10.16-ffea7d24

# Expose necessary ports for Ethereum
EXPOSE 8545 8546 30303

# Run the Ethereum node
CMD ["geth", "--http", "--http.addr", "0.0.0.0", "--http.port", "8545", "--http.api", "eth,net,web3,personal"]
