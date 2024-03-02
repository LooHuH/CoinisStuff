from askvar import askvar

a = askvar('a')
b = askvar('b')
c = askvar('c')

# 𝑎^2 + 𝑏^2 + 𝑐^2 + 2𝑎𝑏 + 2𝑎𝑐 + 2𝑏c
ans = a**2 + b**2 + c**2 + 2*a*b + 2*a*c + 2*b*c

print(f'Answer = {ans}')
