import csv

FEATURES = {
    'coffee': lambda array, index: array[index]['Coffee (mg caffeine)'],
    'coffee-1': lambda array, index: array[index-1]['Coffee (mg caffeine)']
}

with open('data/stats.csv') as datafile:
    reader = csv.DictReader(datafile, delimiter=',')
    dataarray = []
    for row in reader:
        dataarray.append(row)
    print FEATURES['coffee'](dataarray, 18);

