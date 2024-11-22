'''
i = 0
while i < 3 :
    print("반복문", i)
    i += 1
print("끝")
'''
'''
num = 1
total =0
while num <= 10 :
    total += num
    num += 1
print(total)
'''
'''
user_input = ""

while user_input != "종료" :
    user_input = input("원하는 값을 입력하세요. 종료하려면 '종료'를 입력하세요 : ")
    print(f"입력한 값은 {user_input} 입니다.")
print("종료합니다")
'''
'''
while True :
    dinner = input("오늘 저녁 메뉴는 : ")
    if dinner == "제육" :
        print(f"오늘 저녁 메뉴는 {dinner}입니다")
        break
    print(f"오늘 저녁 메뉴는 {dinner}입니다")
print("메뉴 선정 완료")
'''
'''
count = 0
while count < 10 :
    count += 1
    if count % 2 == 0 :
        continue
    print(count, end=" ")
'''

while True :

    num = input("양수를 입력하세요. ('종료' 입력 시 프로그램 종료) : ")
    i = 1
    total = 0

    if num == "종료" :
        print("프로그램을 종료합니다.")
        break
    
    if not num.isdigit() :
### isdigit() => 음수 false, 0, 양수, 문자열 True
### if int(num) <= 0 : => 이렇게 하면 "종료" 이외의 문자열에서 버그
        print("양수만 입력하세요")
        continue

### 아래 코드 왜 적용 안되는지 확인해야 한다.
    if num == "0" :
        continue

    while i <= int(num) :
        total += i
        i += 1
    print(f"1부터 {num}까지의 합은 {total}입니다.")


