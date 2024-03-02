from askvar import askvar

num = askvar('code', raw=True, len_barrier=[3, 3])

a = int(num[0])
b = int(num[1])
c = int(num[2])

open_code = (a * b * c) - sum((a, b, c))

print(f'Code for gate - {open_code}')
