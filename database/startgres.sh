#!/bin/bash

sudo docker run --rm -d -e POSTGRES_PASSWORD=tinykite04 -p 5432:5432 postgis/postgis
