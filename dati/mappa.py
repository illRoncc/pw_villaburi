import mapclassify 
import folium 
import matplotlib.pyplot as plt
from PIL import Image
import geopandas as gpd

shp_file = gpd.read_file ('/home/alessandro/Scrivania/pw_villaburi/dati/villa buri viale ingresso.shp')
shp_file.set_crs (epsg = 3003, inplace = True, allow_override = True)
print(shp_file.crs)
shp_file.plot(figsize = (10,10), alpha = 0.5, edgecolor ='k')
plt.savefig('plot.png')
with Image.open('plot.png') as img :
    img.show()
shp_file.explore()
csvfile = gpd.read_file ('/home/alessandro/Scrivania/pw_villaburi/dati/datiAlberi.csv')
dati_uniti = shp_file.merge(csvfile, on='Numero piante')
dati_uniti.to_file('/home/alessandro/Scrivania/pw_villaburi/nuovo_file.shp')
