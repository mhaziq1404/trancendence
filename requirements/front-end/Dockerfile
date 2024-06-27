FROM debian:bookworm-slim

# Update package lists and install necessary dependencies
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js and npm
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs

# Set up a working directory
WORKDIR /app

# Install Bootstrap and Three.js via npm
RUN npm install bootstrap@5 three

# Copy your HTML, JavaScript, and CSS files into the container
COPY index.html .
COPY script.js .
COPY style.css .

# Expose the port (if needed)
EXPOSE 3000

# Command to run your application
CMD ["npm", "start"]