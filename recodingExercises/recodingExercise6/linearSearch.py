"""
Linear Search — All Occurrences + Count
Suggested time: 12–15 minutes

Problem
Given a list and a target value, find every index where the target appears. Print all matching indices, the total count of matches, and the index of the first and last occurrence. If the target does not appear, print a not-found message.
Examples
Starting list: values = [14, 7, 22, 9, 7, 31, 7, 5]
Target: 7 → Found at indices: [1, 4, 6] | Count: 3 | First: 1 | Last: 6
Target: 22 → Found at indices: [2] | Count: 1 | First: 2 | Last: 2
Target: 18 → Target not found
Constraints
Use a loop; do not use .index(), .count(), or list comprehensions.
Do not stop at the first match — you must find all occurrences.
Do not import libraries.
Do not hardcode the answer.
What This Tests: Lists, loops, comparisons, indexing, building a results list, and tracking multiple pieces of state in one pass.

"""

def linear_search(num_list, target):
    appears = []
    for index, num in enumerate(num_list):
        if num == target:
            appears.append(index)
    if not appears:
        return "Target not found"
    else:
        return f"Found at indices: {appears} | Count: {len(appears)} | First: {appears[0]} | Last: {appears[-1]}"

print(linear_search([14, 7, 22, 9, 7, 31, 7, 5], 7))

