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

METRICS = {
    'productivity': lambda array, index: array[index]['productivity']
}

def load_csv_to_array(filename):
    dataarray = []
    with open(filename) as datafile:
        reader = csv.DictReader(datafile, delimiter=',')
        for row in reader:
            dataarray.append(row)
    return dataarray

dataarray = load_csv_to_array('data/stats.csv')
