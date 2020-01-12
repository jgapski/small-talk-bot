#!/bin/bash

docker stop erlang_docker

docker system prune -af

./run_in_docker.sh
