#!/bin/bash

docker build -t api .

docker run --rm -it \
--volume "/$PWD/api/src:/app" \
--volume "/$PWD/db:/data" \
--env SQLALCHEMY_DATABASE_URL="sqlite:////data/coffee.db" \
--name api_server \
-p 8000:8000 \
api