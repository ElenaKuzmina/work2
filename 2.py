import sqlite3

param = input()
no_better = []
con = sqlite3.connect("squirrels_records.db")
cur = con.cursor()
result = cur.execute(f"""SELECT animal_type, {param} 
FROM Records WHERE {param} <= (SELECT {param} 
FROM Records WHERE animal_type = 'human') 
AND animal_type <> 'human' 
ORDER BY {param} DESC, animal_type""").fetchall()
for elem in result:
    no_better.append([elem[0], elem[1]])

con.close()