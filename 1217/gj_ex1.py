from geojson import Feature, FeatureCollection, Point, Polygon
import folium

locations = Feature(
    goemetry = Polygon([[
        [126.376661, 37.813387],
        [126.675748, 37.777837],
        [127.083821, 38.230695],
        [127.528767, 37.971333],
        [127.501301, 37.682800],
        [127.800679, 37.550088],
        [127.641377, 37.141776],
        [126.913533, 36.937886]
    ]]), properties = {"name" : "수도권"}
)

data = FeatureCollection([locations])
map = folium.Map(location=[36.396431, 128.004089], zoom_start=7.2)

folium.GeoJson(
    data,
    name = "map",
    tooltip=folium.GeoJsonTooltip(
        fields = ["name"],
        aliases = ["영역 이름 : "]
    )
).add_to(map)

'''
folium.Polygon(
    locations=locations, # 다각형 좌표 입력
    fill_color="skyblue", # 채우기 색상
    fill_opacity=0.5, # 채우기 투명도
    color="blue", # 테두리 색상
    weight=3, # 테두리 두께
    opacity=1, # 테두리 투명도
    popup=folium.Popup("영역 이름 : 수도권", parse_html=True, max_width=100)
).add_to(map)
'''

map.save("./1217/map_geo_ex.html")