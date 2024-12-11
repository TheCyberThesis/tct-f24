#!/bin/bash

docker build -t sqli-web .

# docker run -d -p 31002:5000 --name sqli-web-con sqli-web:latest