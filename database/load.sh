#!/bin/bash

PGPASSWORD=tinykite04 psql -h localhost -U postgres < huntref.sql
PGPASSWORD=tinykite04 psql -h localhost -U postgres < areas.sql
PGPASSWORD=tinykite04 psql -h localhost -U postgres < queries.sql
