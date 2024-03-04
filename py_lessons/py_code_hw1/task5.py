from askvar import askvar

d_mm = askvar('d')
s_mm = askvar('s')

d_cm = d_mm / 10
s_cm = s_mm / 10

S = d_cm * s_cm

print(f'S = {S}')
