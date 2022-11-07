import csv

x = int(input())
y = int(input())
with open("nearest_shore.csv", encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    title = next(reader)

    list_place = []
    for index, row in enumerate(reader):
        list_place.append((row[0], (x - int(row[1])) ** 2 + (y - int(row[2])) ** 2))
    list_place.sort(key=lambda x: x[1])
    for item in list_place:
        print(item[0])
