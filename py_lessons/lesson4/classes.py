class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f'Title: {self.title}; Author: {self.author}; Pages: {self.pages}'
    
    def __len__(self):
        return self.pages
    
    def __gt__(self, other_book):
        return self.pages > other_book.pages


book1 = Book('Uvod u veb programiranje', 'Marko Markovic', 260)
book2 = Book('GraphQL', 'Ilija Ivanovic', 350)

books = [book1, book2]
for book in books:
    print(book)
print(book1 > book2)