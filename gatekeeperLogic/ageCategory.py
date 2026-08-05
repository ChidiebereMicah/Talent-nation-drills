"""
AgeCategory
Instructions

Implement age_category(age). 
Return Child if age is less than 13, Teenager if age is less than 18, 
Adult if age is less than 65, and Senior otherwise. 
Use if, elif, and else.
"""

def age_category(age):
    if age < 13:
        return "Child"
    elif age < 18:
        return "Teenager"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"
