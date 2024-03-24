from askvar import askvar

num = askvar('num')
num = str(num)

num_sum = 0
evens = 0

num_multiply = 1
unevens = 0

for x in num:
    if int(x) % 2 == 0:
        num_sum += int(x)
        evens += 1
        
    else:
        num_multiply *= int(x)
        unevens += 1

print(f'Sum of evens - {num_sum}, amount - {evens}',
      f'Multiply of unevens - {num_multiply}, amount - {unevens}',
      sep='\n')
