import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import font_manager
import pandas as pd


path = 'C:/WINDOWS/Fonts/malgun.TTF'
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)


file_name = "./1211/연령별인구현황_성별.csv"
data = pd.read_csv(file_name, encoding="EUC-KR")


region_name = input("검색하고 싶은 지역명을 입력하세요 : ")
data = data.rename(columns={"행정구역" : "지역명"})
male_age_colmns = [ col for col in data.columns if "세" in col and "남" in col]
female_age_colmns = [ col for col in data.columns if "세" in col and "여" in col]

for col in male_age_colmns :
    data[col] = data[col].astype(str).str.replace(",", "").astype(int)

for col in female_age_colmns :
    data[col] = data[col].astype(str).str.replace(",", "").astype(int)

region_data = data[ data["지역명"].str.contains(region_name, na=False)]

if region_data.empty :
    print(f"{region_name} - 지역은 존재하지 않습니다.")


age_groups = [col.split("남")[1] for col in male_age_colmns]
male_result = region_data[male_age_colmns].iloc[0].values
female_result = region_data[female_age_colmns].iloc[0].values

plt.figure(figsize = (10,8))
plt.xlabel("연령대")
plt.ylabel("인구수")
plt.plot(age_groups, male_result, female_result)
plt.title(f"2024년 11월 {region_name} 지역 세대별 남녀 인구수 ")
plt.legend(["남성", "여성"], loc = "upper right")
plt.grid(linestyle="--", alpha=0.5)

plt.show()