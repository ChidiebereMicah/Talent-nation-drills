class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    @property
    def balance(self): 
        #@property allows us to create a method by which we can access a class attribute while restricting external access to that attribute
        return self._balance

    @balance.setter
    def balance(self, amount):
        #@<attrbt>.setter allows us to control how a class attribute is modified outside of the class
        if amount < 0:
            raise ValueError("Balance must not be negative")

        self._balance = amount

account = BankAccount(500)
print(account.balance)