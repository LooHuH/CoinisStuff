from askvar import askvar

a = askvar('a')
b = askvar('b')
divisor = askvar('divisor')

divided_nums = []
for x in range(a + 1, b):
    if x % divisor == 0:
        divided_nums.append(x)

print(f'Sum of divided nums - {sum(divided_nums)}',
      f'Amount of divided nums - {len(divided_nums)}')