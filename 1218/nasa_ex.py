import folium
import requests
import pandas as pd
from folium.plugins import HeatMap
import cv2

api_url = "https://eonet.gsfc.nasa.gov/api/v3/events"
params = {
    "category:" : "wildfire",
    "status" : "open",
    "limit" : 100
}

response = requests.get(api_url, params=params)
data = response.json()
infos = data["events"]
#print(infos[0].get("geometry")[0].get("coordinates")[1])

wildfire_data = []

for info in infos :
    if data :
        data = api_url
        wildfire_data.append({
            "magnitude_value" : info.get("geometry")[0].get("magnitudeValue"),
            "latitude" :  info.get("geometry")[0].get("coordinates")[1],
            "longitude" :  info.get("geometry")[0].get("coordinates")[0]
        })

wildfire_df = pd.DataFrame(wildfire_data)

map = folium.Map(location=[36.396431, 128.004089], zoom_start=5)

ht_map = []

for _, row in wildfire_df.iterrows() :
    popup_info = f"""
    <b>magnitude_value : </b> {row["magnitude_value"]}<br />
    """
    icon_color = "blue" if row["magnitude_value"]<500 else "red"

    folium.Marker(
        location = [row["latitude"], row["longitude"]],
        popup=folium.Popup(popup_info, max_width=300),
        icon = folium.Icon(color = icon_color, icon = "fire")
    )

    ht_map.append([row["latitude"], row["longitude"]])

print(ht_map)

HeatMap(ht_map).add_to(map)
map.save("./1218/index.html")
#
#def download_image() :
#    api_url = "https://wvs.earthdata.nasa.gov/api/v1/snapshot"
#    params = {
#        "REQUEST" : "GetSnapshot",
#        "BBOX" : "-90, -180, 90, 180",
#        "WIDTH" : "1920",
#        "HEIGHT" : "1080",
#        "FORMAT" : "image/png",
#        "LAYERS" : "VIIRS_SNPP_CorrectedReflectance_TrueColor",
#        "CRS" : "EPSG:4326",
#        "TIME" : "2024-11-01"
#    }
#    res = requests.get(api_url, params=params, stream=True)
#    print(res)
#    with open("./1218/test.png", "wb") as file :
#        for chunk in res.iter_content(1024) :
#            file.write(chunk)
#
#download_image()
#
##def fire_result() :
##    image = cv2.imread("./1218/test.png")
##    if image is None :
##        return
#
