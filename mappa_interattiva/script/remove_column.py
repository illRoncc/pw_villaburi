import geopandas as gpd
import json
import geojson

gdf = gpd.read_file('C:/Users/ronca/Desktop/pw_villaburi/database/finale.geojson')

# Rimozione della colonna "id"
gdf.drop(columns=["id"], inplace=True)
gdf.drop(columns=["Multifusto"], inplace=True)
gdf.drop(columns=["Stato"], inplace=True)

# Creazione di un nuovo GeoDataFrame senza la colonna "id"
new_gdf = gpd.GeoDataFrame(gdf)

output_file_path = "C:/Users/ronca/Desktop/pw_villaburi/database/utente.geojson"  # Inserisci il percorso del nuovo file GeoJSON
new_gdf.to_file(output_file_path, driver='GeoJSON')