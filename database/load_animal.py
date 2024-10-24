import json
import psycopg2
import sys

if len(sys.argv) < 4:
    print("Usage:",sys.argv[0],"common_name scientific_name data.geojson")
    exit()

com_name = sys.argv[1]
sci_name = sys.argv[2]
geojson = sys.argv[3]

conn = psycopg2.connect(database="huntref",
                        host="localhost",
                        user="postgres",
                        password="tinykite04",
                        port="5432")
cursor = conn.cursor()

cursor.execute("INSERT INTO game_animals (common_name,scientific_name) VALUES (%s,%s)",(com_name,sci_name))
cursor.execute("SELECT id FROM game_animals WHERE scientific_name=%s",(sci_name,))

animal_id = cursor.fetchone()[0]

f = open(geojson)

o = json.load(f)

for feature in o["features"]:
    if feature["geometry"]["type"] == "Polygon":
        coords = feature["geometry"]["coordinates"][0][0]
        abun = feature["properties"]["Abundance"].strip()
    elif feature["geometry"]["type"] == "MultiPolygon":
        coords = feature["geometry"]["coordinates"][0][0][0]
        abun = feature["properties"]["Abundance"].strip()
    if abun == "L" or abun == "M" or abun == "H":
        cursor.execute("SELECT id,ST_Distance(position,ST_MAKEPOINT(%s,%s)::GEOGRAPHY) as distance FROM permit_areas order by distance limit 1;",(coords[0],coords[1]))
        
        area_id = cursor.fetchone()[0]
        
        cursor.execute("SELECT * FROM area_animal_assoc WHERE area_id=%s AND animal_id=%s;",(area_id,animal_id))

        if cursor.rowcount == 0:
            print("inserting",coords)
            cursor.execute("INSERT INTO area_animal_assoc (animal_id,area_id,abundance) VALUES (%s,%s,%s);",(animal_id,area_id,abun))
        #else:
            #print("already exists",cursor.fetchall())
conn.commit()
