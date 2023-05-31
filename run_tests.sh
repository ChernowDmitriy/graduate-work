#!/bin/bash

cd infrastructures/config/test || exit

docker-compose -f docker-compose.yml down

docker-compose -f docker-compose.yml up -d --build
