import csv
import json
import os
from collections import defaultdict
from datetime import datetime
from io import StringIO
from urllib.request import urlopen

modes = [
    (
        "data/",
        "https://etalab.github.io/jours-feries-france-data/csv/jours_feries_metropole.csv",
    ),
    (
        "data/alsace-moselle/",
        "https://etalab.github.io/jours-feries-france-data/csv/jours_feries_alsace-moselle.csv",
    ),
]

for mode in modes:
    base_path, url = mode
    os.makedirs(base_path, exist_ok=True)

    response = urlopen(url).read().decode("utf-8")
    reader = csv.DictReader(StringIO(response))

    data_by_year = defaultdict(list)
    for row in reader:
        year = int(row["date"][0:4])
        row["annee"] = int(row["annee"])
        data_by_year[year].append(row)

    if max(data_by_year.keys()) < datetime.today().year + 5:
        raise ValueError("We should have bank holidays for 5 years")

    for year in data_by_year:
        filename = base_path + str(year) + ".json"
        with open(filename, "w") as f:
            json.dump(data_by_year[year], f, ensure_ascii=False)
