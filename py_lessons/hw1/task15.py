from askvar import askvar

x1 = askvar('x1')
y1 = askvar('y1')

x2 = askvar('x2')
y2 = askvar('y2')

x3 = askvar('x3')
y3 = askvar('y3')

x12 = abs(x1 - x2)
y12 = abs(y1 - y2)

x23 = abs(x2 - x3)
y23 = abs(y2 - y3)

x13 = abs(x1 - x3)
y13 = abs(y1 - y3)

a = (x12**2 + y12**2) ** 0.5
b = (x23**2 + y23**2) ** 0.5
c = (x13**2 + y13**2) ** 0.5

P = (a + b + c) / 2
S = (P * (P - a) * (P - b) * (P - c)) ** 0.5

print(f'S = {S}')
