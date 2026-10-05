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

def avg(scores):
    total = 0.0
    for score in scores:
        total += score
    return round(total/len(scores), 2)

students = [
    {"name": "Sam", "scores": [80, 90]},
    {"name": "David", "scores": [55, 60]}
]


records = [(student["name"], avg(student["scores"]), grader(avg(student["scores"]))) for student in students]
        

for record in records:
    print(f"{record[0]} -> avg: {record[1]} -> Grade: {record[2]}")

passed_A_to_C = [record[0] for record in records if record[2]  in ("A","B","C")]
print(f"Students who paseed A through C: {passed_A_to_C}")

highest = 0
lowest = 100
for record in records:
    if record[1] >= highest:
        highest = record[1]
    if record[1] <= lowest:
        lowest = record[1]

print(f"Highest: {highest}")
print(f"Lowest: {lowest}")


