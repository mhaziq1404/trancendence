FROM debian:buster

# Update package list and install dependencies
RUN apt-get update && apt-get install -y nginx openssl \
    libnginx-mod-security modsecurity-crs && rm -rf /var/lib/apt/lists/*

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
RUN mkdir -p /var/www/wordpress

# Ensure ModSecurity is enabled and configure it
RUN sed -i 's/SecRuleEngine DetectionOnly/SecRuleEngine On/' /etc/modsecurity/modsecurity.conf

# Include OWASP CRS rules in the Nginx configuration
RUN echo 'Include "/usr/share/modsecurity-crs/owasp-crs.load"' >> /etc/nginx/modsec/main.conf

# Expose port 443 for HTTPS
EXPOSE 443

# Start Nginx in the foreground
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
