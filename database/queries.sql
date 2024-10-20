\connect huntref

SELECT area_name,ST_Distance(position,ST_GeographyFromText('Point(176.85921818484542 -38.69150959596966)')) as distance
 from permit_areas order by distance LIMIT 10;