FROM mysql

ENV MYSQL_ROOT_PASSWORD=S3cret
ENV MYSQL_PASSWORD=user
ENV MYSQL_USER=user
ENV MYSQL_DATABASE=mydb

COPY ./3-Structure.sql /docker-entrypoint-initdb.d/
COPY ./4-Population.sql /docker-entrypoint-initdb.d/

EXPOSE 3306