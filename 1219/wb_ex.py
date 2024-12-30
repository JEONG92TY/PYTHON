from tkinter import *
from bs4 import BeautifulSoup
import requests

url1 = "https://search.naver.com/search.naver?sm=tab_sug.aslt&where=nexearch&ssc=tab.nx.all&query=%EB%A1%9C%EB%98%90&oquery=%ED%8C%8C%EC%9D%B4%EC%8D%AC+%EC%A4%84%EB%B0%94%EA%BF%88&tqi=i2nFnlqVOsossu%2FNNm4ssssstVZ-275992&acq=%EB%A1%9C%EB%98%90&acr=1&qdt=0&acir=1"
response1 = requests.get(url1)
html1 = BeautifulSoup(response1.text, "html.parser")
#회차
ln= html1.select_one("div.select_tab > a")
lottery_num = ln.text[:4]
#당첨번호
wn = html1.select(".winning_number>span")
win_num = [num.text for num in wn]
###win_num = []
###for num in wn :
###    num = num.text
###    win_num.append(num)
#보너스번호
bonus_num = html1.select_one(".bonus_number>span")
#===================================================================================
def on_click():
    num = {"회차" : lottery_num,
               "당첨번호" : win_num,
               "보너스" : bonus_num.text}
    
    lot = lottery.get()

    if lot == num["회차"] :
        win_number.config(text=f"당첨번호 : {num["당첨번호"]} \n 보너스번호 : {num["보너스"]}"),

window = Tk()
window.title("로또 당첨 확인")
window.geometry("250x140")

label1 = Label(window, text="로또 회차 입력")
label1.grid(row=0, column=0)

lottery = Entry(window, width=10, bg="skyblue")
lottery.grid(row=1, column=0)

button = Button(window, text="당첨 번호 확인", command=on_click)
button.grid(row=2, column=1)

win_number = Label(window, width=30 , height=3 , bg="skyblue", text="")
win_number.grid(row=3, column=0, columnspan=2, padx=5)

window.mainloop()
