def simpleCalc(num1, num2, operator):
    num1 = float(num1)
    num2 = float(num2)
    if operator == "*":
        return num1 * num2
    elif operator == "-":
        return num1 - num2
    elif operator == "+":
        return num1 - num2
    elif operator == "/":
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operator"

num1 = input("Please enter your first number: ")
num2 = input("Please enter your second number: ")
operator = input("Please enter your operator: ")
print(simpleCalc(num1, num2, operator))

