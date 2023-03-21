import mapclassify
import folium
import matplotlib.pyplot as plt
from PIL import Image
import geopandas as gpd
import pandas as pd

shp_file = gpd.read_file ("C:/Users/ronca/Desktop/pw_villaburi/dati/villa buri viale ingresso.shp")
csvfile = pd.read_csv("C:/Users/ronca/Desktop/pw_villaburi/dati/datiAlberi.csv",sep =";")

# Così dovreste riuscire a trovare gli id albero comuni tra i due
# Modo molto sporco, ci sono sicuramente metodi più veloci e puliti con altre funzioni/metodi in python

id_shp_file = shp_file['id']
id_csv_file = csvfile['id']

array_unito = []

array_unito = list(set(id_csv_file).intersection(id_shp_file))
# Da qui in poi c'è bisogno di prendere dai due dataset solo le righe con gli id nell'array che abbiamo creato

# Queste righe poi sono da mettere in un altro dataframe CREATO CON GEOPANDAS
fixed_shp = []
fixed_csv = []

for i in range(len(id_shp_file)):
    if id_shp_file[i] in array_unito:
        if id_shp_file[i] not in fixed_shp:
            fixed_shp.append(id_shp_file[i])

for i in range(len(id_csv_file)):
    if id_csv_file[i] in array_unito:
        fixed_csv.append(id_csv_file[i])

print(len(fixed_csv), len(fixed_shp))