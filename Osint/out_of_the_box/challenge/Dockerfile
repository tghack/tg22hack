FROM php:7.4-apache
COPY . /var/www/html
RUN sed -i -e "s/80/8080/gm" -e "s/443/8443/gm" /etc/apache2/ports.conf
