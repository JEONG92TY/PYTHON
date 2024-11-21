'''
number = [1, 2, 3, "Hello", "Python"]
print(number[3])

text = "Hello, Python"
text = list(text)
print(text)

shop = ["의류", "식품", "가전", ["모니터", "마우스"]]
print(shop[:3])
shop[0] = "남성의류"
print(shop)
del shop[3]
print(shop)

a = [1, 2, 3]
b = ["안녕", "하세요"]
print(a+b)
print(b*3)

num = [1, 3, 5, 2, 4]
num_asc = sorted(num)
num_dsc = sorted(num, reverse=True)
print(num_asc)
print(num_dsc)
print(num)
num.sort()
print(num)

korean = ["김", "나", "박", "이"]
korean.sort(reverse=True)
print(korean)

alphabet = ["v", "d", "n", "u"]
alphabet.reverse()
print(alphabet)
print(alphabet.index("v"))

list = [1, 2, 3, 4, 5]
list.append(6)
print(list)
list.pop()
print(list)
list.pop(2)
print(list)
list.insert(2,0)
print(list)
print(list.count("0"))
list.clear()
print(list)

rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "purlpe"]
print(rainbow[2])
rainbow.sort()
print(rainbow)
rainbow.append("black")
print(rainbow)
del rainbow[3:7]
print(rainbow)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[2][0])

matrix [1] = matrix[1] + [99]
print(matrix)
matrix  = matrix + [[10, 11, 12]] # 2개 써야함
print(matrix)
matrix[0][0] = 100
print(matrix)
del matrix[1][3]
print(matrix)
del matrix[0]
print(matrix)
print(len(matrix))
print(len(matrix[0]))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[0].append([10])
matrix.append([10, 11, 12])
matrix[1].insert(3, 100)
matrix.insert(0,[13, 14, 15])
matrix[0].extend([16, 17])
print(matrix)

t1 = (1,)
t2 = (1, 2, 2, 3, 3, 3, 4,5)
t3 = 1, 2, 3
t4 = ([1, 2], [3, 4], [5, 6])
print(t1[0])
print(t2.count(3))
print(t3.index(2))
print(t4[1][1])
print(len(t4))
print(len(t4[0]))
print([5, 6] in t4)

s1 = {1, 2, 2, 3, 3, 3, 4, 4, 4 ,4}
print(s1)
s2 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(s2)
print(set(s2))
'''