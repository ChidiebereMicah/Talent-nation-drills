"""Implementing Polymorphism in parallel with Inheritance

Create:

class Developer(Employee):
    ...
    
class Manager(Employee):
    ...
    
class Designer(Employee):
    ...

Each must override work().

For example:

developer = Developer("Micah")
print(developer.work())

should give:
Micah is writing Python code

Part 2 — The important part
Now create:

def perform_work(employee):
    ...

This function should accept an employee and return the result of that employee's work() method.
The function should work with:

perform_work(Developer("Micah"))
perform_work(Manager("Ada"))
perform_work(Designer("James"))

and also with a plain Employee:

perform_work(Employee("David"))
Part 3 — Put them together

Create:

employees = [
    Employee("David"),
    Developer("Micah"),
    Manager("Ada"),
    Designer("James")
]

Then:

for employee in employees:
    print(perform_work(employee))

should produce:

David is working
Micah is writing Python code
Ada is managing the team
James is designing the interface

Once you've got that working, add a fourth class:

class Robot:
    ...

Robot should not inherit from Employee.
But it should have:

work()

that returns something like:

Robot is processing tasks
"""

#parent class
class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        return f"{self.name} is working"

class Developer(Employee):
    def work(self):
        return f"{self.name} is writing Python code"

class Manager(Employee):
    def work(self):
        return f"{self.name} is managing the team"

class Designer(Employee):
    def work(self):
        return f"{self.name} is designing the interface"

def perform_work(obj):
    return obj.work()

employees = [
    Employee("David"),
    Developer("Micah"),
    Manager("Ada"),
    Designer("James")
]

for employee in employees:
    print(perform_work(employee))

class Robot:
    def work(self):
        return "Robot is processing tasks"

print(perform_work(Robot()))
