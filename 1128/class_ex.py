from abc import ABC, abstractmethod

electiricity_usage = [
    {"date" : "2024-11-01", "usage" : 12.5},
    {"date" : "2024-11-02", "usage" : 15.3},
    {"date" : "2024-11-03", "usage" : 10.8},
    {"date" : "2024-11-04", "usage" : 14.2},
    {"date" : "2024-11-05", "usage" : 13.6}
]

#부모클래스 생성 - 추상클래스
class ElectricityData(ABC) :

    #===========================================================
    #데이터, 총사용량 초기화
    def __init__(self, usage_data=0, total_usage=0) :
        self.usage_data = usage_data
        self.total_usage = total_usage
    #데이터 캡슐화
    def setdata(self, usage_data) :
        self.usage_data = usage_data
    def getdata(self) :
        return self.usage_data   
    #총사용량 캡슐화
    def settotal(self, total_usage) :
        self.total_usage = total_usage
    def gettotal(self) :
        return self.total_usage
    #===========================================================
    #추상메서드 - 총사용량 계산
    @abstractmethod
    def calculate_total_usage(self) :
        pass
    #추상메서드 - 특정 날짜 전력량 반환
    @abstractmethod
    def get_usage_on_data(self, date) :
        pass
    #일반메서드 - 새로운 날짜의 전력 사용량 추가
    def add_usage(self, date, usage) :
        self.date = date
        self.usage = usage
        self.total_usage = 0
        electiricity_usage.append({"date" : self.date, "usage" : self.usage})
        for i in electiricity_usage:
            self.total_usage += i.get("usage")
        print(f"{self.date} 추가 후 총 전력 사용량 : {self.total_usage}")
        #for i in electiricity_usage : #>>>>> 제대로 추가되는지 확인하는 코드입니다.
        #    print(i)
    #일반메서드 - 특정 날짜의 전력 사용량 데이터를 삭제
    def remove_usage(self, date) :
        self.date = date
        self.total_usage = 0
        for i in electiricity_usage:
            if i.get("date") == self.date :
                electiricity_usage.remove(i)
        for i in electiricity_usage:
            self.total_usage += i.get("usage")
        print(f"{self.date} 삭제 후 총 전력 사용량 : {self.total_usage}")
        #for i in electiricity_usage : #>>>>> 제대로 삭제되는지 확인하는 코드입니다.
        #    print(i)
    #===========================================================

#자식클래스 생성
class HomeElectricityData(ElectricityData) :
    #추상메서드 - 총사용량 계산 구현
    def calculate_total_usage(self) :
        for i in electiricity_usage:
            self.total_usage += i.get("usage")
        print(f"총 전력 사용량 : {self.total_usage:.1f}")
    #추상메서드 - 특정 날짜 전력량 반환 구현
    def get_usage_on_data(self, date) :
        for i in electiricity_usage:
            if i.get("date") == date :
                print(f"{date}의 사용량 : {i.get("usage")}")
    #클래스메서드 - 특정 날짜 범위 데이터 필터링 기능
    @classmethod
    def filter(cls, start_date, end_date) :
        period = []
        for i in electiricity_usage:
            if i.get("date") >= start_date and i.get("date") <= end_date :
                period.append(i)
        return f"특정 날짜 범위 내 사용량 : {period}"

    #정적메서드 - 가장 높은 전력 사용량 출력 기능
    @staticmethod
    def high() :
        usage = 0
        for i in electiricity_usage:
            if i.get("usage") > usage :
                usage = i.get("usage")
            else :
                usage = usage
        for j in electiricity_usage:
            if j.get("usage") == usage :
                print(f"가장 높은 사용량 : {j}")


#구현내용

p = HomeElectricityData(0,0)

p.calculate_total_usage()
p.get_usage_on_data("2024-11-03")
p.add_usage("2024-11-06", 16.2)
p.remove_usage("2024-11-05")
#클래스메서드를 통해 객체 생성
f = HomeElectricityData.filter("2024-11-03", "2024-11-04")
print(f)
#클래스메서드를 통해 객체 생성
p.high()