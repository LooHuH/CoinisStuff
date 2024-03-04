from askvar import askvar

num = askvar('code', raw=True, len_barrier=[3, 3])

a = int(num[0])
b = int(num[1])
c = int(num[2])

print(f'Sum - {sum((a, b, c))}')
