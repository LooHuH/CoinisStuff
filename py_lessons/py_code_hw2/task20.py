from askvar import askvar

num = askvar('num', len_barrier=[4, 4], raw=True)

if int(num) % 2 == 0:
    num_sum = 0
    for x in num:
        if int(x) % 2 == 0:
            num_sum += int(x)
    print(f'Sum of even - {num_sum}')
else:
    num_multiply = 1
    for x in num:
        if int(x) % 2 != 0:
            num_multiply *= int(x)
    print(f'Multiply of uneven - {num_multiply}')