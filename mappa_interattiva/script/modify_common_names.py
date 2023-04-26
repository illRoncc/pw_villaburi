import geopandas as gpd

# leggi il file GeoJSON come un GeoDataFrame
gdf = gpd.read_file("C:/Users/ronca/Desktop/pw_villaburi/database/nuovo_modificato.geojson")

# itera su ogni feature e cambia il nome comune se contiene 'acero'
for idx, row in gdf.iterrows():
    nome_comune = row['Nome comune']
    if 'Abete Rosso' in nome_comune.lower():
        gdf.loc[idx, 'Nome comune'] = 'Abete rosso'

for idx, row in gdf.iterrows():
    nome_comune = row['Nome comune']
    if 'corniolo' in nome_comune.lower():
        gdf.loc[idx, 'Nome comune'] = 'Corniolo'

for idx, row in gdf.iterrows():
    nome_comune = row['Nome comune']
    if 'sambuco' in nome_comune.lower():
        gdf.loc[idx, 'Nome comune'] = 'Sambuco'

for idx, row in gdf.iterrows():
    nome_comune = row['Nome comune']
    if 'noce nero' in nome_comune.lower():
        gdf.loc[idx, 'Nome comune'] = 'Noce nero'
        
# salva il file GeoJSON con i nomi comuni modificati
gdf.to_file("C:/Users/ronca/Desktop/pw_villaburi/database/nuovo_modificato.geojson", driver='GeoJSON')

