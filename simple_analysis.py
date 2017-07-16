import csv
import numpy as np
from sklearn.ensemble import RandomForestClassifier

FEATURES = {
    'coffee': lambda array, index: array[index]['Coffee (mg caffeine)'],
    'coffee-1': lambda array, index: array[index-1]['Coffee (mg caffeine)'],
    'coffee-2': lambda array, index: array[index-2]['Coffee (mg caffeine)'],
    #'coffee-1:5': lambda array, index: np.average([float(array[index-i]['Coffee (mg caffeine)']) if len(array[index-i]['Coffee (mg caffeine)']) > 0 else np.nan for i in range(1, 6)]),
    'water': lambda array, index: array[index]['Water (cups)'],
    'water-1': lambda array, index: array[index-1]['Water (cups)'],
    'water-2': lambda array, index: array[index-2]['Water (cups)'],
    #'water-1:5': lambda array, index: np.average([float(array[index-i]['Water (cups)']) if len(array[index-i]['Water (cups)']) > 0 else np.nan for i in range(1, 6)]),
    'sleep-1': lambda array, index: array[index-1]['Sleep'],
    'sleep-2': lambda array, index: array[index-2]['Sleep'],
    'sleep-3': lambda array, index: array[index-3]['Sleep'],
    #'sleep-1:5': lambda array, index: np.average([float(array[index-i]['Sleep']) for i in range(1, 6) if len(array[index-i]['Sleep']) > 0])
}

METRICS = {
    'productivity': lambda array, index: array[index]['Productivity']
}

feature_keys = list(FEATURES.keys())

def load_csv_to_array(filename):
    dataarray = []
    with open(filename) as datafile:
        reader = csv.DictReader(datafile, delimiter=',')
        for row in reader:
            dataarray.append(row)
    return dataarray

featured_data = {}
dataarray = load_csv_to_array('data/stats.csv')
for i in range(16, len(dataarray)):
    continue_outer_loop = False
    feature_values = {}
    metric_values = {}
    for feature in FEATURES.keys():
        try:
            feature_value = np.float(FEATURES[feature](dataarray, i))
            feature_values[feature] = feature_value
        except ValueError:
            continue_outer_loop = True
            break

    if continue_outer_loop:
        continue

    for metric in METRICS.keys():
        try:
            metric_value = float(METRICS[metric](dataarray, i))
            metric_values[metric] = metric_value
        except ValueError:
            continue_outer_loop = True
            break

    if continue_outer_loop:
        continue
    
    featured_data[dataarray[i]['Date']] = {}
    featured_data[dataarray[i]['Date']]['features'] = feature_values
    featured_data[dataarray[i]['Date']]['metrics'] = int(2*metric_values['productivity'] + 0.5)

clf = RandomForestClassifier(
        n_estimators = len(feature_keys),
        max_features = 2,
        max_depth = 4)

y_array = []
x_array = []
for date in featured_data.keys():
    y_array.append(featured_data[date]['metrics'])
    x_array.append([featured_data[date]['features'][key] for key in feature_keys])

print clf.fit(x_array, y_array)
