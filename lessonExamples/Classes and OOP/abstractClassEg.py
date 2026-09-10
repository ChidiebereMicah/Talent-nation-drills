from abc import ABC, abstractmethod

class StipendAcct(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def BVN(self):
        pass

    @abstractmethod
    def NIN(self):
        pass

class NJFP(StipendAcct):
    def BVN(self):
        return input("Please enter your BVN")

    def NIN(self):
            return input("Please enter your NIN")

    def NYSC(self):
        return input("Please enter your NYSC number")

fellow1 = NJFP("Chijioke Okpala")
print(fellow1.NIN())