from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print("Paid", amount, "using credit card")

class UPI(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")

payment1 = CreditCard()
payment2 = UPI()

payment1.pay(5000)
payment2.pay(2000)
