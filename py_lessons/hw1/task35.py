from askvar import askvar

var = askvar('number', len_barrier=[5, 5], raw=True)

a = int(var[0])
b = int(var[1])
c = int(var[2])
d = int(var[3])
e = int(var[4])

ans = c + e

print(f'Answer - {ans}')
