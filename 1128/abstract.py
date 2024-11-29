from abc import ABC, abstractmethod

class PaymentSystem(ABC) :
     
     @abstractmethod
     def authenticate(self) :
         pass
     #추상메서드 = 구현 X

     @abstractmethod
     def process_payment(self, amount) :
         pass
     
     def payment_info(self, amount) :
         print(f"{amount}원 결제가 완료되었습니다")

class Kakaopay(PaymentSystem) :

    def authenticate(self):
        print("인증 완료되었습니다.")

    def process_payment(self, amount):
        print(f"{amount}원을 걸제합니다.")

kakao = Kakaopay()
kakao.authenticate()
kakao.process_payment("50,000")
kakao.payment_info("50,000")