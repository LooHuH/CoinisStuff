from askvar import askvar

x = askvar('x')
y = askvar('y')

tempvar = x
x = y
y = tempvar

print(f'x = {x}',
      f'y = {y}',
      sep='\n')
