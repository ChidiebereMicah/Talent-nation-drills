"""
Binary Search (Revision: Count Your Steps)

Suggested time: 20–25 minutes

Problem
Given a sorted list of integers and a target, return the index of the first (leftmost) occurrence of the target, or -1 if it is not present. Also return how many comparisons your search made.
Examples
nums = [1, 3, 3, 3, 5, 8], target = 3  → (1, comparisons)
nums = [1, 3, 5, 8],       target = 4  → (-1, comparisons)
nums = [],                 target = 7  → (-1, 0)
Constraints
Use a while loop with low and high pointers. No recursion in the main version.
No .index(), no in, no .count().
Must find the leftmost match when duplicates exist. Finding any match is not enough.
The function binary_search(nums, target) -> tuple[int, int] must be pure: no printing inside.
Do not import libraries.
Bonus
Write a recursive version of binary search and check that it returns the same answers as your loop version on at least five test cases.
What this gauges: Can you shrink the problem each step instead of scanning everything? Can you handle duplicates and empty lists?

"""

def binary_search(nums, target):
    index = 0
    comparisons = 0
    while index < len(nums):
        comparisons += 1
        if nums[index] == target:
            return nums, target, index, comparisons
        index += 1
    index = -1
    return nums, target, index, comparisons

nums = [1, 3, 3, 3, 5, 8]
# nums = [1, 3, 5, 8]
# nums = []
nums, target, index, comparisons = binary_search(nums, 8)
print(f"nums = {nums}, target = {target}  → ({index}, {comparisons})")