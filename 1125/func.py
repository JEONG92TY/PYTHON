'''
def hi() :
    print("hi")
'''
'''
def old(name, born) :
    age = 2024 - born
    print(f"{name} 님의 나이는 {age}세 입니다.")

old("정태영", 1992)
'''
'''
def gugu(start, end) :
    print(f"[{start} 단]")
    for i in range(1,end+1) :
        print(f"{start} * {i} = {start * i}")

gugu(2,9)
'''
'''
def cal(num1, num2) :
    total = 0
    for i in range(num1, num2+1) :
        total += i
    return total

c = cal(2,5)
print(c)
'''
'''
def fruit() :
    return ["apple", "banana", "peach"]

print(fruit())
'''
'''
def stu() :
    return {
        "name" : "Jeong",
        "gender" : "male",
        "age" : 32
    }

print(stu())
'''
'''
def cal(i, j) :
    if i == j :
        return f"결과(곱) : {i*j}"
    else :
        return f"결과(합) : {i+j}"
    
a = cal(2, 2)
b = cal(3, 4)

print(a)
print(b)
'''
'''
def price(i) :
    if i < 20000 :
        return f"상품 가격 : {i+2500:,}원"
    else :
        return f"상품 가격 : {i:,}원"
    
a = price(30000)
b = price(15000)

print(a)
print(b)
'''
def time(num) :
    return [i**2 for i in num]


number = [2, 3, 4, 5]
print(time(number))
    