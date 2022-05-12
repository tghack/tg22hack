FROM php:7.4-apache

COPY ./src /var/www/html
COPY flag /flag

RUN sed -i -e "s/80/8080/gm" -e "s/443/8443/gm" /etc/apache2/ports.conf

WORKDIR /var/www/html
