# Dockerfile for Django Backend with PostgreSQL

FROM debian:bookworm-slim

# Install necessary packages
RUN apt-get update \
    && apt-get install -y python3 python3-pip postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the Django project
COPY . .

# Expose port for Django development server
EXPOSE 8000

# Command to run the Django development server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]