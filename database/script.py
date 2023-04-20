import json

with open('C:/Users/ronca/Desktop/pw_villaburi/database/output.geojson') as f:
    data = json.load(f)

for feature in data['features']:
    # Verifica se la feature ha la proprietà 'Diametro (cm)' e il valore è '/'
    if 'properties' in feature and 'Diametro (cm)' in feature['properties'] and feature['properties']['Diametro (cm)'] == '/':
        feature['properties']['Diametro (cm)'] = '10'
    # Verifica se la feature ha la proprietà 'Altezza' e il valore è '/'
    if 'properties' in feature and 'Altezza' in feature['properties'] and feature['properties']['Altezza'] == '?':
        feature['properties']['Altezza'] = '1'
    # Verifica se la feature ha la proprietà 'Nome scientifico' e il valore è '/'
    if 'properties' in feature and 'Nome scientifico' in feature['properties'] and feature['properties']['Nome scientifico'] == '?':
        feature['properties']['Nome scientifico'] = 'specie sconosciuta'
    # Verifica se la feature ha la proprietà 'comune' e il valore è '/'
    if 'properties' in feature and 'Nome comune' in feature['properties'] and feature['properties']['Nome comune'] == '?':
        feature['properties']['Nome comune'] = 'specie sconosciuta' 
for key, value in feature['properties'].items():
        if value == 'specie sconosciuta':
            print(value)
'''with open('output.geojson', 'w') as file:
    json.dump(data, file)'''
