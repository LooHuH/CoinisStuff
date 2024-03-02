from askvar import askvar

var = askvar('number', len_barrier=[6, 6], raw=True)

a = int(var[0])
b = int(var[1])
c = int(var[2])
d = int(var[3])
e = int(var[4])
f = int(var[5])

ans = a * c + 2 + f == b + d * e

print(f'Answer is {ans}')
