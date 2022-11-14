import csv

date_start, date_finish = input().split()
who = []
words = ["treasure", "island", "trove", "map"]
with open("mouth_shut.csv", encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    title = next(reader)
    for index, row in enumerate(reader):
        if int(date_start) <= int(row[3]) <= int(date_finish):
            if any(word in row[2] for word in words):
                if row[1] not in who:
                    who.append(row[1])

print('; '.join(sorted(who)))
