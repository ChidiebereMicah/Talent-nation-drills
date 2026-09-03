class Employee():
    company = "Talent Nation"

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")

        self._salary = value

    @property
    def annual_salary(self):
        return self.salary * 12

    def give_raise(self, amount):
        self.salary += amount

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    @staticmethod
    def valid_salary(salary):
        return True if salary >= 0 else False

    @classmethod
    def from_string(cls, text):
        text = text.split(",")
        return cls(text[0], float(text[1]), text[2])

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        if value == "":
            raise ValueError("Department field cannot be empty")

        self._department = value

a = Employee("Ada", 10000, "AI")
b = Employee("Micah", 15000, "Data")

print(a.company)
print(b.company)

print(a.salary)
a.give_raise(2000)
print(a.salary)

print(a.annual_salary)

print(Employee.valid_salary(5000))
print(Employee.valid_salary(-100))

Employee.change_company("OpenAI")

print(a.company)
print(b.company)

c = Employee.from_string("James,20000,Web")

print(c.name)
print(c.salary)
print(c.department)

value = ""
print()