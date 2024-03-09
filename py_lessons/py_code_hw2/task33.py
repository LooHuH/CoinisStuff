from askvar import askvar

num = askvar('num')
num = str(num)
summ = sum(int(x) for x in num)
print(summ)