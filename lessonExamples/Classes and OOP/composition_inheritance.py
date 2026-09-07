class Engine:
    def start(self):
        return "Petrol engine started"

class ElectricEngine:
    def start(self):
        return "Electric engine started"

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        return self.engine.start()

car1 = Car(Engine())
car2 = Car(ElectricEngine())

print(car1.start())
print(car2.start())