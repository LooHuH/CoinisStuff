from askvar import askvar

var = askvar('number', len_barrier=[6, 6], raw=True)

a = int(var[0])
b = int(var[1])
c = int(var[2])
d = int(var[3])
e = int(var[4])
f = int(var[5])

sqr_of_sum = sum(int(x) for x in var)**2
third_times_fourth_nums = c * d

ans = sqr_of_sum - third_times_fourth_nums

print(f'Answer - {ans}')
