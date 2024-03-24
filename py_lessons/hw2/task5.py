from askvar import askvar

a = askvar('a')
b = askvar('b')
c = askvar('c')

if (sum([a, b]) < c
        or sum([a, c]) < b
        or sum([b, c]) < a):
    print("Triangle doesn't exist")
else:
    print("Triangle does exist")