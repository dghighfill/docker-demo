#!/bin/bash

docker build -t api .

docker run --rm -it \
--volume "/$PWD/api/src:/app" \
--volume "/$PWD/db:/flyway/db" \
--env SQLALCHEMY_DATABASE_URL="sqlite:////flyway/db/coffee.db" \
--name api_server \
-p 8000:8000 \
api
