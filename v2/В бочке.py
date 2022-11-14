import sqlite3

file_name = input()
second_condition = input()
union = input()
con = sqlite3.connect(file_name)
cur = con.cursor()
result = cur.execute(f"""SELECT name FROM ship_team 
WHERE status = 'sailor' {union} {second_condition} 
ORDER BY age""").fetchall()
for elem in result:
    print(elem[0])

con.close()