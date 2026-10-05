def twoSum(num_list, target):
    seen = {}
    for index, num in enumerate(num_list):
        diff = target - num
        if diff in seen:
            return [seen[diff], index]
        seen[num] = index

print(twoSum([2, 7, 11, 15], 9))