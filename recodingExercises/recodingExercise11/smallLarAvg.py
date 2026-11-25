"""
2. Smallest, Largest and Average

Suggested time: 15–20 minutes

Problem
Write stats(nums) that returns (smallest, largest, average) for a list of numbers. Round the average to 2 decimal places. For an empty list, return None.
Examples
stats([4, 9, 2, 7])   → (2, 9, 5.5)
stats([5])            → (5, 5, 5.0)
stats([-3, -1, -2])   → (-3, -1, -2.0)
stats([])             → None
Constraints
Do not use min(), max(), or sum().
Find all three in one loop.
Do not change the list passed in.
What this gauges: Tracking several values in one pass, and handling empty input safely (you will need this for your app).

"""

def stats(nums):
    if not nums:
        return None
    
    smallest, largest, total = nums[0], nums[0], nums[0]
    
    for num in nums[1::]:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
        total += num

    avg = round(total/len(nums), 2)

    return smallest, largest, avg

print(stats([4, 9, 2, 7]))
print(stats([5]))
print(stats([-3, -1, -2]))
print(stats([]))