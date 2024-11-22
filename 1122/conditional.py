'''
num = input("비밀번호를 입력하세요. : ")
if num == "abc123" :
    print("비밀번호가 맞습니다.")
else :
    print("비밀번호가 틀렸습니다.")

print()

num1 = int(input("숫자를 입력하세요. : "))
a = num1 % 2
if a == 0 :
    print("짝수입니다.")
else :
    print("홀수입니다.")
#
score = int(input("점수를 입력하세요 : "))
if score >= 90 :
    print("학점 = A")
elif score >= 80 :
    print("학점 = B")
elif score >= 70 :
    print("학점 = C")
elif score >= 60 :
    print("학점 = D")
else :
    print("학점 = F")

age = int(input("나이를 숫자로 입력해주세요 : "))
pay = input("결제방법을 입력해주세요 (현금 또는 카드) : ")
if pay == "현금" :
    if age >= 75 :
        price = "무료"
       # print(age,"세의 현금 요금은 무료입니다")
    elif age >= 20 :
        price = "1,300원"
       # print(age,"세의 현금 요금은 1,300원입니다")
    elif age >= 14 :
        price = "1,000원"
       # print(age,"세의 현금 요금은 1,000원입니다")
    elif age >= 8 :
        price = "450원"
       # print(age,"세의 현금 요금은 450원입니다")
    elif age >= 0 :
        price = "무료"
       # print(age,"세의 현금 요금은 무료입니다")
    else :
        price = None
elif pay == "카드" :
    if age >= 75 :
        price = "무료"
       # print(age,"세의 현금 요금은 무료입니다")
    elif age >= 20 :
        price = "1,200원"
       # print(age,"세의 현금 요금은 1,200원입니다")
    elif age >= 14 :
        price = "720원"
       # print(age,"세의 현금 요금은 720원입니다")
    elif age >= 8 :
        price = "450원"
       # print(age,"세의 현금 요금은 450원입니다")
    elif age >= 0:
        price = "무료"
       # print(age,"세의 현금 요금은 무료입니다")
    else :
        price = None

if pay != "현금" and pay != "카드" :
    print("결제 수단을 정확히 기입하세요")

if price :
    print(f"{age}세의 {pay} 가격은 {price} 입니다.")
else :
    print("나이를 정확히 기입하세요")

fruit = input("과일을 입력하세요 : ")

if fruit in ["사과", "바나나", "포도", "복숭아"] :
    print(f"{fruit}은(는) 과일에 포함되어 있습니다.")
else :
    print(f"{fruit}은(는) 과일에 포함되어 있지 않습니다.")
'''

dic = {
    "apple" : 95,
    "banana" : 105,
    "cherry" : 50
}

fru = input("과일을 영문으로 입력하세요. ; ")
if fru in dic :
    cal = dic.get(fru)
    print(f"{fru}의 칼로리는 {dic.get(fru)}Kcal 입니다.")
else :
    print("존재하지 않는 과일입니다.")
