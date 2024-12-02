'''
# "w"는 파일이 없으면 만들고, 있으면 덮어씌움
with open("test_txt", "w", encoding="utf-8") as file :
    file.write("안녕하세요\n")
    file.write("파이썬쓰기연습\n")

# "a"는 기존 파일에 내용 추가하는 기능
with open("test_txt", "a", encoding="utf-8") as file :
    file.write("내용 추가\n")
    file.write("1111") #문자열이 아닌 경우 추가가 안된다
'''
'''
with open("user_txt", "a", encoding="utf-8") as file :
    while True :
        line = input("파일에 넣을 문자열 입력(종료하려면 ""종료"" 입력) : ")
        if line == "종료" :
            print("입력을 종료합니다.")
            break
        file.write(line + "\n")
print("사용자 입력이 파일에 저장되었습니다.")
'''
'''
with open("user_txt", "r", encoding="utf-8") as file :
    print(file.read())

with open("user_txt", "r", encoding="utf-8") as file :
    print(file.readlines())
'''