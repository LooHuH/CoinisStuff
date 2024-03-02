from askvar import askvar

x = askvar('dimension x')
y = askvar('dimension y')
square = askvar('square size')

ans = (x * y) // square**2

print(f'Answer - {ans}')
