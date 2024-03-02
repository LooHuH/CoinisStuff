from askvar import askvar

x1 = askvar('x1')
y1 = askvar('y1')
x2 = askvar('x2')
y2 = askvar('y2')

a = x1 - x2
b = y2 - y1

r = (a**2 + b**2)**0.5

print(f'Distance = {r}')
