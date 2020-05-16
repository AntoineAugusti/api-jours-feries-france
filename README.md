# API Jours Fériés France

⚠️ **Ce projet n'est plus maintenu et le service web peut être arrêté à tout moment. Veuillez utiliser [l'API d'Etalab](https://github.com/etalab/jours-feries-france-api), fonctionnant de manière similaire.** ⚠️

---

Une API pour lister les jours fériés en France. Ceci se base sur les données [du package suivant](https://github.com/AntoineAugusti/jours-feries-france).

## Déploiement et hébergement
Le déploiement est assuré par Netlify, le fichier de build se trouve dans `build.py`.

## Endpoints
Les endpoints retournent des données au format JSON.

- Les jours fériés pour une année : `https://jours-feries-france.antoine-augusti.fr/api/:annee`

Exemple :
- https://jours-feries-france.antoine-augusti.fr/api/2019
```json
[
  {"date": "2019-01-01", "nom_jour_ferie": "Jour de l'an"},
  {"date": "2019-04-22", "nom_jour_ferie": "Lundi de Pâques"},
  {"date": "2019-05-01", "nom_jour_ferie": "Fête du travail"},
  {"date": "2019-05-08", "nom_jour_ferie": "Victoire des alliés"},
  {"date": "2019-05-30", "nom_jour_ferie": "Ascension"},
  {"date": "2019-06-10", "nom_jour_ferie": "Lundi de Pentecôte"},
  {"date": "2019-07-14", "nom_jour_ferie": "Fête Nationale"},
  {"date": "2019-08-15", "nom_jour_ferie": "Assomption"},
  {"date": "2019-11-01", "nom_jour_ferie": "Toussaint"},
  {"date": "2019-11-11", "nom_jour_ferie": "Armistice"},
  {"date": "2019-12-25", "nom_jour_ferie": "Noël"}]
```

- Les jours fériés pour une année, en Alsace-Moselle : `https://jours-feries-france.antoine-augusti.fr/api/alsace-moselle/:annee`

Exemple :
- https://jours-feries-france.antoine-augusti.fr/api/alsace-moselle/2019
```json
[
  {"date": "2019-01-01", "nom_jour_ferie": "Jour de l'an"},
  {"date": "2019-04-19", "nom_jour_ferie": "Vendredi Saint"},
  {"date": "2019-04-22", "nom_jour_ferie": "Lundi de Pâques"},
  {"date": "2019-05-01", "nom_jour_ferie": "Fête du travail"},
  {"date": "2019-05-08", "nom_jour_ferie": "Victoire des alliés"},
  {"date": "2019-05-30", "nom_jour_ferie": "Ascension"},
  {"date": "2019-06-10", "nom_jour_ferie": "Lundi de Pentecôte"},
  {"date": "2019-07-14", "nom_jour_ferie": "Fête Nationale"},
  {"date": "2019-08-15", "nom_jour_ferie": "Assomption"},
  {"date": "2019-11-01", "nom_jour_ferie": "Toussaint"},
  {"date": "2019-11-11", "nom_jour_ferie": "Armistice"},
  {"date": "2019-12-25", "nom_jour_ferie": "Noël"},
  {"date": "2019-12-26", "nom_jour_ferie": "Saint Étienne"}]
```


## Licence
MIT
