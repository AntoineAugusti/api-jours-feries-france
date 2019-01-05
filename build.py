import csv
import json
import os
from collections import defaultdict
from datetime import datetime
from io import StringIO
from urllib.request import urlopen

DATA_GOUV = 'https://www.data.gouv.fr/fr/datasets/r/'

modes = [
    ('data/', DATA_GOUV + 'cc620384-4ccf-41ae-a7ba-9eceacb7b6db'),
    ('data/alsace-moselle/', DATA_GOUV + '944504ac-2592-4503-acd9-6befe8942ae2'),
]

for mode in modes:
    base_path, url = mode
    os.makedirs(base_path, exist_ok=True)

    response = urlopen(url).read().decode('utf-8')
    reader = csv.DictReader(StringIO(response))

    data_by_year = defaultdict(list)
    for row in reader:
        year = int(row['date'][0:4])
        del row['est_jour_ferie']
        data_by_year[year].append(row)

    if max(data_by_year.keys()) < datetime.today().year + 15:
        raise ValueError('We should have bank holidays for 15 years')

    for year in data_by_year:
        filename = base_path + str(year) + '.json'
        with open(filename, 'w') as f:
            json.dump(data_by_year[year], f, ensure_ascii=False)
