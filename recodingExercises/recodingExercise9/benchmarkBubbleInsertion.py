"""
This code compares the run time for bubble sort and insertion sort algorithms using the Python timeit module
"""

import timeit

def insertion_sort(nums):
    comparisons = 0
    shifts = 0
    for i in range(1, len(nums)):
        key = nums[i]
        key_idx = i
        mover_idx = i - 1
        while key_idx > 0 and nums[mover_idx] > key:
            comparisons += 1
            nums[key_idx] = nums[mover_idx]
            mover_idx -= 1
            key_idx -= 1
            shifts += 1
            
        if key_idx > 0:
            comparisons += 1

        nums[key_idx] = key

    return comparisons, shifts

def bubble_sort(nums):
    comparisons = 0
    swaps = 0
    for i in range(len(nums)):
        swapped = False
        for j in range(len(nums) - 1 - i):
            comparisons += 1
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swaps += 1
                swapped = True
        if not swapped:
            break

    return comparisons, swaps

def benchmark(sort_function, nums, repetitions=5):
    times = []

    for _ in range(repetitions):
        data = nums.copy()

        start = timeit.default_timer()
        sort_function(data)
        elapsed = timeit.default_timer() - start

        times.append(elapsed)

    return min(times)


sizes = [100, 200, 400, 800, 1600, 3200, 6400]

prev_insertion_sorted = None
prev_insertion_reversed = None
prev_insertion_nearly_sorted = None

prev_bubble_sorted = None
prev_bubble_reversed = None
prev_bubble_nearly_sorted = None

print(
    f"{'Size':<8}"
    f"{'Ins_sorted (s)':<18}"
    f"{'Ratio':<10}"
    f"{'Ins_reversed (s)':<18}"
    f"{'Ratio':<10}"
    f"{'Ins_nearly_sorted (s)':<18}"
    f"{'Ratio':<10}"
    f"{'Bub_sorted (s)':<18}"
    f"{'Ratio':<10}"
    f"{'Bub_reversed (s)':<18}"
    f"{'Ratio':<10}"
    f"{'Bub_nearly_sorted (s)':<18}"
    f"{'Ratio':<10}"
)

for n in sizes:
    nums_sorted = list(range(n))
    nums_reversed = list(range(n, 0, -1))
    nums_nearly_sorted = list(range(n))
    nums_nearly_sorted[n//2], nums_nearly_sorted[(n//2)+1] = nums_nearly_sorted[(n//2)+1], nums_nearly_sorted[n//2]

    insertion_time_sorted = benchmark(insertion_sort, nums_sorted)
    insertion_time_reversed = benchmark(insertion_sort, nums_reversed)
    insertion_time_nearly_sorted = benchmark(insertion_sort, nums_nearly_sorted)

    bubble_time_sorted = benchmark(bubble_sort, nums_sorted)
    bubble_time_reversed = benchmark(bubble_sort, nums_reversed)
    bubble_time_nearly_sorted = benchmark(bubble_sort, nums_nearly_sorted)

    insertion_ratio_sorted = (
        insertion_time_sorted / prev_insertion_sorted
        if prev_insertion_sorted is not None and prev_insertion_sorted > 0
        else 0
    )

    insertion_ratio_reversed = (
        insertion_time_reversed / prev_insertion_reversed
        if prev_insertion_reversed is not None and prev_insertion_reversed > 0
        else 0
    )

    insertion_ratio_nearly_sorted = (
        insertion_time_nearly_sorted / prev_insertion_nearly_sorted
        if prev_insertion_nearly_sorted is not None and prev_insertion_nearly_sorted > 0
        else 0
    )

    bubble_ratio_sorted = (
        bubble_time_sorted / prev_bubble_sorted
        if prev_bubble_sorted is not None and prev_bubble_sorted > 0
        else 0
    )

    bubble_ratio_reversed = (
        bubble_time_reversed / prev_bubble_reversed
        if prev_bubble_reversed is not None and prev_bubble_reversed > 0
        else 0
    )

    bubble_ratio_nearly_sorted = (
        bubble_time_nearly_sorted / prev_bubble_nearly_sorted
        if prev_bubble_nearly_sorted is not None and prev_bubble_nearly_sorted > 0
        else 0
    )

    print(
    f"{n:<8}"
    f"{insertion_time_sorted:<18.6f}"
    f"{insertion_ratio_sorted:<10.2f}"
    f"{insertion_time_reversed:<18.6f}"
    f"{insertion_ratio_reversed:<10.2f}"
    f"{insertion_time_nearly_sorted:<22.6f}"
    f"{insertion_ratio_nearly_sorted:<10.2f}"
    f"{bubble_time_sorted:<18.6f}"
    f"{bubble_ratio_sorted:<10.2f}"
    f"{bubble_time_reversed:<18.6f}"
    f"{bubble_ratio_reversed:<10.2f}"
    f"{bubble_time_nearly_sorted:<22.6f}"
    f"{bubble_ratio_nearly_sorted:<10.2f}"
    )

    prev_insertion_sorted = insertion_time_sorted
    prev_insertion_reversed = insertion_time_reversed
    prev_insertion_nearly_sorted = insertion_time_nearly_sorted

    prev_bubble_sorted = bubble_time_sorted
    prev_bubble_reversed = bubble_time_reversed
    prev_bubble_nearly_sorted = bubble_time_nearly_sorted