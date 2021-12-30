from csv import DictReader

with open("fighters.csv") as f:
    csv_reader = DictReader(f)
    for row in csv_reader:
        print(row)