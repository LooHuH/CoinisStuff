from askvar import askvar

a = askvar('a')
b = askvar('b')
c = askvar('c')

# a*x^2 + b*x + c = 0
D = b**2 - 4*a*c
x1 = (-b + D**0.5) / (2*a)
x2 = (-b - D**0.5) / (2*a)

print(f'x1 = {x1}',
      f'x2 = {x2}',
      sep='\n')
