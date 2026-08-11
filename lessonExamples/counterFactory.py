"""
Implement:

def make_counter(start):
    # your code

It should return another function that increments and 
returns a counter each time it is called.

Your constraints:
You must use an inner function.
You must use a closure—don't use a global variable.
The inner function should modify the enclosing variable.
Don't use a class.

One hint:
The inner function to modify a variable 
belonging to its enclosing function.
"""

def make_counter(start):

    def count():
        nonlocal start
        start += 1
        return start
    return count

counter_a = make_counter(0)
counter_b = make_counter(100)

print(counter_a())  # 1
print(counter_a())  # 2
print(counter_b())  # 101
print(counter_a())  # 3
print(counter_b())  # 102

menu_items = [
    {"name": "Mocha", "price": True},
    {"name": "Espresso", "price": False},
    {"name": "Latte", "price": False}
]
print(sorted(menu_items, key = lambda p: p["price"]))