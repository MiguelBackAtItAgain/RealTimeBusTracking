FROM mysql:8.0

ENV MYSQL_DATABASE=MBTAdb \
    MYSQL_ROOT_PASSWORD=YourCustomPassword

ADD Scripts/MBTA.sql /docker-entrypoint-initdb.d

EXPOSE 3306