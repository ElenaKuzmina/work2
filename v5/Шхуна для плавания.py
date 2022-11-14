import csv

volume_ships, count_salers, count_passengers = [int(v) for v in input().split(' ')]
names = []
with open("schooner_for_sailing.csv", encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    title = next(reader)
    for index, row in enumerate(reader):
        if int(row[2]) >= volume_ships:
            if int(row[5]) <= count_salers:
                if (int(row[4]) >= count_passengers // 2 and count_passengers % 2 == 0) \
                        or (int(row[4]) >= count_passengers // 2 + 1 and count_passengers % 2 == 1):
                    if row[1] not in names:
                        names.append(f"{row[1]} ({row[3]})")
print('\n'.join(sorted(names)))