import sqlite3
import csv

filename = input()
date_start, date_finish = input().split()
con = sqlite3.connect(filename)
cur = con.cursor()
result = cur.execute(f"""SELECT s.ship, c.captain, n.navigator, year, benefit 
FROM ships as s, captains as c, navigators as n  
WHERE (s.id_cap = (SELECT id_cap FROM captains WHERE captain = 'Billy Bons') 
OR s.id_navigator = (SELECT id_navigator FROM navigators WHERE navigator = 'Billy Bons')) 
AND year BETWEEN 1760 AND 1766 
ORDER BY s.id""").fetchall()
with open("pirates.csv", 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quotechar='"')
    for res in result:
        writer.writerow(res)
con.close()