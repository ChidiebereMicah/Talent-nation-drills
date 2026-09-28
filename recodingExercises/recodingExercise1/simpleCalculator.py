def simple_calculator(num1, num2, operator):

    if operator == '+':
        return float(num1) + float(num2)
    elif operator == '-':
        return float(num1) - float(num2)
    elif operator == '*':
            return float(num1) * float(num2)
    elif operator == '/':
            try:
                  return float(num1)/float(num2)
            except ZeroDivisionError:
                  return "Cannot divide by zero"
    else:
          return "Invalid operator"

num1 = input("Enter 1st number: ")
num2 = input("Enter 2nd number: ")
operator = input("Enter operator(+, -, *, or /): ")

print(round(simple_calculator(num1, num2, operator), 3))

