import csv

FEATURES = {
    'coffee': lambda array, index: array[index]['Coffee (mg caffeine)'],
    'coffee-1': lambda array, index: array[index-1]['Coffee (mg caffeine)'],
    'coffee-2': lambda array, index: array[index-2]['Coffee (mg caffeine)'],
    'coffee-1:5': lambda array, index: np.average([array[index-i]['Coffee (mg caffeine)'] for i in range(1, 6)]),
    'water': lambda array, index: array[index]['Water (cups)'],
    'water-1': lambda array, index: array[index-1]['Water (cups)'],
    'water-2': lambda array, index: array[index-2]['Water (cups)'],
    'water-1:5': lambda array, index: np.average([array[index-i]['Water (cups)'] for i in range(1, 6)]),
    'sleep-1': lambda array, index: array[index-1]['Sleep'],
    'sleep-2': lambda array, index: array[index-2]['Sleep'],
    'sleep-3': lambda array, index: array[index-3]['Sleep'],
    'sleep-1:5': lambda array, index: np.average([array[index-i]['Sleep'] for i in range(1, 6)])
}

with open('data/stats.csv') as datafile:
    reader = csv.DictReader(datafile, delimiter=',')
    dataarray = []
    for row in reader:
        dataarray.append(row)
    print FEATURES['coffee'](dataarray, 18);

