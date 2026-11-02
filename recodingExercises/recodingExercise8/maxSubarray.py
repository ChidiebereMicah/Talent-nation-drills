"""
Maximum Subarray (Revision: Brute Force vs Single Pass)
Suggested time: 25–30 minutes
Problem
Given a list of integers (positive and negative), find the contiguous slice with the largest sum. Return the sum and the start and end indices.
Examples
[-2, 1, -3, 4, -1, 2, 1, -5, 4] → sum 6, indices (3, 6)   # [4, -1, 2, 1]
[5]                              → sum 5, indices (0, 0)
[-3, -1, -2]                     → sum -1, indices (1, 1)
Constraints
Write two functions:
max_subarray_brute(nums): checks every possible slice (nested loops are allowed here).
max_subarray_fast(nums): a single pass with no nested loops.
Both must return identical answers on every test.
No max(), min(), sum(), or slicing to compute sums.
All-negative lists must return the single largest element, not 0.
Do not import libraries.
Hint
At each position, ask: is it better to extend the running sum, or to start fresh here?
Bonus
Write a test loop that runs both versions on at least five lists of your own (including an empty list) and prints Match or Mismatch for each.
What this gauges: Can you replace brute force with a single-pass insight, and prove the two agree?
"""

def max_subarray_brute(nums):
    if not nums:
        return nums, None, None, None
    sum = nums[0]
    for i in range(len(nums)):
        sub_array = nums[i]
        for j in range(i, len(nums)):
            if sum <= sub_array:
                sum = sub_array
                start, stop = i, j
            if j != len(nums)-1:
                sub_array += nums[j+1]

    return nums, sum, start, stop

nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [5]
nums3 = [-3, -1, -2]
nums4 = []
nums, sum, start, stop = max_subarray_brute(nums4)
print(f"{nums} → sum {sum}, indices ({start}, {stop})")
