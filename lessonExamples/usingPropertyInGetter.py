class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self): #@propertyallows us to name the getter method with same name as the attribt
        return self._balance

account = BankAccount(500)
print(account.balance)