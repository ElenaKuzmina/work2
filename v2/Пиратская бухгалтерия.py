import csv

count_cross = int(input())
summa = 0
with open("pirate_accounting.csv", encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    title = next(reader)
    for index, row in enumerate(reader):
        if row[2].count('x') == len(row[2]) and row[2].count('x') >= count_cross:
            if int(row[1]) > 1765:
                summa += int(row[3])
print(summa)