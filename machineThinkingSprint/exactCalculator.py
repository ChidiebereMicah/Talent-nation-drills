"""
ExactCalculator
Instructions

Implement exact_calculator(left, operator, right). 
Convert left and right to numbers. Support addition, 
subtraction, multiplication, division, remainder, and exponent. 
If either number cannot be converted, return Invalid number. 
If the operator is not supported, return Invalid operator. 
If division or remainder uses zero on the right side, return Cannot divide by zero. 
Round numeric results to 2 decimal places.
"""

def exact_calculator(left, operator, right):
    try:
        left = float(left)
        right = float(right)
    except ValueError:
        return "Invalid number"

    if operator not in ["+","-","*","/","%","**"]:
        return "Invalid operator"

    if operator in ["/","%"] and right==0:
        return "Cannot divide by zero"
    
    result = eval(f"{left}{operator}{right}")

    return round(result, 2)


#Using direct operator logic
def exact_calculator(left, operator, right):
    try:
        left = float(left)
        right = float(right)
    except ValueError:
        return "Invalid number"

    if operator not in ["+","-","*","/","%","**"]:
        return "Invalid operator"

    if operator in ["/","%"] and right==0:
        return "Cannot divide by zero"
    
    if operator == "+":
        return round(left + right, 2)
    if operator == "-":
        return round(left - right, 2)
    if operator == "*":
        return round(left * right, 2)
    if operator == "/":
        return round(left / right, 2)
    if operator == "%":
        return round(left % right, 2)
    if operator == "**":
        return round(left ** right, 2)


        
