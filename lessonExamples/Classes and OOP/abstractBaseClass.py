from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    def __init__(self, method):
        self.method = method

    @abstractmethod
    def pay(self):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        return f"{self.method} of {amount} processed"

class PayPal(PaymentMethod):
    def pay(self, amount):
        return f"{self.method} of {amount} processed"

class BankTransfer(PaymentMethod):
    def pay(self, amount):
        return f"{self.method} of {amount} processed"

def process_payment(method, amount):
    return method.pay(amount)

methods = [
    CreditCard("Credit card"),
    PayPal("PayPal"),
    BankTransfer("Bank transfer")
]

for method in methods:
    print(process_payment(method, 500))

class CryptoPayment(PaymentMethod):
    pass

crypto = CryptoPayment("Crypto payment")