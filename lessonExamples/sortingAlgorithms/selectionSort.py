def selection_sort(nums):
    comparisons = 0
    swaps = 0

    for i in range(len(nums)-1):
        min_idx = i
        for j in range(i+1, len(nums)):
            comparisons += 1
            if nums[min_idx] > nums[j]:
                min_idx = j
        if min_idx != i:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
            swaps += 1

    return nums, comparisons, swaps

nums1 = [9, 4, 7, 2, 6]
nums2 = [5, 4, 3, 2, 1]
nums3 = [5]
nums4 = []

nums, comparisons, swaps = selection_sort(nums4)
print(f"sorted {nums} with {comparisons} comparisons and {swaps} swaps")
print()