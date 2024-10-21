import json
import psycopg2

conn = psycopg2.connect(database="huntref",
                        host="localhost",
                        user="postgres",
                        password="tinykite04",
                        port="5432")
cursor = conn.cursor()

f = open("deer.geojson")

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
        
        cursor.execute("SELECT * FROM area_animal_assoc WHERE area_id=%s;",(area_id,))

        if cursor.rowcount == 0:
            print(cursor.rowcount,"inserting")
            cursor.execute("INSERT INTO area_animal_assoc (animal_id,area_id,abundance) VALUES (0,%s,%s);",(area_id,abun))
        else:
            print("already exists",cursor.fetchall())
conn.commit()