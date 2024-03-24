from askvar import askvar

x = askvar('x')
if x <= -7:
    y = -2*x + 7/2
elif -7 < x < 1:
    y = (x**2 - 3*x + 5) / (x**2 + 2)
elif 1 <= x <= 8:
    y = (x**2 + 2*x + 2)**0.5 + abs(1.5*x - 4/7)**0.5
else:
    y = abs(3/x**2 - 11*x)
    
print(f'y = {y}')