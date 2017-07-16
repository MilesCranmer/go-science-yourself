import csv

with open('data/stats.csv') as datafile:
    reader = csv.DictReader(datafile)
    for row in reader:
        print row.keys()
