FROM postgres:latest

WORKDIR /app

COPY signatures.csv signatures.csv
COPY init-user-db.sh /docker-entrypoint-initdb.d/init-user-db.sh
