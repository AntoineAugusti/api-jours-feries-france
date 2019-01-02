import csv
import os
import json
from collections import defaultdict
from urllib.request import urlopen
from io import StringIO

DATA_GOUV = 'https://www.data.gouv.fr/s/resources/jours-feries-en-france/'

modes = [
    ('data/', DATA_GOUV + '20180704-205342/jours_feries_seuls.csv'),
    ('data/alsace-moselle/', DATA_GOUV + '20180705-154059/jours_feries_seuls_alsace_moselle.csv'),
]

for mode in modes:
    base_path, url = mode
    os.makedirs(base_path, exist_ok=True)

    response = urlopen(url).read().decode('utf-8')
    reader = csv.DictReader(StringIO(response))

    data_by_year = defaultdict(list)
    for row in reader:
        year = row['date'][0:4]
        del row['est_jour_ferie']
        data_by_year[year].append(row)

    for year in data_by_year:
        filename = base_path + year + '.json'
        with open(filename, 'w') as f:
            json.dump(data_by_year[year], f, ensure_ascii=False)
