#!/bin/bash

cp -r /etc/mount/* /opt/
mkdir /etc/nginx/modules
cp /opt/nginx-1.22.1/objs/ngx_http_modsecurity_module.so /etc/nginx/modules/
rm -rf /usr/share/modsecurity-crs
git clone https://github.com/coreruleset/coreruleset /usr/local/modsecurity-crs
mv /usr/local/modsecurity-crs/crs-setup.conf.example /usr/local/modsecurity-crs/crs-setup.conf
mv /usr/local/modsecurity-crs/rules/REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf.example /usr/local/modsecurity-crs/rules/REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf


mkdir -p /etc/nginx/modsecurity
cp /opt/ModSecurity/unicode.mapping /etc/nginx/modsecurity
cp /opt/ModSecurity/modsecurity.conf-recommended /etc/nginx/modsecurity/modsecurity.conf

sed -i 's/SecRuleEngine DetectionOnly/SecRuleEngine On/' /etc/nginx/modsecurity/modsecurity.conf

echo "\n\n\n script finished"

# Start NGINX
/usr/sbin/nginx -g 'daemon off;'

while true
do
    echo "stuck"
    sleep 1
done
