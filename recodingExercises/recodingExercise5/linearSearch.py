def linear_search(num_list, target):
    for index, num in enumerate(num_list):
        if num == target:
            return (f"Target: {target}\n"
                    f"Found at index {index}")
    return (f"Target: {target}\n"
            "Target not found")

values = [14, 7, 22, 9, 7, 31]
print(linear_search(values, 22))
print(linear_search(values, 18))


        
