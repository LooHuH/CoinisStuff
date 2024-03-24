from askvar import askvar

num = askvar('num')
num = str(num)
      
out = 1
for x in num:  
    out *= int(x)
print(out)