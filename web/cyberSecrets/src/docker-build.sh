#!/bin/bash
docker build -t cybersecrets-web .

docker run -d -p 31000:80 --name cybersecrets-web-con cybersecrets-web:latest