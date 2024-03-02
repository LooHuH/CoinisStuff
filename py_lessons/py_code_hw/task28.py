from askvar import askvar

var = askvar('code', len_barrier=[3, 3], raw=True)

ans = var[::-1]
print(f'Answer - {ans}')
