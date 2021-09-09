#!/bin/sh

docker build --tag nasdaq.institution.selenium:py3.8 -f DockerTools/Dockerfile .

#docker images | grep none | awk '{print $3}' | xargs docker rmi --force
