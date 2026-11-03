"""
7. Find Duplicates
Suggested time: 15–20 minutes
Problem
Given a list of numbers, find all the numbers that appear more than once. Print each duplicate only once, in the order it first appears as a duplicate.
Examples
Input: [1, 2, 3, 2, 4, 5, 1] → [1, 2]
Input: [4, 4, 4, 4] → [4]
Input: [1, 2, 3, 4] → [] (no duplicates)
Input: [10, 20, 10, 30, 20] → [10, 20]
Constraints
Use loops and conditionals.
Do not use set().
Do not use .count().
Do not use sort() or sorted().
Do not import libraries.
Each duplicate should appear only once in the output.
Do not hardcode the answer.
What This Tests: Looping, membership checks, conditionals, and deduplication without sets.
Optional Stretch: Return the duplicates along with how many times each one appears, stored in a dictionary.

"""

def find_duplicates(nums):
    num_freq = {}
    duplicates = []
    for num in nums:
        num_freq[num] = num_freq.get(num, 0) + 1

        if num_freq[num] == 2:
            duplicates.append(num)

    return duplicates


nums1 = [1, 2, 3, 2, 4, 5, 1]
nums2 = [4, 4, 4, 4] 
nums3 = [1, 2, 3, 4] 
nums4 = [10, 20, 10, 30, 20]
nums5 = []
nums6 = [1, 2, 2, 1]

print(find_duplicates(nums4))

# Optional stretch
# def find_duplicates_with_counts(nums):
#     num_freq = {}
#     duplicates = {}

#     for num in nums:
#         num_freq[num] = num_freq.get(num, 0) + 1

#         if num_freq[num] == 2:
#             duplicates[num] = 2
#         elif num in duplicates:
#             duplicates[num] = num_freq[num]

#     return duplicates