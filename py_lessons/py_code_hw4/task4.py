from functools import reduce


l = ["Hello, World!", "Python is cool", "Functional programming rocks"]

word_count = lambda sentence: len(sentence.split())
l_words_count = list(map(word_count, l))

sum_attr = lambda a, b: a + b
l_words_count_sum = reduce(sum_attr, l_words_count)
print(l_words_count_sum)