from bs4 import BeautifulSoup
import requests

html_url = "https://www.yna.co.kr/view/AKR20241203139851004?section=society/all&site=topnews01"
res = requests.get(html_url)
soup = BeautifulSoup(res.text, "html.parser")

title = soup.select("h1.tit")
publication_date = soup.select(".update-time")
body = soup.select("article.story-news > p")

print(publication_date)
#for i in title :
#    print(f"제목 : {i.text}")

#for i in publication_date :
#    print(f"발행일 : {i.text}")

#for i in body :
#    print(i.text)