import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import font_manager
import pandas as pd


path = 'C:/WINDOWS/Fonts/malgun.TTF'
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)


file_name = "./1211/연령별인구현황.csv"
data = pd.read_csv(file_name, encoding="EUC-KR")

region_name = input("검색하고 싶은 지역명을 입력하세요 : ")
data = data.rename(columns={"행정구역" : "지역명"})
age_colmns = [ col for col in data.columns if "세" in col]

for col in age_colmns :
    data[col] = data[col].str.replace(",", "").astype(int)

print(data.head())
'''
region_data = data[ data["지역명"].str.contains(region_name, na=False)]

if region_data.empty :
    print(f"{region_name} - 지역은 존재하지 않습니다.")

age_groups = [col.split("계")[1] for col in age_colmns]
result = region_data[age_colmns].iloc[0].values

plt.figure(figsize = (10,8))
plt.plot(age_groups, result, marker="o", label=region_name)
plt.title(f"{region_name}", fontsize=16, pad=10)
plt.xlabel("AGE")
plt.ylabel("NUM OF PEO")
plt.grid(True, linestyle="--", alpha=0.6)
plt.xticks(rotation=45)
plt.legend()
plt.show()

#print(region_data[age_colmns].iloc[0].values)
'''