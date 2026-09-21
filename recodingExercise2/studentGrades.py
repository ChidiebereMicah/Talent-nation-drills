def grader(grade):
    if grade >= 70:
        return "A"
    elif grade >= 60:
        return "B"
    elif grade >= 50:
        return "C"  
    elif grade >= 45:
        return "D"
    elif grade >= 40:
        return "E"
    else:
        return "F"  
    
students = [
    ["Samuel", 80, 75, 90],
    ["David", 55, 60, 50],
    ["Mary", 35, 40, 30],
    ["John", 65, 70, 68]
]

def average(student):
    student = student[1:]
    average = round(sum(student)/len(student), 2)
    # total = 0
    # for score in student:
    #     total += score
    # average = round(total/len(student), 2)
    return average

for student in students:
    avg = average(student)
    grade = grader(avg)
    print(f"{student[0]} - Average: {avg} - Grade: {grade}")