# def make_multiplier(factor):
#     def multiply(x):
#         return x * factor
#     return multiply

# double = make_multiplier(2)

# print(make_multiplier(3)(5))

def outer(a):
    b = a + 1

    def inner(c):
        return a + b + c

    return inner

f = outer(10)

print(f(5))
print(type(f))