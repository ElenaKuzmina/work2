import csv

nominal = int(input())
summa = 0
with open("dead_mans_chest.csv", encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    title = next(reader)
    for index, row in enumerate(reader):
        if "coin" in row[1]:
            if int(row[3]) <= nominal:
                summa += int(row[3])
print(summa)