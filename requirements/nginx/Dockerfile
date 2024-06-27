FROM debian:bookworm-slim

# Update package list and install dependencies
RUN apt-get update && apt-get install -y nginx openssl \
    bison build-essential ca-certificates curl dh-autoreconf doxygen \
    flex gawk git iputils-ping libcurl4-gnutls-dev libexpat1-dev libgeoip-dev liblmdb-dev \
    libpcre3-dev libssl-dev libtool libxml2 libxml2-dev libyajl-dev locales \
    lua5.3-dev pkg-config wget zlib1g-dev libxslt-dev libgd-dev libperl-dev && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /etc/nginx/ssl

RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/nginx/ssl/your-private-key.key \
    -out /etc/nginx/ssl/your-cert.crt \
    -subj "/C=MY/ST=Selangor/L=Sunway/O=42 Malaysia/OU=Student/CN=mmuhamad"

COPY ./conf/nginx.conf /etc/nginx/nginx.conf
COPY ./conf/default.conf /etc/nginx/conf.d/default.conf
COPY ./conf/main.conf /etc/nginx/modsec/main.conf
COPY ./conf/modsecurity.conf /etc/nginx/modsecurity/modsecurity.conf

COPY /tools/script.sh /tools/script.sh
RUN chmod +x /tools/script.sh

RUN mkdir -p /var/www/transcendence

EXPOSE 443

CMD ["bash", "/tools/script.sh"]
