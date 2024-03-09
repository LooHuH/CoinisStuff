from askvar import askvar

year = askvar('year')

year_is_leap = False
if year % 400 == 0:
    year_is_leap = True
elif year % 100 == 0:
    year_is_leap = False
elif year % 4 == 0:
    year_is_leap = True
else:
    year_is_leap = False
    
if year_is_leap:
    print('year is leap')
else:
    print('year is not leap')