import csv
FILENAME = "myCSV.csv"
users = [
    ["Tom", 28],
    ["Alice", 23],
    ["Bob", 34] ]
with open(FILENAME, "w") as file:
    writer = csv.writer(file)
    writer.writerows(users)


FILENAME = "myCSV.csv"
user = ['Ivan', 19]
with open(FILENAME, "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(user)


FILENAME = "myCSV.csv"
with open(FILENAME, "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], " - ", row[1])




FILENAME = "myCSV.csv"

users = [
    {"name": "Tom", "age": 28},
    {"name": "Alice", "age": 23},
    {"name": "Bob", "age": 34}
]

with open(FILENAME, "w", newline="") as file:
    columns = ["name", "age"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()

    # запись нескольких строк
    writer.writerows(users)

    user = {"name" : "Ivan", "age": 19}
    # запись одной строки
    writer.writerow(user)

with open(FILENAME, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], "-", row["age"])
