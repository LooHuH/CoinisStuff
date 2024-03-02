from askvar import askvar

book_price = askvar('book price')
discount = askvar('discount in percents', num_barrier=[0, 100])

new_book_price = book_price * (100-discount)/100

print(f'Price with discount - {new_book_price}')
