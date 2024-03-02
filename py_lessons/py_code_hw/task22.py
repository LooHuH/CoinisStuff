from askvar import askvar

N = askvar('pupils count')
Np2 = askvar('pupils on second page')
p1 = askvar('average points on first page')
p2 = askvar('average points on second page')

Np1 = N - Np2

point_sum_p1 = p1 * Np1
point_sum_p2 = p2 * Np2

average_of_all_pupils = round((point_sum_p1 + point_sum_p2) / N, 2)

print(f'Average point of all pupils - {average_of_all_pupils}')
