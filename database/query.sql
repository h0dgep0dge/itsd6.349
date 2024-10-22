\c huntref

/* nearest 10 places to taupo to find deer, ordered with most abundant at the top */
/*SELECT * FROM (SELECT *,ST_DISTANCE(ST_MAKEPOINT(176.09100199566095,-38.69226626199746)::GEOGRAPHY,permit_areas.position) as distance
FROM permit_areas
JOIN area_animal_assoc ON area_id=permit_areas.id
JOIN game_animals on animal_id=game_animals.id
WHERE common_name = 'Red deer'
ORDER BY distance
LIMIT 10) ORDER BY abundance DESC;*/

/* all places to find deer within 100km of tauranga with most abundant at the top */
/*SELECT *,ST_DISTANCE(ST_MAKEPOINT(176.16996407646488,-37.70127991105802)::GEOGRAPHY,permit_areas.position) as distance
FROM permit_areas
JOIN area_animal_assoc ON area_id=permit_areas.id
JOIN game_animals on animal_id=game_animals.id
WHERE common_name = 'Wild boar' AND ST_DISTANCE(ST_MAKEPOINT(176.16996407646488,-37.70127991105802)::GEOGRAPHY,permit_areas.position) <= 100000
ORDER BY abundance DESC;*/

