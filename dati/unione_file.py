import mapclassify
import folium
import matplotlib.pyplot as plt
from PIL import Image
import geopandas as gpd

shp_file = gpd.read_file ('/home/alessandro/Scrivania/pw_villaburi/dati/villa buri viale ingresso.shp')
csvfile = gpd.read_file ('/home/alessandro/Scrivania/pw_villaburi/dati/datiAlberi.csv')
dati_uniti = shp_file.merge(csvfile, on='id')
dati_uniti.to_file('/home/alessandro/Scrivania/pw_villaburi/nuovo_file.shp')


# Così dovreste riuscire a trovare gli id albero comuni tra i due
# Modo molto sporco, ci sono sicuramente metodi più veloci e puliti con altre funzioni/metodi in python

id_shp_file = shp_file['id']
id_csv_file = csvfile['id']

id_shp_file.sort()
id_csv_file.sort()

array_unito = []

for i in range(len(id_csv_file)):
    if (id_csv_file[i] == id_csv_file[i]):
        array_unito.append(id_csv_file[i])

# Da qui in poi c'è bisogno di prendere dai due dataset solo le righe con gli id nell'array che abbiamo creato

fixed_shp = []
fixed_csv = []

for i in range(len(id_shp_file)):
    if id_shp_file[i] in array_unito:
        fixed_shp.append(id_shp_file[i])

for i in range(len(id_csv_file)):
    if id_csv_file[i] in array_unito:
        fixed_csv.append(id_csv_file[i])

print(fixed_csv)

# Queste righe poi sono da mettere in un altro dataframe CREATO CON GEOPANDAS

common_ids = set(fixed_shp).intersection(set(fixed_csv))
nuovo_df = dati_uniti[dati_uniti['id'].isin(common_ids)]
