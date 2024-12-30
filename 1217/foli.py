import folium

map = folium.Map(location=[37.651912, 126.866301], zoom_start=12,
                 title="my_home")

map_info = [
    {"location" : [37.634669, 126.832886], "popup" : "화정역"},
    {"location" : [37.653404, 126.843049], "popup" : "원당역"},
    {"location" : [37.650792, 126.873270], "popup" : "원흥역"},
    {"location" : [37.653273, 126.895493], "popup" : "삼송역"},
    {"location" : [37.648272, 126.913831], "popup" : "지축역"}
]

for info in map_info :
    folium.Marker(
        location = info["location"],
        popup = info["popup"],
        icon = folium.Icon(color="red", icon="subway")
    ).add_to(map)

map.save("./1217/map.html")