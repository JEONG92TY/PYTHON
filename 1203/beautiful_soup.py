from bs4 import BeautifulSoup
import requests

'''
html_str = """
<html>
    <body>
        <div id = "content">
            <ul  class = "industry">
                <li>인공지능</li>
                <li>빅데이터</li>
                <li>신재생에너지</li>
            </ul>
            <ul  class = "comlang">
                <li>Python</li>
                <li>C++</li>
                <li>javescript</li>
            </ul>
        </div>
    </body>
<html>
"""
'''

#soup = BeautifulSoup(html_str, "html.parser")
#print(soup)
#first_ul = soup.find("ul")
#print(first_ul.text)
#<li>인공지능</li> >> html
#인공지능 >> text

#all_ul = soup.find_all("ul")
#print(all_ul[1].text)

#class_ul = soup.find("ul", attrs ={"class" : "comlang"})
#print(class_ul.text)

#first_ul = soup.select_one("ul.industry")
#print(first_ul)

#all_ul = soup.select("div > ul")
#print(all_ul)

"""
html_url = "https://www.seoul.go.kr/main/index.jsp"
res = requests.get(html_url)
#print(res.text)
soup = BeautifulSoup(res.text, "html.parser")
all_nav = soup.select("nav > ul > li >a")
#print(all_nav)
for i in all_nav :
    print(i.text)
"""
html_url = "https://quotes.toscrape.com/"
res = requests.get(html_url)
soup = BeautifulSoup(res.text, "html.parser")

quote = soup.select(".quote > .text")

#for i in quote : 
#    print(i.text.strip())

list = [i.text.strip() for i in quote]
print(list)