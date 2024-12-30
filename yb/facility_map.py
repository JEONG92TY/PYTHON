import pandas as pd
import folium
import geopandas as gpd
from shapely.geometry import Point
from matplotlib.colors import Normalize, rgb2hex
import plotly.express as px
from folium import IFrame
import json

# from geojson import Feature, FeatureCollection, Polygon
# from folium.plugins import HeatMap, MarkerCluster, DualMap


facility_df = pd.read_csv("./yb/fa_data/2023_신규_발전소_설치.csv", encoding="euc-kr")
e_power_df = pd.read_csv("./yb/fa_data/2023_신규_발전량.csv", encoding="euc-kr")

facility_df.columns = ["loc_nm", "facility_capacity","facility_count", "latitude", "longitude"]
e_power_df.columns = ["loc_nm", "2023-01", "2023-02", "2023-03", "2023-04", "2023-05","2023-06", "2023-07", "2023-08", "2023-09", "2023-10", "2023-11", "2023-12", "latitude", "longitude"]



#----------------------------------------------------facility_df
# geojson 읽어오기
geojson = gpd.read_file("./yb/fa_data/법정구역_시군구.geojson", encoding="utf-8")
print(geojson)

# 발전소 포인트 찍기
geo_point = []
for _, data in facility_df.iterrows():
    # data = pd.DataFrame(data)
    # print(data)
    facility_point = Point(data["longitude"], data["latitude"])
    # 포인트 포함된 지역
    zone_point = geojson[geojson.contains(facility_point)]

    # zone_point에 포인트지역 넣기
    if not zone_point.empty:
        zone_name = zone_point.iloc[0]['CTP_KOR_NM']
    else:
        zone_name = None
    
    # geo_point 리스트에 append
    geo_point.append(zone_name)

# 색상데이터를 위한 count 노멀라이즈
facility_df["facility_count"] = facility_df["facility_count"].str.replace(",", "").astype(float)
norm = Normalize(vmin=facility_df["facility_count"].min(), vmax=facility_df["facility_count"].max())
facility_df['normalized_count'] = facility_df['facility_count'].apply(norm)

# 발전소 데이터에 새로 컬럼 추가해서 해당하는 지역이름 넣기
facility_df["CTP_KOR_NM"] = geo_point
# merge~
merge_geojson = pd.merge(geojson, facility_df, left_on="CTP_KOR_NM", right_on="CTP_KOR_NM", how="left")

#------------------------------e_power_df 파이차트
# import io
# import matplotlib.pyplot as plt

# pie_charts_data = zip(e_power_df['2023-01'],
#                       e_power_df['2023-02'],
#                       e_power_df['2023-03'],
#                       e_power_df['2023-04'],
#                       e_power_df['2023-05'],
#                       e_power_df['2023-06'],
#                       e_power_df['2023-07'],
#                       e_power_df['2023-08'],
#                       e_power_df['2023-09'],
#                       e_power_df['2023-10'],
#                       e_power_df['2023-11'],
#                       e_power_df['2023-12'],  
#                       )

# # 파이차트 만들기
# fig = plt.figure(figsize=(0.5, 0.5))
# fig.patch.set_alpha(0)
# ax = fig.add_subplot(111)
# plots = []

# for sizes in pie_charts_data:
#     ax.pie(sizes, colors=("#c93c3c", "#c9773c", "#faee41", "#85fa41", "#41faea", "#418bfa", "#25257a", "#9148f7", "#dd48f7", "#f748bd", "#9de3d7"))
#     buff = io.StringIO()
#     plt.savefig(buff, format="SVG")
#     buff.seek(0)
#     svg = buff.read()
#     svg = svg.replace("\n", "")
#     plots.append(svg)
#     plt.cla()
# plt.clf()
# plt.close()

#------------------------------ 맵 생성/저장


m = folium.Map(location=[37.56, 126.98], zoom_start=7,
               tiles="cartoDB Positron")  # 기준지역 맵 생성

# 색상

# 스타일함수
def colormap(value):
    return rgb2hex((value, 1 - value, 0))


def style_function(x):
    facility_count = x["properties"].get("normalized_count", 0)
    print(facility_count)
    return {
        "fillColor": colormap(facility_count),
        "color": "black",
        "weight": 1,
        "fillOpacity": 0.4,
    }

# geojson 저장 / 툴팁, 스타일, 팝업

gm = folium.GeoJson(
    merge_geojson,
    tooltip=folium.GeoJsonTooltip(fields=["CTP_KOR_NM", "facility_capacity", "facility_count"],
                                   aliases=["지역명:", "설비 용량 (KW) :", "설비 개수:"],),
    style_function=style_function
)

for i in range(17) :
    name = e_power_df.columns[1:13]
    value = e_power_df.iloc[i, 1:13]
    fig = px.bar( y=value ,x=name)
    html = fig.to_html(include_plotlyjs="cdn")
    iframe = IFrame(html, width=400, height=300)
    popup = folium.Popup(iframe, max_width=500).add_to(gm)

gm.add_to(m)

m.save("./yb/발전소.html")
