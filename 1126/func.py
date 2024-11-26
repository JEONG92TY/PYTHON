'''
quan = 10

def get_price(price) :
    price = price * quan
    return price

print(f"{quan}개의 가격은 {get_price(5000): ,}입니다.")

def oneUp() :
    x =0
    x += 1
    return(x)

print(oneUp())

quan = 10

def price_sum(price) :
    quan = 7
    return price * quan

print(price_sum(2000))
'''
'''
def square(x) :
    return x**3

number = [1, 2, 3, 4]
squared = list(map(square, number))
print(squared)
'''
'''
def even_number(x) :
    return x % 2 == 0

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(even_number, number)))
'''
'''
x = int(input("숫자 : "))

def count(x) :
    total = 0
    list = []

    for i in range(1, 31) :
        if i % x == 0 :
            list.append(i)
            total += 1
    print(list)
    return total

print(f"{x}의 배수 개수 : {count(x)}")
'''
'''
def sos(i) :
    print("살려줘", i)
    if i == 1 :
        return ""
    else :
        return sos(i-1)
sos(5)
'''
'''
def factorial(n) :
    if n == 1 :
        return 1
    else :
        return n*factorial(n-1)
print(factorial(3))
'''
'''
def fibo(x) :
    if x < 2 :
        return x
    else :
        return fibo(x-1) + fibo(x-2)

x = int(input("몇번째 숫자를 확인하시겠습니까? : "))
print(f"{x}번째 숫자는 {fibo(x)}")
'''
'''
oneup = lambda x : x + 1
print(oneup(1))
print((oneup)(1))
print((lambda x : x+1)(1))
'''
'''
square = lambda x : x**2
print(square(4))

plus = lambda x, y : x+y
print(plus(1,2))
'''
'''
def call(func) :
    for i in range(10) :
        func()
def hello() :
    print("안녕하세요")
hello2 = lambda : print("반갑습니다")
call(hello)
call(hello2)
'''
num = [1,2,3,4,5]
square = map(lambda x : x**3, num)
print(list(square))
even = filter(lambda x : x%2==0, num)
print(list(even))