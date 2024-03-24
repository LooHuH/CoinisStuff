from askvar import askvar

text = askvar('any text you want', raw=True)

new_text = text[1:-1]

print(new_text)