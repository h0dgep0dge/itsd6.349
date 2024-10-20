\connect huntref

INSERT INTO area_animal_assoc (animal_id,area_id,abundance) VALUES
(0,400,'M'),
(2,400,'L'),
(0,405,'M'),
/*(0,224,'H'),*/
(1,406,'M');

SELECT *,ST_Distance(position,ST_GeographyFromText('Point(175.87066174802968 -37.735100735866936)')) as distance
 from permit_areas order by distance LIMIT 10;
