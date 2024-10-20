import psycopg2

conn = psycopg2.connect(database="huntref",
                        host="localhost",
                        user="postgres",
                        password="tinykite04",
                        port="5432")

cursor = conn.cursor()

# add a red deer (0) at 175.28116357346426 -38.37439329113799 with abundance M

cursor.execute("SELECT id,ST_Distance(position,ST_MAKEPOINT(175.28116357346426,-38.37439329113799)::GEOGRAPHY) as distance FROM permit_areas order by distance limit 1")

aid = cursor.fetchone()[0]
print(aid)
#cursor.execute("SELECT permit_areas.area_name,area_animal_assoc.* FROM permit_areas JOIN area_animal_assoc ON area_id=permit_areas.id")
#cursor.execute("SELECT permit_areas.area_name,area_animal_assoc.* FROM permit_areas JOIN area_animal_assoc ON area_id=permit_areas.id WHERE permit_areas.id="+str(aid))
cursor.execute("SELECT * FROM area_animal_assoc WHERE area_id="+str(aid))

if cursor.rowcount == 0:
    print(cursor.rowcount,"inserting")
    cursor.execute("INSERT INTO area_animal_assoc (animal_id,area_id,abundance) VALUES (0,"+str(aid)+",'M');")
else:
    print("already exists",cursor.fetchall())


cursor.execute("SELECT permit_areas.area_name,area_animal_assoc.* FROM permit_areas JOIN area_animal_assoc ON area_id=permit_areas.id")
#cursor.execute("SELECT permit_areas.area_name,area_animal_assoc.* FROM permit_areas JOIN area_animal_assoc ON area_id=permit_areas.id WHERE permit_areas.id="+str(aid))
print(cursor.rowcount)
for row in cursor.fetchall():
    print(row)

conn.commit()