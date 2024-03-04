from askvar import askvar

var = askvar('code', len_barrier=[4, 4], raw=True)

ans = sum(int(x) for x in var) ** 2
print(f'Floor - {ans}')
