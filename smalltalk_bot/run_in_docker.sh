#!/bin/bash

docker build -t erlang_docker .

docker run -d -p 8080:8080 --name erlang_docker erlang_docker
