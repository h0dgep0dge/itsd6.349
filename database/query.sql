\c huntref

\echo 'find  nearest 10 places to taupo to find deer, ordered with most abundant at the top'

SELECT * FROM (SELECT *,ST_DISTANCE(ST_MAKEPOINT(176.09100199566095,-38.69226626199746)::GEOGRAPHY,permit_areas.position) as distance
FROM permit_areas
JOIN area_animal_assoc ON area_id=permit_areas.id
JOIN game_animals on animal_id=game_animals.id
WHERE common_name = 'Red deer'
ORDER BY distance
LIMIT 10) ORDER BY abundance DESC;

\echo 'find all places to find deer within 100km of tauranga with most abundant at the top'

SELECT *,ST_DISTANCE(ST_MAKEPOINT(176.16996407646488,-37.70127991105802)::GEOGRAPHY,permit_areas.position) as distance
FROM permit_areas
JOIN area_animal_assoc ON area_id=permit_areas.id
JOIN game_animals on animal_id=game_animals.id
WHERE common_name = 'Wild boar' AND ST_DISTANCE(ST_MAKEPOINT(176.16996407646488,-37.70127991105802)::GEOGRAPHY,permit_areas.position) <= 100000
ORDER BY abundance DESC;

\echo 'find nearby places to hunt, within 100km of your location (tauranga in this case)'

SELECT *,ST_DISTANCE(ST_MAKEPOINT(176.16996407646488,-37.70127991105802)::GEOGRAPHY,permit_areas.position) as distance
FROM permit_areas
WHERE ST_DISTANCE(ST_MAKEPOINT(176.16996407646488,-37.70127991105802)::GEOGRAPHY,permit_areas.position) <= 100000
ORDER BY distance ASC;

\echo 'when you''ve selected a location, find what game is available there, and how abundant it is'

SELECT * 
FROM permit_areas
JOIN area_animal_assoc on permit_areas.id = area_animal_assoc.area_id
JOIN game_animals ON game_animals.id = area_animal_assoc.animal_id
WHERE permit_areas.id = 219
ORDER BY area_animal_assoc.abundance DESC;

\echo 'create a notice to warn other users of the app of a slip on the gravel road in the Hangatiki Scenic Reserve (id=219)'

DO $$ 
DECLARE
    retnoticeid notices.id%TYPE;
BEGIN
    INSERT INTO notices (body) 
    VALUES ('Bad slip across the road, 4wd necessary')
    RETURNING notices.id INTO retnoticeid;

    INSERT INTO notice_assoc (notice_id,area_id)
    VALUES (retnoticeid,219);
END $$;

\echo 'create notices to warn other users of an outbreak of a virus affecting deer, for every area with deer within 150km of the outbreak'

DO $$
DECLARE
    retnoticeid notices.id%TYPE;
BEGIN
    INSERT INTO notices (body)
    VALUES ('Cases of bovine turberculosis found in whanganui national park, take precautions')
    RETURNING notices.id INTO retnoticeid;

    INSERT INTO notice_assoc (notice_id,area_id)
    SELECT retnoticeid,permit_areas.id
    FROM permit_areas
    JOIN area_animal_assoc ON permit_areas.id = area_animal_assoc.area_id
    JOIN game_animals ON area_animal_assoc.animal_id = game_animals.id
    WHERE
        ST_DISTANCE(ST_MAKEPOINT(174.84644842667964,-39.246175557430504)::GEOGRAPHY,permit_areas.position) <= 150000
        AND game_animals.scientific_name = 'Cervus elaphus scoticus';
END $$;

\echo 'find all the notices that apply to Hangatiki Scenic Reserve (id=219)'

SELECT permit_areas.area_name,ST_Y(permit_areas.position::geometry) as latitude,ST_X(permit_areas.position::geometry) as longitude,notices.body
FROM permit_areas
JOIN notice_assoc ON permit_areas.id = notice_assoc.area_id
JOIN notices ON notice_assoc.notice_id = notices.id
WHERE permit_areas.id = 219;
