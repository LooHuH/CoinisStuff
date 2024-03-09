from askvar import askvar

num = askvar('num', raw=True, len_barrier=[2, 2])

a = int(num[0])
b = int(num[1])

if a > b:
    print(a - b)
elif a < b:
    print(a + b)
elif a == b:
    print(a * b)