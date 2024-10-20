import json

f = open("areas.geojson")

o = json.load(f)

index = 0
print("\\connect huntref")
print("INSERT INTO permit_areas (id, area_name, position) VALUES")
for feature in o["features"]:
    if feature["geometry"]["type"] == "Polygon":
        coords = feature["geometry"]["coordinates"][0][0]
        name = feature["properties"]["HuntBlockName"].strip()
        pass
    elif feature["geometry"]["type"] == "MultiPolygon":
        coords = feature["geometry"]["coordinates"][0][0][0]
        name = feature["properties"]["HuntBlockName"].strip()
        pass
    
    print("(",index,", '",name.replace("'","''"),"', ST_MAKEPOINT(",coords[0],",",coords[1],")::geography),",sep="")
    index = index+1

#(0,'Kaweka Forest Park',ST_MAKEPOINT(176.379014030882, -39.26223936542265)::geography),