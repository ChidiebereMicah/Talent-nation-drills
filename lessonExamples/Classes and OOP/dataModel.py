
class Book:
    category = "Programming"

    def __init__(self, title):
        self.title = title

book = Book("Python Mastery")

"Introspecting attributes to show how Python Data Model maps them"
"__dict__ shows all the attributes in an object's namespace"

print(Book.__dict__)
print(book.__dict__)#only the instance attribute is available in the namespace of a class instance