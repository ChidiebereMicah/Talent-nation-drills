"""
Given the following sets:
python_class = {"Ada", "James", "Micah", "Sarah", "David"}
ai_class = {"Micah", "Sarah", "John", "David", "Grace"}

Write a function that returns a dictionary containing:

{
    "common": {"Micah", "Sarah", "David"},
    "only_a": {"Ada", "James"},
    "only_b": {"John", "Grace"},
    "all_students": {"Ada", "James", "Micah", "Sarah", "David", "John", "Grace"}
}
"""

def class_overlap(class_a, class_b):
    return {"common": class_a ^ class_b,
            "only_a": class_a - class_b,
            "only_b": class_b - class_a,
            "all_students": class_a | class_b}

python_class = {"Ada", "James", "Micah", "Sarah", "David"}
ai_class = {"Micah", "Sarah", "John", "David", "Grace"}

print(class_overlap(python_class, ai_class))