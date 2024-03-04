from askvar import askvar

num = askvar('code', raw=True, len_barrier=[4, 4])

a = int(num[0])
b = int(num[1])
c = int(num[2])
d = int(num[3])

open_code = (a + d)**2 - (b**2 - c**2)

print(f'Code for safe - {open_code}')
