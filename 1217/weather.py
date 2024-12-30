import folium
import requests
import pandas as pd

API_KEY = "273fddb8e35e585a709181c3c28f9045"

def get_weather_data(lat, lon) :
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=kr"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else : 
        return None

cities = [
    {"name" : "Seoul", "lat" : 37.551449, "lon" : 126.989974},
    {"name" : "Busan", "lat" : 35.170231, "lon" : 129.048819},
    {"name" : "Daejeon", "lat" : 36.338929, "lon" : 127.387481},
    {"name" : "Daegu",  "lat" : 35.829521, "lon" : 128.550659}
]

weather_data = []

for city in cities :
    data = get_weather_data(city["lat"], city["lon"])
    if data :
        weather_data.append({
            "city" : city["name"],
            "temperature" : data["main"]["temp"], 
            "weather" : data["weather"][0]["description"],
            "latitude" :  city["lat"],
            "longitude" : city["lon"]
        })

weather_df = pd.DataFrame(weather_data)

map = folium.Map(location=[36.396431, 128.004089], zoom_start=7.2)

for _, row in weather_df.iterrows() :
    popup_info = f"""
    <b>city : </b> {row["city"]}<br />
    <b>temp : </b> {row["temperature"]} ℃<br />
    <b>weather : </b> {row["weather"]}
    """
    icon_color = "blue" if row["temperature"]< 0 else "red"

    folium.Marker(
        location = [row["latitude"], row["longitude"]],
        popup=folium.Popup(popup_info, max_width=300),
        icon = folium.Icon(color = icon_color, icon = "cloud")
    ).add_to(map)

map.save("./PYTHON/index.html")