DROP DATABASE IF EXISTS huntref;
CREATE DATABASE huntref;

\connect huntref

CREATE EXTENSION postgis;

CREATE TABLE game_animals (
    id int primary key,
    common_name varchar(255),
    scientific_name varchar(255)
);

CREATE TABLE permit_areas (
    id int primary key,
    area_name varchar(255),
    position GEOGRAPHY
);

CREATE TYPE abundance_type AS ENUM ('L','M','H');

CREATE TABLE area_animal_assoc (
    id int primary key,
    animal_id int not null,
    area_id int not null,
    season_start date,
    season_end date,
    abundance abundance_type
);

CREATE TABLE notices (
    id int primary key,
    expiry date,
    body varchar(512)
);

CREATE TABLE notice_assoc (
    id int primary key,
    notice_id int,
    area_id int,
    animal_id int
);

/*INSERT INTO permit_areas (id, area_name, position) VALUES
(0,'Kaweka Forest Park',ST_GeogFromText('POINT(-39.26223936542265 176.379014030882)')),
(1,'Ruahine Forest Park',ST_GeogFromText('POINT(-39.82125811686515 176.1380415488733)')),
(2,'Tararua Forest Park',ST_GeogFromText('POINT(-40.84626904872246 175.37291703742596)'));*/


/*SELECT area_name,ST_Distance(position,ST_GeographyFromText('Point(176.85921818484542 -38.69150959596966)')) as distance
 from permit_areas order by distance
*/