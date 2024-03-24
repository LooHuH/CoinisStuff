from askvar import askvar

r1 = askvar('table 1 radius')
r2 = askvar('table 2 radius')

pi = 3.14

S1 = pi * r1**2
S2 = pi * r2**2

if S1 > S2:
    print(round(2*pi*r1, 2))
elif S2 > S1:
    print(round(2*pi*r2, 2))
else:
    print('circles are the same')