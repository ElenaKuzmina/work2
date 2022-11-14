import sqlite3

file_name = input()
first_condition = input()
second_condition = input()
con = sqlite3.connect(file_name)
cur = con.cursor()
result = cur.execute(f"""SELECT latitude, longitude FROM Island 
WHERE NOT {first_condition} AND NOT {second_condition} 
ORDER BY latitude, longitude""").fetchall()
for elem in result:
    print((elem[0], elem[1]))
con.close()