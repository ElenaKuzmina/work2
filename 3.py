import sqlite3
import csv


def debt(ship, *data):
    con = sqlite3.connect("liability.db")
    cur = con.cursor()
    result = cur.execute(f"""SELECT central_hold + remaining_holds 
    FROM Types WHERE id = (SELECT type_id FROM Ships 
    WHERE name= '{ship}')""").fetchall()
    goods = cur.execute("""SELECT * FROM Goods ORDER BY volume DESC, good""").fetchall()
    with open("loading_order.csv", 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quotechar='"')
        writer.writerow(["good", "amount", "total_volume"])
        volume_total = result[0][0]
        print(volume_total)
        print(goods)
        for g in goods:
            for d in data:
                if g[0] == d[0]:
                    if g[2] * d[1] < volume_total:
                        writer.writerow([g[1], d[1], g[2] * d[1]])
                        volume_total -= g[2] * d[1]
                    elif volume_total > 0:
                        k = volume_total // g[2]
                        writer.writerow([g[1], k, g[2] * k])
                        volume_total -= g[2] * k

                    print(volume_total)

    con.close()


data = [(1, 100), (2, 20), (5, 50), (7, 50)]
debt("Arabella", *data)