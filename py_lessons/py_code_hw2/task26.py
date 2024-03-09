from askvar import askvar

num = askvar('num', raw=True)

prefix = num[:2]

if prefix == '0b':
    print('Num is binary')
elif prefix == '0o':
    print('Num is octal')
elif prefix == '0x':
    print('Num is hexadecimal')
else:
    print('Num is decimal')