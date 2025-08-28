class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def list_book(self):
        return [f"{book.title} by {book.author}" for book in self.books]

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

lib = Library("NY Public Library")

book1 = Book("Monk who sold his car", "Robin Sharma")
book2 = Book("Ponniyin Selvan", "Amarar Kalki")

lib.add_book(book1)
lib.add_book(book2)

print(*lib.list_book(), sep="\n")