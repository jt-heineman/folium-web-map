import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def returnColorElevation(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(zoom_start=1,tiles="OpenStreetMap",height="80%",width="80%")
data = pandas.read_csv("Volcanoes.txt",delimiter=",")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
html = """<h4>Volcano information:</h4>
Name: %s <br> Height: %s m
"""
fg = folium.FeatureGroup(name="Volcanoes") #better method, create a feature group. helps make code organized. and work with layers
for lt, ln, el, desc  in zip(lat, lon, elev, name):
    newcolor = returnColorElevation(el)
    iframe = folium.IFrame(html=html % (str(desc), str(el)), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe), radius=6, fill_color=newcolor, color="grey", fill_opacity=0.7, fill=True))
fg2 = folium.FeatureGroup(name="Countries")
fg2.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor' : 'green' if x['properties']['POP2005'] < 5000000
else 'orange' if 5000000 <= x['properties']['POP2005'] < 200000000 
else 'red'}))
map.add_child(fg2)
map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("Map1.html")
#return map._repr_html_()
