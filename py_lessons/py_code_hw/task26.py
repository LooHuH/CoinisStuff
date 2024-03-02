from askvar import askvar

var = askvar('code', len_barrier=[4, 4], raw=True)

print(f'Floor - {var[-1]}')
