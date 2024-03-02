d = 50
a0 = 16
b0 = 9

d0 = (a0**2 + b0**2)**0.5

x = d / d0

a = a0 * x
b = b0 * x

S = a * b

print(f'S = {S}')
