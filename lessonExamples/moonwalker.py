"""
Moonwalker

numbers = [
    3, 8, 12, 5, 17, 21, 4, 9, 14, 6,
    25, 11, 18, 7, 30, 2, 16, 13, 20, 10
]

Count how many numbers are even among the elements encountered 
when walking backward from the second-to-last element to the 
beginning, visiting every second element.

In other words:

Start at the second-to-last element.
Move backward by 2 positions each time.
Continue until you reach the beginning of the list.
Count how many of the encountered numbers are even.
Restrictions

You must:

Use negative-step slicing to select the elements.
Use a counting technique to determine the number of even values.
Not use reversed().
Not use .reverse().
Don't manually write the indices.
"""

numbers = [
    3, 8, 12, 5, 17, 21, 4, 9, 14, 6,
    25, 11, 18, 7, 30, 2, 16, 13, 20, 10
]

michael = numbers[len(numbers)-2::-2]
# count = 0
# for num in michael:
    # if num%2 == 0:
        # count += 1 
"or"
jackson = sum(num % 2 == 0 for num in michael) #sum adds the boolean values to get the even num count
print(jackson)

"or"
michael_jackson = [num for num in numbers[len(numbers)-2::-2] if num % 2 == 0]
print(len(michael_jackson))

"or"
print(sum(num % 2 == 0 for num in numbers[len(numbers)-2::-2]))