import sqlite3

file_name = input()
first_condition = input()
second_condition = input()
firth_condition = input()
con = sqlite3.connect(file_name)
cur = con.cursor()
result = cur.execute(f"""SELECT team_id, leader FROM towage 
WHERE ({first_condition} AND {second_condition}) OR {firth_condition}
 ORDER BY leader""").fetchall()
for elem in result:
    print(f"{elem[0]} ({elem[1]})")
con.close()
