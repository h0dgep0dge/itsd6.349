#!/bin/bash

PGPASSWORD=tinykite04 psql -h localhost -U postgres < schema.sql
#PGPASSWORD=tinykite04 psql -h localhost -U postgres < animals.sql
python3 areas.py

python3 load_animal.py 'Red deer' 'Cervus elaphus scoticus' deer.geojson
python3 load_animal.py 'Wild boar' 'Sus scrofa' boar.geojson
python3 load_animal.py 'Chamois' 'Rupicapra rupicapra' chamois.geojson
python3 load_animal.py 'Rabbit' 'Oryctolagus cuniculus' rabbit.geojson