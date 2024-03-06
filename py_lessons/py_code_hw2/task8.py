from askvar import askvar

number_of_points = askvar('number of points', num_barrier=[1, 25])
custom_range = range(number_of_points)
all_points = [askvar(f'points ({x + 1}/{len(custom_range)})', num_barrier=[1, 5]) for x in custom_range]

if 1 in all_points:
    average_points = 1
else:
    average_points = sum(all_points) / len(all_points)

if average_points >= 4.5:
    print(f'{average_points} - Excellent')
elif average_points >= 3.5:
    print(f'{average_points} - Very good')
elif average_points >= 2.5:
    print(f'{average_points} - Good')
elif average_points >= 2:
    print(f'{average_points} - Sufficient')
else:
    print(f'{average_points} - Insufficient')
