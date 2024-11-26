weather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-22", "서울", 8.3, 0.0],
    ["2024-11-22", "부산", 12.0, 0.0]
    ]

def city_list() :
    list = []
    for i in range (len(weather_data)) :
        init = weather_data[i][1]
        list.append(init)
        i =+ 1
    return list


def ave_tem(city) :
    if city in city_list() :
        list = []
        for i in range(len(weather_data)) :
            if weather_data[i][1] == city :
                list.append(weather_data[i][2])
                i += 1
            else :
                i += 1       
        print(f"{city}의 평균 온도는 {sum(list)/len(list):.2f}°C 입니다.")
        print("")
    else :
        print("없는 도시입니다.")
        print("")

def tem_mm(city) :
    if city in city_list() :
        list = []
        for i in range(len(weather_data)) :
            if weather_data[i][1] == city :
                list.append(weather_data[i][2])
                i += 1
            else :
                i += 1       
        print(f"{city}의 최고 기온 : {max(list)}°C, 최저 기온 : {min(list)}°C")
        print("")
    else :
        print("없는 도시입니다.")
        print("")

def rainfall(city) :
    if city in city_list() :
        list1 = []
        for i in range(len(weather_data)) :
            if weather_data[i][1] == city :
                list1.append(weather_data[i][3])
                i += 1
            else :
                i += 1
        day = list(filter(lambda x : x > 0, list1))
        print(f"{city}의 총 강수량 : {sum(list1)}mm")
        print(f"{city}의 강수량이 있었던 날 : {len(day)}")
        print("")
    else :
        print("없는 도시입니다.")
        print("")

def add() :
    d = input("날짜를 입력하세요 (YYYY-MM-DD) : ")
    c = input("도시를 입력하세요 : ")
    t = float(input("평균 기온을 입력하세요 (°C) : "))
    r = float(input("강수량을 입력하세요 (mm) : "))
    new = [d, c, t, r]
    weather_data.append(new)
    print(f"{c}의 날씨 데이터가 추가되었습니다.")
    print("")

def data_list() :
    i = 0
    for i in range(0, len(weather_data)) :
        print(f"날짜 : {weather_data[i][0]}, 도시 : {weather_data[i][1]}, 기온 : {weather_data[i][2]}, 강수량 : {weather_data[i][3]}")
        i += 1
    print("")

print("\n"
      "\n"
      "[날씨 데이터 분석 프로그램]""\n"
      "1. 평균 기온 계산""\n"
      "2. 최고/최저 기온 찾기""\n"
      "3. 강수량 분석""\n"
      "4. 날씨 데이터 추가""\n"
      "5. 전체 데이터 출력""\n"
      "6. 종료 --- 정태영 ""\n"
      "\n"
      "")

'''
weather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-22", "서울", 8.3, 0.0],
    ["2024-11-22", "부산", 12.0, 0.0]
    ]
'''

while True :
    num = input("원하는 기능의 번호를 입력하세요 : ")
    if num == "1" :
        print("")
        city = input("도시 이름을 입력하세요 : ")
        ave_tem(city)
    elif num == "2" :
        print("")
        city = input("도시 이름을 입력하세요 : ")
        tem_mm(city)
    elif num == "3" :
        print("")
        city = input("도시 이름을 입력하세요 : ")
        rainfall(city)
    elif num == "4" :
        print("")
        add()
    elif num == "5" :
        print("")
        data_list()
    elif num == "6" :
        print("종료합니다.")
        break
    else :
        print("잘못된 번호입니다.")
        print("")