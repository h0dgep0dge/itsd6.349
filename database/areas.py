import json
import psycopg2

conn = psycopg2.connect(database="huntref",
                        host="localhost",
                        user="postgres",
                        password="tinykite04",
                        port="5432")
cursor = conn.cursor()

f = open("areas.geojson")

o = json.load(f)

for feature in o["features"]:
    if feature["geometry"]["type"] == "Polygon":
        coords = feature["geometry"]["coordinates"][0][0]
        name = feature["properties"]["HuntBlockName"].strip()
    elif feature["geometry"]["type"] == "MultiPolygon":
        coords = feature["geometry"]["coordinates"][0][0][0]
        name = feature["properties"]["HuntBlockName"].strip()
    
    #print("(",index,", '",name.replace("'","''"),"', ST_MAKEPOINT(",coords[0],",",coords[1],")::geography),",sep="")
    
    cursor.execute("INSERT INTO permit_areas (id,area_name,position) VALUES (default,%s,ST_MAKEPOINT(%s,%s)::GEOGRAPHY);",(name,coords[0],coords[1]))

conn.commit()