"""
ScoreSummary
Instructions

Implement score_summary(name, a, b, c). 
Convert the three score values to numbers. 
If conversion fails, return Invalid score. 
If any score is below 0 or above 100, return Invalid score. 
Otherwise calculate the average, round it to 2 decimal places, 
choose a grade, and return a three-line report with labels Student, Average, and Grade. 
Grade is A for 90 and above, B for 80 and above, C for 70 and above, and F below 70.
"""

def score_summary(name, a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except (ValueError, TypeError): #type error catches when None is passed as a variable
        return "Invalid score"
    
    if not all(0 <= score <= 100 for score in (a, b, c)):
        return "Invalid score"

    average = round((a+b+c)/3, 2)
    return f"Student: {name}\nAverage: {average}\nGrade: {grade_label(average)}"

def grade_label(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

print(score_summary("Ada","80","90","85"))


