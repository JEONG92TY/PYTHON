'''
print("안녕하세요")
print("Hello", "PYTHON")
print("Hello", "PYTHON", sep="~ ")
print("안녕하세요", end="!! ")
print("저는 정태영입니다.")
print(1111)

singer = input("좋아하는 가수는?")
print("좋아하는 가수는",singer,"입니다")
'''

# 한줄 주석 사용, 코드 뒤에서 붙일 수 있다.

'''
x=10
y,z = 3.5, "안녕"
print("x = ",x,"y = ",y,"before z =",z, id(z))
z = "잘가"
print("x = ",x,"y = ",y,"after z =",z, id(z))

a = [1,2,3]
print("before a = ",a,  id(a))
a.append(4)
print("after a =",a, id(a))

import keyword
print(keyword.kwlist)

x= 48 / 2 *(9+3)
print(x)

num = 5
print(num)
num += 5
print(num)
num -= 2
print(num)
num *= 6
print(num)
num /= 2
print(num)
num //= 3
print(num)
num %= 5
print(num)
num **= 3
print(num)

num1 = 10
num2 = 20
num3 = "10"

print( num1 < num2 )
print( num1 > num2 )
print( num1 == num3)
print( num1 != num3)
print( num1 >= 9)
print( num2 <= 30)

a = 3 > 1
b = 2 < 1
c = 1 > 0
print(a or b)

'''

x = 3
a = x%2
print(a)
print("True면 짝수, False면 홀수 : ", a == 0 )