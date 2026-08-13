"""
Testing out possible set manipulations
"""

fruits = {"apple", "banana"}

fruits.update(["orange", "mango", "grape"]) #add each element of iterable
print(fruits)

fruits.add(("coconut", "watermelon")) #can add tuple to set
print(fruits)

fruits.add(["agbalumo", "lime", "breadfruit"]) #cannot add list to set
print(fruits)

fruits.add({"blueberry", "strawberry"}) #cannot set list to set
print(fruits)

fruits.add("pomegranate") #adds each element of the iterable also
print(fruits)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A|B)
print(A & B)
print(A)
print(B)

A.update(B) #modifies A to become the union of A and B
print(A)

A |= B #also modifies A to become the union of A and B
print(A)

print(A & B) #in A and also in B
print(A ^ B) #only in A and only in B 