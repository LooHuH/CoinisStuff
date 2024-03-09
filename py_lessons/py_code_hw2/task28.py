from askvar import askvar

text = askvar('text', raw=True)
target = askvar('target text', raw=True)

if text.endswith(target):
    print('Yes')
else:
    print('No')