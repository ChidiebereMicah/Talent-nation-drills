"""
Write a list comprehension that achieves the exact same results 
as list(map(lambda x: x * 2, prices))
"""
prices = [8,4,5,7]
print(list(map(lambda x: x * 2, prices)))

print([x*2 for x in prices]) #note that the comprihension must be enclosed in a list