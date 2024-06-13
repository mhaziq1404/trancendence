FROM debian:buster

# Update package list and install basic dependencies
RUN apt-get update && apt-get install -y \
    nginx openssl git bison build-essential ca-certificates curl \
    dh-autoreconf doxygen flex gawk git iputils-ping wget \
    && rm -rf /var/lib/apt/lists/*

# Install development libraries and tools
RUN apt-get update && apt-get install -y \
    libcurl4-gnutls-dev libexpat1-dev libgeoip-dev liblmdb-dev \
    libpcre3-dev libpcre++-dev libssl-dev libtool libxml2 libxml2-dev \
    libyajl-dev locales lua5.3-dev pkg-config zlib1g-dev zlibc \
    libxslt-dev libgd-dev \
    && rm -rf /var/lib/apt/lists/*

# Create directory for SSL certificates
RUN mkdir -p /etc/nginx/ssl

# Generate self-signed SSL certificate
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/nginx/ssl/your-private-key.key \
    -out /etc/nginx/ssl/your-cert.crt \
    -subj "/C=MY/ST=Selangor/L=Sunway/O=42 Malaysia/OU=Student/CN=mmuhamad"

# Copy Nginx and default site configuration files
COPY ./conf/nginx.conf /etc/nginx/nginx.conf
COPY ./conf/default.conf /etc/nginx/conf.d/default.conf

# Create directory for web content
RUN mkdir -p /var/www/html

# Copy the script and make it executable
COPY tools/script.sh .
RUN chmod +x script.sh

# Expose port 443 for HTTPS
EXPOSE 443

# Start Nginx using the script
CMD ["./script.sh"]

