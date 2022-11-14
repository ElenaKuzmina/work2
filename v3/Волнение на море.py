import sqlite3
import csv

filename = input()
date, title_side = input().split()
con = sqlite3.connect(filename)
cur = con.cursor()
result = cur.execute(f"""SELECT b.title, p.date, p.time, p.wind FROM Bays as b, Sides as s, Predictions as p WHERE s.id = b.side_id AND s.id = p.side_id AND s.id in (SELECT pp.side_id Predictions as pp WHERE date = {int(date)}) AND s.id in (SELECT bb.side_id FROM Bays as bb WHERE b.title = {title_side}) ORDER BY p.time, b.title""").fetchall()
with open("weather.csv", 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quotechar='"')
    for res in result:
        writer.writerow(res)
con.close()