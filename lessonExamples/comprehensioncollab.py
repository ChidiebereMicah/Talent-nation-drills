
# my_list = [20, 30, 200000]

# # for num in my_list:
# #     print(num*2)

# money_doubler = {num*2 for num in my_list}
# print(money_doubler)

# #print(num*2 for num in my_list)

numbers = list(range(1,101))
even_num = {num for num in numbers if num%2 == 0}
# print(even_num)

odd_num = [num for num in numbers if num not in even_num]
print(odd_num)

labels = ["even" if num % 2 == 0 else "odd"
          for num in numbers]
print(labels)

