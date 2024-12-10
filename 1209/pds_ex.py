import pandas as pd

file_name = "./1209/서울특별시_공원 내 운동기구 설치 현황_20201231.csv"
df = pd.read_csv(file_name, encoding="cp949")

df.columns = ["p_name", "p_loc", "eqi_name", "amt", "mng_num", "mng_org"]

#======================= 1번 ========================
result1 = df.groupby("p_name").agg({
    "amt" : "sum"
    })
result1.to_string('result1.txt')
#======================= 2번 ========================
result2 = df.groupby("eqi_name").agg({
    "amt" : "sum"
    })
result2.to_string('result2.txt')
#======================= 3번 ========================
result3 = df.groupby("mng_org").agg({
    "amt" : "sum"
    })
result3.to_string('result3.txt')
#======================= 4번 ========================
result4 = df.loc[df["p_name"] == " 남산공원(회현) "]
result4.to_csv('result4.txt', sep = '\t')
#======================= 5번 ========================
result5 = df.loc[df["eqi_name"] == " 스텝사이클 "]
result5.to_csv('result5.txt', sep = '\t')
#======================= 6번 ========================
ex6 = df.groupby("eqi_name").agg({
    "amt" : "sum"
    })
result6 = ex6.sort_values("amt", ascending = False)
result6.to_csv('result6.txt', sep = '\t')
