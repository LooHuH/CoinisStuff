from askvar import askvar

p = askvar('Petar apples')
m = askvar('Milos apples')

if p > m:
    print('Petar has more apples')
elif m > p:
    print('Milos has more apples')
else:
    print("Wait, this isn't supposed to happen")