import json
import pandas as pd
import geojson

# Carico il file GeoJSON
with open('C:/Users/ronca/Desktop/pw_villaburi/database/finale.geojson') as f:
    data = json.load(f)

# Aggiorno i valori numerici nel file GeoJSON originale
count = 0
for feature in data['features']:
    value = feature['properties']['Diametro (cm)']
    if value == '>100':
        value = 100 
    try:
        value = float(value)
    except ValueError:
        value = None
    feature['properties']['Diametro (cm)'] = value
    count += 1

print(f"Numero totale di righe stampate: {count}")

# Creo un dizionario di righe con i nuovi valori numerici
rows = []
for feature in data['features']:
    value = feature['properties']['Diametro (cm)']
    rows.append({'id': feature['properties']['id'], 'Diametro (cm)': value})

# Creo un nuovo DataFrame a partire dal dizionario di righe
new_df = pd.DataFrame(rows)

# Carico il file GeoJSON come oggetto geojson
with open('C:/Users/ronca/Desktop/pw_villaburi/database/finale.geojson') as f:
    gj = geojson.load(f)

# Aggiorno i valori numerici nell'oggetto geojson
for feature in gj['features']:
    feature_id = feature['properties']['id']
    new_value = new_df.loc[new_df['id'] == feature_id, 'Diametro (cm)'].iloc[0]
    if pd.isna(new_value):
        continue
    feature['properties']['Diametro (cm)'] = new_value

# Salvo l'oggetto geojson in un file
with open('C:/Users/ronca/Desktop/pw_villaburi/database/finale2.geojson', 'w') as f:
    geojson.dump(gj, f)