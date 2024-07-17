FROM debian:bookworm-slim

# Install dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-venv python3-pip curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port
EXPOSE 5000

# Run the application
CMD [ "python3", "server.py" ]

