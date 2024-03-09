from askvar import askvar

a = askvar('a')
b = askvar('b')

sqrt_nums = []
for x in range(a, b + 1):
    if (x % 2 == 0
        and x % 4 != 0):
        sqrt_nums.append(x**2)

print(sum(sqrt_nums))