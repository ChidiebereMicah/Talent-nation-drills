"""
Exemplification of mutable and immutable types in Python
"""

my_list = [1,2,3,4]
print(id(my_list))
my_list[1] = 9
print(id(my_list)) #still the same - mutable

my_string = "sunshine"
print(id(my_string))
my_string = "sunny"
print(id(my_string)) #address changes - not mutable


my_dict = {"name": "Micah",
           "age": "young",
           "fashion": "swag"}
print(id(my_dict))
my_dict["fashion"] = "sleek"
print(id(my_dict)) #address still same - mutable

my_tuple = (8,6,4,2)
print(id(my_tuple))
my_tuple = (10,8,6,4)
print(id(my_tuple)) #address changes - not mutable
