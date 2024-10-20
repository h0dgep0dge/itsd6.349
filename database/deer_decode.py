import json
import psycopg2

conn = psycopg2.connect(database="huntref",
                        host="localhost",
                        user="postgres",
                        password="tinykite04",
                        port="5432")

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
        print(abun)
