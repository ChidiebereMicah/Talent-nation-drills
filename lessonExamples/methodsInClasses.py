class Employee:
    company = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

    @classmethod
    def change_company(cls, self, new_company):
        cls.company = new_company
        self.company = "the company"
        return [cls.company, self.company]

    @staticmethod
    def valid_salary(salary):
        return salary >= 0

employee = Employee("Ada", 5000)

employee.give_raise(500)
print(Employee.change_company(Employee.change_company, "AI Corp"))
print(Employee.valid_salary(7000))