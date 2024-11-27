'''
class Car :
    model = ""
    cc = 0

    def info(self) :
        print(f"모델명 : {self.model}, 배기량 : {self.cc} cc")


car1 = Car()
car1.model = "산타페"
car1.cc = 2000

print(f"모델명 : {car1.model}")
print(f"배기량 : {car1.cc}cc")

car1.info()
'''
'''
class Car :
    def __init__(self, model, cc):
        self.model = model
        self.cc = cc

    def __str__(self):
        return f"모델명 : {self.model}, 배기량 : {self.cc}"
    
    def info(self) :
        print(f"모델명 : {self.model}, 배기량 : {self.cc}")
        # print(f"모델명 : {model}, 배기량 : {cc}")

car1 = Car("산타페",2000)
car1.info()
'''
'''
class Dog :
    kind : "진돗개"

    def __init__(self, name):
        self.name = name

dog1 = Dog("포메라이언")
dog2 = Dog("말티즈")

print(dog1.name)
print(dog2.name)
'''
'''
class Exam :
    shared = "공유 변수"

    def __init__(self, name) :
        self.name = name

e1 = Exam("A")
e2 = Exam("B")
Exam.shared ="변경된 공유 변수"
print(e1.shared)
print(e2.shared)
e1.name = "C"
print(e1.name)
print(e2.name)
'''
'''
class Employee :
    serial_num = 1000 # 클래스 변수

    def __init__(self,name):
        Employee.serial_num += 1
        self.id = Employee.serial_num
        self.name = name
    
    def __str__(self):
        return f"사번 : {self.id}, 이름 : {self.name}"

e1 = Employee("정태영")
e2 = Employee("정경은")
print(e1)
print(e2)
employees = [Employee("가"), Employee("나"), Employee("다"), Employee("라")]

for emp in employees :
    print(emp)
'''

class Person :

    def __init__(self):
        self._name = ""
        self._age = 0

    def setname(self, name) :
        self._name = name

    def getname(self) :
        print(self._name)
    
    def setage(self, age) :
        self._age = age
    
    def getage(self) :
        return self._age

p1 = Person()
p1.setname("정태영")
p1.setage(32)
p1.getname()
print(p1.getage())