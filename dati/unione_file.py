#import mapclassify
#import folium
#import matplotlib.pyplot as plt
#from PIL import Image
import geopandas as gpd
import pandas as pd
import json

shp_file = gpd.read_file ("C:/Users/ronca/Desktop/pw_villaburi/dati/villa buri viale ingresso.shp")
csvfile = pd.read_csv("C:/Users/ronca/Desktop/pw_villaburi/dati/datiAlberi.csv", sep =";")

# Così dovreste riuscire a trovare gli id albero comuni tra i due
# Modo molto sporco, ci sono sicuramente metodi più veloci e puliti con altre funzioni/metodi in python

id_shp_file = shp_file['id']
id_csv_file = csvfile['id']

#print(len(id_shp_file), len(id_csv_file))

array_unito = []

array_unito = list(set(id_csv_file).intersection(id_shp_file))
# Da qui in poi c'è bisogno di prendere dai due dataset solo le righe con gli id nell'array che abbiamo creato

'''
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

new_shp_file = shp_file[shp_file['id'].isin(fixed_shp)]
new_csv_file = csvfile[csvfile['id'].isin(fixed_csv)]

fixed_dati_uniti = pd.merge(new_shp_file, new_csv_file, on = 'id')
'''

#print(fixed_dati_uniti)
#print(type(fixed_dati_uniti), len(fixed_dati_uniti))

#gdf = gpd.GeoDataFrame(fixed_dati_uniti, geometry = 'geometry')

'''

    Il risultato di queste operazioni è un nuovo geodataframe ma ha lunghezza 1910
    nvece quello che abbiamo trovato con gli id in comune era un array di 1887 elementi

    Questo perchè merge e intersection sono due tipi di unione diversi:
        - merge fa di default un inner join, mantiene i duplicati ma toglie i valori nulli
        - intersection rimuove i duplicati ma mantiene i valori nulli
        
    Quindi per avere un insieme pulito basta fare un merge, a partire dal GeoDataFrame (shp_file)
    sulla colonna ['id'] come riferimento e poi eseguire .drop_duplicates
    
'''


new_df = shp_file.merge(csvfile, how='inner', on='id')
df_no_duplicates = new_df.drop_duplicates(subset='id')

print(len(df_no_duplicates['id']))

'''

    Ora possiamo esportare questo file in geoJson come formato di facile utilizzo da mappare con leaflet
    Idealmente questo processo non verrà fatto esportando a mano ogni volta il file ma prenderno direttamente
    la versione aggiornata del DB che andremo a creare

'''

df_no_duplicates.to_file("alberi.geojson", driver='GeoJSON')

#funzione per leggere in file geojson

with open('alberi.geojson', 'r') as f:

    data = json.load(f)

print(data)






