"""FixSafeDivide
Instructions
Implement safe_divide(a, b). 
Return a divided by b rounded to 2 decimal places. 
If b is zero, return Cannot divide by zero. 
This fixes the common ZeroDivisionError bug.
"""
#Solution
def safe_divide(a, b):
    # Bug to fix: dividing by zero crashes the program.
    try:
        return round(a/b,2)
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(safe_divide(23,0))
