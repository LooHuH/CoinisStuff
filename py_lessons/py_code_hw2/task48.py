from askvar import askvar

x = askvar('x')
n = askvar('n')

out = 1
for _ in range(n):
    out *= x
    
print(f'{x}**{n} == {out}')