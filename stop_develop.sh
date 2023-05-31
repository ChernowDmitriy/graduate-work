#!/bin/bash

cd infrastructures/config/dev || exit

docker-compose -f docker-compose.yml down
