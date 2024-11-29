from datetime import datetime
import time

words = [
    "mountain", "river", "forest",
    "ocean", "desert", "tree",
    "flower", "cloud", "rain",
    "sunlight"
    ]

print("게임 시작 2초전")
time.sleep(1)
print("게임 시작 1초전")
time.sleep(1)
print("게임 시작")
print("")
start_time = datetime.now()

w = 0

while True :
    #for i in range(1000000) :
    while w < len(words) :
        print(f"단어 : {words[w]}")
        typing = input("입력 : ")
        if typing == words[w] :
            print("통과!")
            print("")
            w < len(words)-1
            w += 1
        else :
            print("오답! 다시 시도하세요.")
            w == w
    break

print("게임 종료")
time.sleep(1)

end_time = datetime.now()
taken_time = end_time - start_time

print("")
print(f"총 걸린 시간 : {taken_time}초")
print(f"타자 속도 : 단어 당 {taken_time/len(words)}초")
