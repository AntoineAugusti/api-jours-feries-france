import csv
import os
import json
from collections import defaultdict

modes = [
    ('data/', 'jours_feries_seuls.csv'),
    ('data/alsace-moselle/', 'jours_feries_seuls_alsace_moselle.csv'),
]

for mode in modes:
    base_path, filename = mode
    os.makedirs(base_path, exist_ok=True)

    reader = csv.DictReader(open(filename))

    data_by_year = defaultdict(list)
    for row in reader:
        year = row['date'][0:4]
        del row['est_jour_ferie']
        data_by_year[year].append(row)

    for year in data_by_year:
        filename = base_path + year + '.json'
        with open(filename, 'w') as f:
            json.dump(data_by_year[year], f, ensure_ascii=False)
