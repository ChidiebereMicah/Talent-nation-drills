#Using single and double underscore to determine the scope of an attribute

"""single underscore is only used as a convention to signal that the attrbt is to be used only inside the class"""
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

account = BankAccount(500)
print(account._balance)#this still works even when attrbt is accessed outside of class

"""double underscore is  used to enforce  the use of an attrbt only inside the class"""
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_attrbt(self, ):
        return self.__balance
    
account = BankAccount(500)
print(account.get_attrbt())#this works cos attrbt is accessed by member menthod

try:
    print(account.__balance)#this doesn't work cos attrbt is accessed outside of class
except AttributeError as error:
    print(f"You attemted to access a dedicated class attrbt from outside the class\n {error}")
