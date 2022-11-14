import sqlite3

file_name = input()
param = input()
first_condition = input()
union = input()
second_condition = input()
con = sqlite3.connect(file_name)
cur = con.cursor()
result = cur.execute(f"""SELECT {param} FROM Stories 
WHERE {first_condition} {union} {second_condition} ORDER BY {param}""").fetchall()
for elem in result:
    print(elem[0])

con.close()
