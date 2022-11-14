import sqlite3
import csv

filename = input()
title, loophole_number = input().split()
con = sqlite3.connect(filename)
cur = con.cursor()
result = cur.execute(f"""SELECT t.name, t.weapon, s.time_on_duty 
FROM Schedule as s, Team as t, Places_to_protect as p  
WHERE s.team_id = t.id AND s.place_id = p.id AND 
s.place_id = (SELECT id FROM Places_to_protect WHERE title = "{title}") 
AND s.loophole_number = {int(loophole_number)} 
ORDER BY s.time_on_duty""").fetchall()
with open("on_duty.csv", 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quotechar='"')
    for res in result:
        writer.writerow(res)
con.close()