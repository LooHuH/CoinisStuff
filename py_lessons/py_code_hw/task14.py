from askvar import askvar

print('Aparts dimensions')
d = askvar('d')
s = askvar('s')

print('Parking settings')
parking_exists = askvar('parking exists', num_barrier=[0, 1])
parking_zone = askvar('parking zone', num_barrier=[1, 3])

place_price = 1000
price_per_m2 = 1200

S = d * s
location = 5 * S
parking = 10 * location

match parking_zone:
    case 1:
        parking_multiplyer = 3
    case 2:
        parking_multiplyer = 2
    case 3:
        parking_multiplyer = 1

whole_price = (place_price
               + (S * price_per_m2)
               + location
               + (parking_exists * parking * parking_multiplyer))

print(f'Aparts price - {whole_price} e')
