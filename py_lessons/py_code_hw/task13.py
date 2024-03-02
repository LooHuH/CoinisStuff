from askvar import askvar

x1 = askvar('x1')
y1 = askvar('y1')
x2 = askvar('x2')
y2 = askvar('y2')

x3 = x2 + 2
y3 = y2 - 3

print(f'a) Treasure cords are - ({x3}, {y3})')

x13 = abs(x1 - x3)
y13 = abs(y1 - y3)

S13 = (x13**2 + y13**2)**0.5

print(f'b) Distance betweeen start and treasure - {S13}')

x12 = abs(x1 - x2)
y12 = abs(y1 - y2)
S12 = (x12**2 + y12**2)**0.5

x23 = abs(x2 - x3)
y23 = abs(y2 - y3)
S23 = (x23**2 + y23**2)**0.5

S123 = S12 + S23

print(f'c) Distance of all way - {S123}')
