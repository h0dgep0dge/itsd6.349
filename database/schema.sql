DROP DATABASE IF EXISTS huntref;
CREATE DATABASE huntref;

\connect huntref

CREATE EXTENSION postgis;

CREATE TABLE game_animals (
    id serial primary key,
    common_name varchar(255),
    scientific_name varchar(255) unique
);

CREATE TABLE permit_areas (
    id serial primary key,
    area_name varchar(255),
    position GEOGRAPHY
);

CREATE TYPE abundance_type AS ENUM ('L','M','H');

CREATE TABLE area_animal_assoc (
    id serial primary key,
    animal_id int not null,
    area_id int not null,
    /*season_start date,
    season_end date,*/
    abundance abundance_type
);

CREATE TABLE notices (
    id serial primary key,
    expiry date,
    body varchar(512)
);

CREATE TABLE notice_assoc (
    id serial primary key,
    notice_id int,
    area_id int,
    animal_id int
);
