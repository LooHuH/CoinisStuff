from askvar import askvar

x = askvar('x')
y = askvar('y')

wire = 2 * x + 5

if y == wire:
    print('bee is on wire')
else:
    print('bee is not on wire')