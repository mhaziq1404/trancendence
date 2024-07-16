FROM debian:bookworm-slim

RUN apt-get update \
    && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://deb.nodesource.com/setup_21.x | bash - \
    && apt-get install -y nodejs

RUN mkdir web/

EXPOSE 8080

WORKDIR ./web

RUN npm init -y
RUN npm install express jsonwebtoken body-parser

COPY files/* .

EXPOSE 3000

CMD ["node", "index.js"]