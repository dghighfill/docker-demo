#!/bin/bash

docker run --rm -it \
--volume "/$PWD/flyway/conf:/flyway/conf" \
--volume "/$PWD/flyway/sql:/flyway/sql" \
--volume "/$PWD/db:/flyway/db" \
flyway/flyway -configFiles="conf/flyway.toml" $1 $2 $3 $4
