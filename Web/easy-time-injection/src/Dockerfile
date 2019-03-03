FROM mattrayner/lamp:latest-1604-php7

MAINTAINER Lhaihai 

ADD sql.sql /tmp/
Run cd /tmp/ && \
    chown www-data:www-data -R /app && \
    mysql -uroot < sql.sql && \
    rm -rf /tmp/sql.sql

EXPOSE 80 3306
