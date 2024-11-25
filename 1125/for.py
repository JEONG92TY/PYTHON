'''
fruit = ["사과", "복숭아", "포도", "바나나"]
for fru in fruit :
    print("과일은 : ", fruit)
'''
'''
number = [10, 20, 30, 40, 50]
total = 0
for num in number :
    total += num
print(total)
'''
'''
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in number :
    if num % 2 == 0:
        print(num, end=" ")
'''
'''
square = [ i**2 for i in range(1, 20)]
print(square)
'''
'''
even_square = [i**2 for i in range(1,10) if i % 2 == 0]
print(even_square)
'''
'''
my_dic = {
    "name" : "홍길동",
    "address" : "서울시",
    "gender" : "남자",
    "hobby" : ["런닝", "헬스", "낚시"]
}
for i in my_dic :
    print(i, end=" ")
print()
for i in my_dic.keys() :
    print(i, end=" ")
print()
for i in my_dic.values() :
    print(i, end=" ")
print()
for i in my_dic.items() :
    print(i, end=" ")
'''
'''
i = int(input("몇 단을 출력할까요? : "))
j = 1
for j in range(1,10) :
    print(f"{i} * {j} = {i * j}")
'''
'''
i = int(input("어디까지 계산할까요? : "))
num = [i for i in range(1,i+1) if i % 2 != 0]
print(num)
print(sum(num))
'''
'''
dic = {
    "학생1" : [83, 92, 88],
    "학생2" : [90, 79, 86],
    "학생3" : [88, 86, 94]
    }

len = len(dic.get("학생1"))

for i in dic :
    ave = sum(dic.get(i))/len
    print(f"{i}의 국영수 평균은 : {ave:.1f} 입니다.")
'''
'''
for i in range(5) :
    for j in range(3) :
        print(f"i : {i}, j : {j}")
    print()
'''
'''
mat = [
    [3, 6, 9, 12],
    [2, 4, 6, 8],
    [10, 20, 30, 40],
    [11, 12, 13, 14]
]
for row in mat :
    for ele in row :
        if ele % 3 == 0 :
            print(ele, end=" ")
'''
'''
for i in range(2,10) :
    print(f"[{i} 단]")
    for j in range(1,10) :
        print(f"{i} * {j} = {i*j}")
    print()
'''