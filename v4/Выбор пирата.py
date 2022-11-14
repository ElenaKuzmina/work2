import csv

ships = input().split(' - ')
no_word = input().lower()
names = []
with open("suitable_crew.csv", encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    title = next(reader)
    for index, row in enumerate(reader):
        if row[2] not in ships:
            if no_word not in row[3].lower():
                if row[1] not in names:
                    names.append(row[1])

print('\n'.join(sorted(names)))