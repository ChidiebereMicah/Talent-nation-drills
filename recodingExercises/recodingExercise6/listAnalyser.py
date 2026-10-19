"""
List Analyser — Extended

Suggested time: 12–15 minutes
Problem
Given a list of numbers, find the smallest, largest, total, and average — and also report the index of the smallest and largest values, and how many numbers are above the average.
Examples
Starting list: numbers = [12, 5, 27, 8, 14, 27, 3]
Input list: [12, 5, 27, 8, 14, 27, 3]
Smallest: 3 (at index 6)
Largest: 27 (at index 2)
Total: 96
Average: 13.71
Numbers above average: 3
Constraints
Use loops and variables to calculate all results.
Do not use min(), max(), sum(), .index(), or .count().
You may use len() for the average.
If the smallest or largest value appears more than once, report the first index where it appears.
The “numbers above average” count must be calculated in a second pass through the list (after the average is known).
Assume the list contains at least one number.
"""

def list_analyser(num_list):
    smallest = num_list[0]
    largest = num_list[0]
    total = num_list[0]
    small_index = 0
    large_index = 0

    if len(num_list) > 1:
        for index, num in enumerate(num_list[1:]):
            if num > largest:
                largest = num
                large_index = index + 1
            elif num < smallest:
                smallest = num
                small_index = index + 1
            total += num

    average = round(total/len(num_list), 2)

    count = 0
    for num in num_list:
        if num > average:
            count += 1

    return smallest, small_index, largest, large_index, total, average, count

smallest, small_index, largest, large_index, total, average, count = list_analyser([12, 5, 27, 8, 14, 27, 3])

print(f"Smallest: {smallest} (at index {small_index})\n"
      f"Largest: {largest} (at index {large_index})\n"
      f"Total: {total}\n"
      f"Average: {average}\n"
      f"Numbers above average: {count}\n"
      )