import sqlite3

file_name = input()
positiv_condition = input()
negativ_condition = input()
con = sqlite3.connect(file_name)
cur = con.cursor()
result = cur.execute(f"""SELECT name FROM bays_of_island 
WHERE {positiv_condition} AND NOT {negativ_condition} 
ORDER BY depth DESC""").fetchall()
for elem in result:
    print(elem[0])

con.close()