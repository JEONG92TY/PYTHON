try :
    x = int(input("숫자를 입력하세요"))
    result = 10/x
except ZeroDivisionError as e :
    print("예외메세지 : " , e)
except ValueError as e :
    print("예외메세지 :" , e)
else :
    print(f"result : {result}")
finally :
    print("프로그램이 종료됩니다.")