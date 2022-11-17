import sqlite3
import csv

filename = input()
date, title_side = input().split()
con = sqlite3.connect(filename)
cur = con.cursor()
result = cur.execute(f"""SELECT b.title, p.time, p.waves, p.wind 
FROM Bays as b, Sides as s, Predictions as p 
WHERE s.id = b.side_id AND s.id = p.side_id AND p.date = {int(date)} AND 
b.side_id = (SELECT ss.id 
FROM Sides as ss WHERE ss.title = '{title_side}') ORDER BY b.title, p.time""").fetchall()
with open("weather.csv", 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quotechar='"')
    for res in result:
        writer.writerow(res)
con.close()