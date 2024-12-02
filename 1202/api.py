import requests, json

url = "http://koreanjson.com/posts"
res = requests.get(url)

#print(res.json())
#print(res)

if res.status_code == 200 :
    data = res.json()
    for i in data :
        print(f"ID : {i["id"]}m 제목 : {i["title"]}")
    else :
        print("요청 실패")

#아래코드는 json에서 데이터를 받아올 때 주로 쓰는 코드로 외워두는게 좋다
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)