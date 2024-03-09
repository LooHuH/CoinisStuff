from askvar import askvar

a = askvar('a')
b = askvar('b')

if ((a > b) and (2*b <= a)
        or (a < b) and (2*a <= b)):
    print('you can place 2 squares in this rectangle')
else:
    print('you can not place 2 squares in this rectangle')