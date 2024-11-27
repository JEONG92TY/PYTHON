'''
class Calc :   

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self) :
        print(self.num1 + self.num2)

    def sub(self) :
        print(self.num1 - self.num2)

    def mul(self) :
        print(self.num1 * self.num2)
    
    def div(self) :
        if self.num2 <= 0:
            print("분모 오류")
        else :
            print(self.num1 / self.num2)    

calc1 = Calc(3, -2)
calc1.add()
calc1.sub()
calc1.mul()
calc1.div()
'''
'''
class Mar :

    def __init__(self, location, name, product, customer):
        self.location = location
        self.name = name
        self.product = product
        self.customer = customer

    def print_location(self) :
        print(f"위치 : {self.location}")

    def change_category(self, new_product) :
        self.product = new_product
    
    def show_list(self) :
        print(f"상품 : {self.product}")

    def enter_customer(self) :
        self.customer += 1

    def show_info(self) :
        print(f"위치 : {self.location}, 이름 : {self.name}, 상품 : {self.product}, 고객수 : {self.customer}")
        
a = Mar("고양시 원흥동", "엽기떡볶이", "마라엽떡", 1)
a.print_location()
a.show_list()
a.show_info()

print("")
a.enter_customer()
a.enter_customer()
a.enter_customer()
print("")

a.change_category("엽기닭도리탕")
a.show_list()
a.show_info()
'''

class Health :

    def __init__(self):
        self._name = ""
        self._drink = 0
        self._exercise = 0
        self._hp = 0

    def setinfo(self, name, exercise, drink, hp) :
        self._name = name
        self._exercise = exercise
        self._drink = drink
        self._hp = hp

    def getinfo(self) :
        print(f"운동 : {self._exercise} 시간")
        print(f"음주 : {self._drink} 잔")
        print(f"{self._name}의 HP : {self._hp - self._drink + self._exercise}")

a1 = Health()
a1.setinfo("정태영", 5, 2, 30)
a1.getinfo()