from askvar import askvar

temp = askvar('temp')

if temp <= 0:
    print('solid')
elif 0 < temp < 100:
    print('liquid')
else:
    print('gas')