import re

def task1(text_in, letter_in):
    sentences = re.split(r'[.!?]', text_in)[:-1]
    
    output = []
    for sentence in sentences:
        words_list = sentence.split()
        right_words = []
        for word in words_list:
            if word.endswith(letter_in):
                right_words.append(word)
        right_words.append(len(right_words))
        output.append(tuple(right_words))
    print(output)


task1('Print only the words that end with the chosen letter in those sentences. Example can contains one or more sentences.', 
      's')
