#!/bin/bash
docker build -t cookie-web .

docker run -d -p 31001:5000 --name cookie-web-con cookie-web:latest