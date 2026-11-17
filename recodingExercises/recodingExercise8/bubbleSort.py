"""
6. Bubble Sort (Revision: Best Case vs Worst Case)
Suggested time: 20–25 minutes

Problem
Implement bubble sort that sorts a list in place and returns the number of comparisons and swaps it performed.
Examples
[5, 1, 4, 2, 8] → sorted [1, 2, 4, 5, 8], with counts
[1, 2, 3, 4, 5] → already sorted: your optimized version should stop after ONE pass
[]              → [] with 0 comparisons and 0 swaps
Constraints
No sort(), sorted(), min(), max().
Implement the early-exit optimization: if a full pass makes no swaps, stop immediately.
Each pass should check one fewer pair than the last (the largest items have already settled at the end).
Show with comparison counts that your function makes fewer comparisons on an already-sorted list than on a reverse-sorted list of the same size.
Do not import libraries.
Bonus
Add a descending=True parameter that sorts largest to smallest.
What this gauges: Can you measure your own code, and do you understand that one algorithm can have different costs depending on its input?

"""
def bubble_sort(nums):
    comparisons = 0
    swaps = 0
    for i in range(len(nums)):
        arranged = True
        for j in range(i+1,len(nums)):
            if j < len(nums):
                comparisons += 1
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    swaps += 1
                if j < len(nums) - 1 and nums[j] > nums[j+1]:
                    arranged = False
        if arranged:
            return nums, comparisons
                    
    return nums, comparisons

nums1 = [5, 1, 4, 2, 8]
nums2 = [1, 2, 3, 4, 5]
nums3 = [4,1,2,6,7,8,9]
nums4 = []
nums5 = [3,5,1,7,3,8,2,9,4]

nums, comparisons = bubble_sort(nums1)
print(f"sorted {nums} with {comparisons}")
print()
nums, comparisons = bubble_sort(nums2)
print(f"sorted {nums} with {comparisons}")
print()
nums, comparisons = bubble_sort(nums3)
print(f"sorted {nums} with {comparisons}")
print()
nums, comparisons = bubble_sort(nums4)
print(f"sorted {nums} with {comparisons}")
print()
nums, comparisons = bubble_sort(nums5)
print(f"sorted {nums} with {comparisons}")
