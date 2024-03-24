from askvar import askvar

text = askvar('text', raw=True)

binary = True
for x in '0', '1':
    if not x in text:
        print('it is not binary')
        binary = False
if binary:
    print('num is binary')