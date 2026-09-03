"""
Implementing inheritance using the Employee class
"""

class Employee:
    company = "Talent Nation"

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def give_raise(self, amount):
        self.salary += amount

class Manager(Employee):
    def __init__(self, name, salary, department, team_size):
        super().__init__(name, salary, department)
        self.team_size = team_size

    def give_raise(self, amount):
        super().give_raise(amount) #copying the parent behavior
        self.salary *= 2 #extending the behavior in the child method
    
    def manage_team(self):
        return f"{self.name} is managing {self.team_size} people"
        
employee = Employee("Ada", 10000, "AI")
manager = Manager("Micah", 10000, "AI", 8)

print(isinstance(employee, Employee))
print(isinstance(manager, Employee))
print(isinstance(manager, Manager))
print(employee.company)
print(manager.company)

employee.give_raise(5000)
print(employee.salary)
manager.give_raise(5000)
print(manager.salary)