vending_machine = ["게토레이", "게토레이", "레쓰비", "레쓰비", "생수", "생수", "생수", "이프로"]

while True :
    user = input("사용자를 입력하세요(소비자/주인/종료) : ")
    if user == "소비자" :
        print("소비자 로그인")
        print(f"현재 리스트 : {vending_machine}")
        while True :
            while True :
                bev = input("마시고 싶은 음료수를 적으세요(종료 가능) : ")
                if bev == "종료" :
                    print("선택 종료")
                    break
                elif bev in vending_machine :
                    print(f"{bev}을/를 드리겠습니다.")
                    vending_machine.remove(bev)
                    print(f"남은 음료수 : {vending_machine}")
                else :
                    print("해당 음료 없음, 다른 음료를 적으세요")
                    continue
            break
    elif user == "주인" :
        print("주인 로그인")
        while True :
            do = input("업무 종류(추가/삭제/종료) : ")
            if do == "종료" :
                print("업무 종료")
                break
            elif do == "추가" :
                print(f"현재 리스트 : {vending_machine}")
                add = input("추가할 음료 : " )
                while True :
                    if add == "취소" :
                        print("작업 취소")
                        break
                    else :
                        vending_machine.append(add)
                        print("추가 완료")
                        print(f"변경된 리스트 : {vending_machine}")
                        break
            elif do == "삭제" :
                print(f"현재 리스트 : {vending_machine}")
                rem = input("삭제할 음료 : " )
                if rem in vending_machine :
                    vending_machine.remove(rem)
                    print("삭제 완료")
                    print(f"변경된 리스트 : {vending_machine}")
                    continue
                elif rem == "취소" :
                    print("작업 취소")
                    continue
                else :
                        print("해당 음료는 없습니다.")
            else :
                print("업무를 다시 적으세요")
                continue
        break
    elif user == "종료" :
        print("시스템 종료합니다")
        break
    else :
        print("다시 입력하세요")