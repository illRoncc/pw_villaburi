import geopandas as gpd

# Carica il GeoDataFrame dal file GeoJSON
gdf = gpd.read_file("C:/Users/ronca/Desktop/pw_villaburi/database/utente.geojson")

# Rinomina la colonna 'Altezza' in 'Altezza (m)'
gdf = gdf.rename(columns={'Altezza': 'Altezza (approssimata in metri)'})

# Salva il nuovo GeoDataFrame in un file GeoJSON
gdf.to_file("C:/Users/ronca/Desktop/pw_villaburi/database/nuovo.geojson", driver='GeoJSON')
