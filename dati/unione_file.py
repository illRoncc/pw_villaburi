import mapclassify 
import folium 
import matplotlib.pyplot as plt
from PIL import Image
import geopandas as gpd

shp_file = gpd.read_file ('/home/alessandro/Scrivania/pw_villaburi/dati/villa buri viale ingresso.shp')
csvfile = gpd.read_file ('/home/alessandro/Scrivania/pw_villaburi/dati/datiAlberi.csv')
dati_uniti = shp_file.merge(csvfile, on='id')
dati_uniti.to_file('/home/alessandro/Scrivania/pw_villaburi/nuovo_file.shp')