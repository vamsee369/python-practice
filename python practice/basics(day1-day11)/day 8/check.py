import csv
with open("csv.reader", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
