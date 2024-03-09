text = input(' vvv Enter text vvv \n')

char_replace = '###'
for char in ['.', '!', '?']:
    text = text.replace(char, char_replace)
text_split = text.split(char_replace)
sentences = []
for x in text_split:
    if x != '':
        sentences.append(x)
    
print(f'Sentences - {len(sentences)}')
