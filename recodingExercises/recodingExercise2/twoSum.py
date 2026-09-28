def two_sum(num_list, target):
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            if num_list[i] + num_list[j] == target:
                return f"{num_list[i]} + {num_list[j]} = {target}"
    return "No pair sums up to target"

num_list = [6, 4, 7, 4]
target = 8
print(two_sum(num_list, target))