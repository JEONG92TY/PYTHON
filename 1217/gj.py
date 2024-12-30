from geojson import Feature, FeatureCollection, Point
import folium

feature1 = Feature(geometry=Point((126.978859, 37.530487)), properties={"name" : "Seoul", "population" : "9.7M"})
feature2 = Feature(geometry=Point((129.048819, 35.170231)), properties={"name" : "Busan", "population" : "3.4M"})
feature3 = Feature(geometry=Point((127.387481, 36.338929)), properties={"name" : "Daejeon", "population" : "1.5M"})
feature4 = Feature(geometry=Point((128.550659, 35.829521)), properties={"name" : "Daegu", "population" : "2.4M"})

geojson_data = FeatureCollection([feature1, feature2, feature3, feature4])

map = folium.Map(location=[36.396431, 128.004089], zoom_start=7)

folium.GeoJson(
    geojson_data,
    name="GeoJSON Data",
    tooltip = folium.GeoJsonTooltip(
        fields=["name", "population"],
        aliases=["도시이름 : ", "인구 : "]
    )
).add_to(map)

map.save("./1217/map_geo.html")