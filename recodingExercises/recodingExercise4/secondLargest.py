def secondLargest(num_list):
    num_list = {num for num in num_list}
    largest = 0
    second_largest = 0
    for num in num_list:
        if num > largest:
            largest = num
        elif num > second_largest and num > largest:
            second_largest = num
    return second_largest

print(secondLargest([4, 4, 4, 4, 4, 3]))

    