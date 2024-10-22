import psycopg2

conn = psycopg2.connect(database="huntref",
                        host="localhost",
                        user="postgres",
                        password="tinykite04",
                        port="5432")

cursor = conn.cursor()


cursor.execute("SELECT permit_areas.area_name,area_animal_assoc.*,game_animals.common_name FROM permit_areas JOIN area_animal_assoc ON area_id=permit_areas.id join game_animals on animal_id=game_animals.id where common_name='Red Deer'")
#cursor.execute("SELECT permit_areas.area_name,area_animal_assoc.* FROM permit_areas JOIN area_animal_assoc ON area_id=permit_areas.id WHERE permit_areas.id="+str(aid))
print(cursor.rowcount)
for row in cursor.fetchall():
    print(row)

conn.commit()