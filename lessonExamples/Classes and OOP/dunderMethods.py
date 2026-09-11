class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'"{self.title}" by "{self.author}"'

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if isinstance(other, tuple):
            other = Book(*other)
        if isinstance(other, Book):
            return self.pages == other.pages and self.author == other.author and self.title == other.title
        if not isinstance(other, Book):
            return NotImplemented

book1 = Book("Python Mastery", "Micah", 450)
book2 = Book("Python Mastery", "Micah", 450)

print(book1)
print(repr(book1))
print(len(book1))
print(book1 == book2)