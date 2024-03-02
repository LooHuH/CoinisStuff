from askvar import askvar

lit_per_hour = 0.5
hours = askvar('km')

liters = hours//1 * lit_per_hour

print(f'time = {hours} ----> liters = {liters}')
