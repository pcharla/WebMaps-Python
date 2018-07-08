import folium
import pandas
data= pandas.read_csv('Volcanoes_USA.txt')
latitudes= list(data['LAT'])
longitudes= list(data['LON'])
#names= list(data['NAME'])
elevation= list(data['ELEV'])
def classify(m):
  if m > 3000:
    return'red'
  elif m>1500:
    return'green'
  else:
    return 'blue'

mylocation= folium.Map(location=[37.4467,25.3289], zoom_start=6,tiles='Mapbox Bright')

featuregroupv= folium.FeatureGroup(name='Volcanoes')

for i, j, elev in zip(latitudes, longitudes, elevation) :
#featuregroup.add_child(folium.Marker(location=[37,25], popup= str(n), icon= folium.Icon(color='red')))
  #featuregroup.add_child(folium.Marker(location=[i,j], popup= folium.Popup(n,parse_html= True), icon= folium.Icon(color='red')))
   #featuregroup.add_child(folium.Circle(location=[i,j], radius=0.5,  popup= str(elev), color = classify(elev)))
  featuregroupv.add_child(folium.CircleMarker(location=[i,j], radius=6,  popup= str(elev)+'m', fill_color = classify(elev), color='grey', fill= True, fill_opacity=0.7))

featuregroupp= folium.FeatureGroup(name='Population')

featuregroupp.add_child(folium.GeoJson(data= open('world.json','r',encoding= 'utf-8-sig').read(),style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] <= 10000000 else 'orange' if 10000000 < x['properties']['POP2005'] < 20000000 else 'red'}))

mylocation.add_child(featuregroupv)
mylocation.add_child(featuregroupp)
mylocation.add_child(folium.LayerControl())
mylocation.save('Mikonos.html')
