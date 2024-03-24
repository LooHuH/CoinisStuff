from askvar import askvar

price_per_km = 0.5
km = askvar('km')

price = 1 + km * price_per_km

print(f'km = {km} ----> price = {price}')
