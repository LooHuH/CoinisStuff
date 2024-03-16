class Book:
    def __init__(
            self, 
            name: str, 
            author: str, 
            year: int, 
            amount: int):
        
        self._name = name
        self._author = author
        self._year = year
        self._amount = amount
    
    def set(self, 
            name: str = None, 
            author: str = None, 
            year: int = None, 
            amount: int = None):
        
        if name is not None:
            self._name = name
        if author is not None:
            self._author = author
        if year is not None:
            self._year = year
        if amount is not None:
            self._amount = amount
    
    def get(self, 
            all: bool = None, 
            name: bool = None, 
            author: bool = None, 
            year: bool = None, 
            amount: bool = None):
        
        result = {}
        
        if all:
            if name is None:
                name = True
            if author is None:
                author = True
            if year is None:
                year = True
            if amount is None:
                amount = True
        
        if name:
            result['name'] = self._name
        if author:
            result['author'] = self._author
        if year:
            result['year'] = self._year
        if amount:
            result['amount'] = self._amount
        
        return result


class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self, book: Book):
        self._books.append(book)
    
    def delete_book(self, book_name: str):
        for book in self._books:
            if book.get(name=True)['name'] == book_name:
                self._books.remove(book)
                break
    
    def search_book(self, attribute: str):
        pass
    
    def show_books(self, print_result: bool = False):
        result = [book.get(all=True, amount=False) for book in self._books]
        if print_result:
            print(result)
        else:
            return result
