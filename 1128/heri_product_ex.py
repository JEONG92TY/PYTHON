class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # 재고 업데이트 메서드
    def update_quantity(self, amount):
        self.quantity += amount
        print(f"{self.name} 재고가 {amount}만큼 {'증가' if amount > 0 else '감소'}했습니다. 현재 재고: {self.quantity}")

    # 상품 정보 출력 메서드
    def display_info(self):
        print(f"상품명: {self.name}")
        print(f"가격: {self.price}원")
        print(f"재고: {self.quantity}개")

class Electronic(Product) :

    def display_info(self, warranty_period=12) :
        self.warranty_period = warranty_period
        super().display_info()
        print(f"보증기간 : {self.warranty_period}개월")
    
    def extend_period(self, month) :
        self.month = month
        print(f"기간이 {self.month}개월 연장되었습니다. 현재 보증 기간 : {self.warranty_period + self.month}개월")

class Food(Product) :

    def display_info(self, expiration_date) :
        self.expiration_date = expiration_date
        super().display_info()
        print(f"유통기간 : {self.expiration_date}")
    
    def is_expired(self, current_date) :
        self.current_date = current_date
        if self.current_date > self.expiration_date :
            print(f"{self.name}의 유통기한이 지났습니다.")
        else :
            print(f"{self.name}의 유통기한이 지나지 않았습니다.")

c1 = Electronic("스마트TV", 150000, 5)
c2 = Food("사과", 3000, 50)

c1.display_info(24)
c1.extend_period(12)

print("")

c2.display_info("2024-11-28")
c2.is_expired("2024-11-30")
c2.is_expired("2024-11-26")