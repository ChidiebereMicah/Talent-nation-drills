def selection_sort(nums):
    for i in range(len(nums)-1):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[min_idx] > nums[j]:
                min_idx = j
        if min_idx != i:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

nums1 = [9, 4, 7, 2, 6]
nums2 = [5, 4, 3, 2, 1]
nums3 = [5]
nums4 = []
print(selection_sort(nums2))