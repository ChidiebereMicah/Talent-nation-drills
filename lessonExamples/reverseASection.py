"""
Write an expression using only list slicing that produces:
1. [80, 70, 60, 50, 40] from numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
2. [100, 80, 60, 40] from numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
Requirements
You must use the start, stop, and step values.
Your step must be negative.
Don't use reversed().
Don't use a for loop.
Don't use sort() or reverse().
Hint

First identify the indices of the values you want:

Value:    10  20  30  40  50  60  70  80  90
Index:     0   1   2   3   4   5   6   7   8
"""

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(numbers[7:2:-1])

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
print(numbers[len(numbers)-2:2:-2])