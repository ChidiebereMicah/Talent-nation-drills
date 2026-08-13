"""
Write a function:
def student_report(name, scores):
where scores is a dictionary containing a student's subject scores

For example:

scores = {
    "math": 85,
    "english": 92,
    "python": 78
}

Your function should return a dictionary containing:
{
    "name": "Micah",
    "subjects": 3,
    "average": 85.0,
    "status": "Pass"
}

Requirements

1. Validate the required subjects
The dictionary must contain "math", "english", and "python".

Use the in operator to check for missing subjects.
If any are missing, return:
{"error": "Missing subject"}

2. Safely retrieve an optional subject
The student may also have a "database" score.
Use .get() to retrieve it.
If it doesn't exist, assume its score is 0.
"""

def student_report(name, scores):

    total_score = 0
    subject_num = 0
    subjects = ("math", "english", "python")
    
    for subject in subjects:
        if subject not in scores:
            return {"error": "Missing subject"}

    for subject in scores:
        subject_num += 1
        total_score += scores.get(subject, 0)

    avg = round(total_score/subject_num,2)

    return {
         "name": name,
         "subjects": subject_num,
         "average": avg,
         "status": "Pass" if avg>= 50 else "Fail"
    }
    

scores = {
    "math": 85,
    "english": 92,
    "python": 78
}

print(student_report("Nurudeen", scores))