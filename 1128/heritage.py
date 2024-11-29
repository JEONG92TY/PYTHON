'''
class Animal :
    def speak(self) :
        print("동물이 소리를 냅니다.")

    def move(self) :
        print("동물이 움직입니다.")

class Cat(Animal) :
    def meow(self) :
        print("야옹")

cat = Cat()
cat.speak()
cat.move()
cat.meow()
'''
'''
class Animal :
    def __init__(self,name):
        self.name = name
    
    def speak(self) :
        print(f"{self.name}이 소리를 냅니다.")
        
    def move(self) :
        print(f"{self.name}이 움직입니다.")

class Cat(Animal) :
    def __init__(self, name, sound):
        super().__init__(name) #name이 입력된 것이 아니라 부모클래스에서 호출한다는 뜻
        self.sound = sound

    def meow(self) :
        print(f"{self.name} 가 {self.sound} 하고 웁니다.")

cat = Cat("정태영", "야옹")
cat.speak()
cat.move()
cat.meow()
'''

class Engine :
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Wheel :
    def __init__(self, count):
        self.count = count

class Car(Engine, Wheel) :
    def __init__(self, horsepower, count):
        Engine.__init__(self, horsepower)
        Wheel.__init__(self, count)

    def info(self) :
        print(f"이 자동차는 {self.horsepower} 마력과 {self.count}개의 바퀴를 가지고 있다.")

car = Car(100,4)
car.info()
print(Car.mro())

'''
class Parent :
    def greet(self) :
        print("부모클래스")

class Child(Parent) :
    def greet(self) :
        super().greet() # Parent 클래스 그대로 가져옴
        #print("자식클래스") # Parent 클래스의 함수를 가져와서 수정하는 것 : 오버라이딩

p = Parent()
c = Child()
p.greet()
c.greet()
'''