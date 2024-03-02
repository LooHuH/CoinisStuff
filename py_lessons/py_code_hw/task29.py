from askvar import askvar

x1 = askvar('x1')
y1 = askvar('y1')
x2 = askvar('x2')
y2 = askvar('y2')

x3 = (x1 + x2) / 2
y3 = (y1 + y2) / 2

print(f'Middle cords are:',
      f'x3 - {x3}',
      f'y3 - {y3}',
      sep='\n')
