"""
C2. Insertion Sort (Revision: Count Your Work)
Suggested time: 25 to 30 minutes
Problem
Implement insertion_sort(nums) that sorts the list in place and returns a tuple (comparisons, shifts).
Counting rules: each time you compare the item being inserted (the key) with an element to its left, that is one comparison. Each time you move an element one place to the right, that is one shift.
Examples
[5, 2, 4, 1]  -> sorted [1, 2, 4, 5], returns (6, 5)
[1, 2, 3, 4]  -> already sorted, returns (3, 0)
[4, 3, 2, 1]  -> reversed, returns (6, 6)
[]            -> returns (0, 0)

Constraints
No sort(), sorted(), min() or max().
Sort in place. The function returns only the two counts.
From outside the function, show with the counts that an already sorted list of 10 numbers costs less than a reversed list of 10, then do the same for 20 numbers. Write one sentence on the pattern.
Do not import libraries.
Bonus
Run last week’s bubble sort and this function on the same five lists. Which one does less work on nearly sorted lists? Write one sentence explaining why.
What this gauges: Can you shift items to open a gap and insert into it? Can you measure your own code and see that input order changes the cost?

"""

def insertion_sort(nums):
    comparisons = 0
    shifts = 0
    for i in range(1, len(nums)):
        key = nums[i]
        key_idx = i
        mover_idx = i - 1
        while key_idx > 0:
            comparisons += 1
            if nums[mover_idx] > key:
                nums[key_idx] = nums[mover_idx]
            mover_idx -= 1
            key_idx -= 1
            shifts += 1
        nums[key_idx] = key

    return nums, comparisons, shifts

nums1 = [5, 2, 4, 1]
nums2 = [1, 2, 3, 4]
nums3 = [4, 3, 2, 1] 
nums4 = []
nums, comparisons, shifts = insertion_sort(nums1)
print(f"{nums1}  -> sorted {nums}, returns ({comparisons}, {shifts})")
            

