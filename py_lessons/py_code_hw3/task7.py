class Book:
    def __init__(
            self, 
            name: str, 
            author: str, 
            year: int, 
            amount: int):
        
        self.___name = name
        self.___author = author
        self.___year = year
        self.___amount = amount
    
    def set(self, 
            name: str = None, 
            author: str = None, 
            year: int = None, 
            amount: int = None):
        
        if name is not None:
            self.___name = name
        if author is not None:
            self.___author = author
        if year is not None:
            self.___year = year
        if amount is not None:
            self.___amount = amount
    
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
            result['name'] = self.___name
        if author:
            result['author'] = self.__author
        if year:
            result['year'] = self.__year
        if amount:
            result['amount'] = self.__amount
        
        return result


class Library:
    def __init__(self):
        self.__books = []
    
    def add_book(self, book: Book):
        self.__books.append(book)
    
    def delete_book(self, book_name: str):
        for book in self.__books:
            if book.get(name=True)['name'] == book_name:
                self.__books.remove(book)
                break
    
    def search_book(self, name: str = None, author: str = None):
        for book in self.__books:
            book_info = book.get(name=True, author=True)
            if (name == book_info['name']
                    or author == book_info['author']):
                return book
    
    def show_books(self, print_result: bool = False):
        result = []
        for book in self.__books:
            book_info = book.get(all=True, amount=False)
            book_amount = book.get(amount=True)['amount']
            if book_amount > 0:
                result.append(book_info)
        if print_result:
            print(result)
        else:
            return result
