from bs4 import BeautifulSoup
import numpy as np
import requests

html_url = "https://www.koreabaseball.com/Record/TeamRank/TeamRankDaily.aspx"
res = requests.get(html_url)
soup = BeautifulSoup(res.text, "html.parser")

data = soup.select("table >  tbody > tr")

list = [["순위", "팀", "승", "패", "무", "승률"]]

for item in data[:10] :

    rank = (item.select_one("td:nth-child(1)").text).strip()
    team = (item.select_one("td:nth-child(2)").text).strip()
    win = (item.select_one("td:nth-child(4)").text).strip()
    lose = (item.select_one("td:nth-child(5)").text).strip()
    draw = (item.select_one("td:nth-child(6)").text).strip()
    rate = (item.select_one("td:nth-child(7)").text).strip()
    
    list.append([rank, team, win, lose, draw, rate])


kbo_arr = np.array(list)

file_name = "2024_kbo_raking.txt"

with open(file_name, "w", encoding="utf-8") as file :
    file.write("========= 2024 한국 프로야구 성적표 =========\n")
    for i in kbo_arr :
        file.write("\t".join(i)+"\n")

with open(file_name, "r", encoding = "utf-8") as file :
    print(file.read())