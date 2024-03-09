from askvar import askvar

text = askvar('text', raw=True)

vovewls = False
for x in 'euioa':
    if x in text:
        print('text has vowels')
        vovewls = True
        break
if not vovewls:
    print('text has not vowels')