#!/bin/bash

PGPASSWORD=tinykite04 psql -h localhost -U postgres < schema.sql
PGPASSWORD=tinykite04 psql -h localhost -U postgres < animals.sql
python3 areas.py
python3 deer.py
python3 boar.py
python3 chamois.py
python3 rabbit.py