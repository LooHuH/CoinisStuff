from askvar import askvar

a = askvar('a')
b = askvar('b')

P = 2 * (a + b)
S = a * b

print(f'P = {P}',
      f'S = {S}',
      sep='\n')
