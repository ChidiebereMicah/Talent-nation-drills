entry = input("Enter your numbers seperated by a comma e.g 1,2,3,4: ")
try:
    num_list = (entry.split(','))
except Exception:
    print("Use the right format e.g 2,4,6,8")

num_list = {float(num) for num in num_list}
num_list = [num for num in num_list]

for i in range(len(num_list)):
    swapped = False
    for j in range(0,len(num_list) - i - 1):
        if num_list[j] > num_list[j + 1]:
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
            swapped = True
        if not swapped:
            break

print(num_list[-2])
