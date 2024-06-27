FROM debian:bookworm-slim

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    gnupg2 \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install OpenJDK (required for Elasticsearch and Logstash)
RUN apt-get update && apt-get install -y openjdk-11-jre-headless

# Install Elasticsearch
RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add -
RUN echo "deb https://artifacts.elastic.co/packages/oss-7.x/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-7.x.list
RUN apt-get update && apt-get install -y elasticsearch-oss logstash-oss kibana-oss

# Expose ports for Elasticsearch, Logstash, and Kibana
EXPOSE 9200 9300 5044 5601

# Command to start the services
CMD service elasticsearch start && service logstash start && service kibana start && tail -f /dev/null
