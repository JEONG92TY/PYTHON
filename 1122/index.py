'''
dic1 = {}
print(dic1)
dic1 = dict()
print(dic1)
dic1 = {
    "name": "홍길동",
    "age" : "100",
    "city": "서울",
    #"hobby" : ["탁구", "배드민턴", "게임"]
}
print(dic1)
print(dic1["name"])
#print(dic1["hobby"][1])

dic1["name"] = "정태영"
print(dic1)
dic1["birthday"] = "19920105"
print(dic1)

fruit = {
    "apple" : "사과",
    "banana" : "바나나"
}
print(fruit.get("apple"))
print(fruit.get("peach"))
print(fruit.get("peach", "복숭아"))
fruit.update({
    "grape" : "포도",
    "melon" : "멜론"
})
print(fruit)
print(fruit.keys())
print(fruit.values())
print(fruit.items())

#1
score = {}
print(score)
#2
score = {
    "Alice" : 85,
    "Bob" : 90,
    "Charlie" : 95
}
print(score)
#3
score["David"] = 80
print(score)
#4
score["Alice"] = 88
print(score)
#5
del score["Bob"]
print(score)
'''

names = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 90, 95, 88]
zipped = list(zip(names, scores))
print(zipped)