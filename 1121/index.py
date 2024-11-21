from sys import getsizeof
'''
print(getsizeof(1))
print(getsizeof("1"))

print(type(1111))
print(type(11.11))
print(type("정태영"))
print(type(True))
print(type(None))

#형변환
num = int(input("숫자를 입력하세요"))
a = num%2 == 0
print(num,"=",a)

print(int(5.5))
print(int("30"))

#문자열 연산
print("안녕" + "하세요")
a = "하"
print("안녕"+a+"세요")
print("와"*3)

song = """
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산
대한사랑 대한으로 길이 보전하세
"""
print(song)

print('"오늘저녁뭐먹지?"')
print("'굶는다'")

number = "저는 올해 %d 살 입니다." %33.123
print(number)
calc = "20 나누기 3은 %.3f" %6.67
print(calc)
text = "저는 %s에 살고 있습니다." %"원흥"
print(text)
char = "이모티콘은 %c 이것으로 하겠습니다." %

print("국가명를 적으세요")
country = input("")
print("도시명을 적으세요")
city = input("")
print("이름을 적으세요")
people = input("")

text = "저는 {0}, {1}에 살고있는 {2} 입니다.".format(country, city, people)
print(text)

a = "[{0:>10}]".format("HEY")
print(a)

print("|\_/|")
print("|q p|   /}")
print("( 0 )"+'"""'+"\\")
print('|"^"`    |')
print("||_/=\\__|")

name = "정태영"
text = f"{name:@^10}"
print(text)

mid = "{중괄호}"
text1 = '문자열 실습입니다. {0}를 출력해보세요'.format(mid)
print(text1)
print(f'문자열 실습입니다. {mid}를 출력해보세요')

a = "Hello, Python"
print(a[7:13])

a = "abcabcabc"
first_a = a.find("a")
print(first_a)
second_a = a.find("a",first_a+1)
print(second_a)
third_a = a.find("a",second_a+1)
print(third_a)

a = "12.34"
print(a.isdecimal())
print(a.isdigit())
print(a.isnumeric())
'''

print("이름을 입력하세요")
a = input()
print("나이을 입력하세요")
b = input()
text = ("안녕하세요! {0}님 ({1}살)").format(a,b)
print(text)

print("이름을 입력하세요")
a = input()
print("태어난 년도를 입력하세요")
b = input()
print("올해 년도를 입력하세요")
c = input()
d = int(c)-int(b)
text1 = ("올해는 {0}년, {1}님의 나이는 {2}세 입니다.").format(c,a,d)
print(text1)