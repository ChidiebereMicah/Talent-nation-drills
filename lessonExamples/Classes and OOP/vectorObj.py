"""Direct comparison of two vector objects i.e comparing their elements and not their instances"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y})'

    def __eq__(self, other): #__eq__ is called by an obj of Vector class and receives another obj- other- as arg
        print("__eq__ called")
        if isinstance(other, tuple): #check to see if other is an obj of tuple before making it an obj of Vector
            other = Vector(*other)
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

a = Vector(1,2)
b = (1,2)
print(a.__eq__(b))