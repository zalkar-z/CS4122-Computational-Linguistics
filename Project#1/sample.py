!/usr/bin/env python3

import nltk


words = nltk.corpus.gutenberg.words('austen-emma.txt')
bigrams = nltk.bigrams(words)


def count_bigrams(bigrams_list):

    word_dictionary = {}

    for current_tuple in bigrams_list:
        first_word = current_tuple[0]
        second_word = current_tuple[1]

        if first_word in word_dictionary:




if __name__ == "__main__":
    sample_list = [('The', 'cat'), ('The', 'cat')]
    # print(count_bigrams(sample_list))

    for word in sample_list:
        print(word[1])

sample_dict = {'the': {'': 0}}

if 'the' in sample_dict:
    if 'cat' not in sample_dict['the']:
        sample_dict['the']['cat'] = 1

sample_dict['the']['cat'] += 1
sample_dict['the']['cat'] += 1
sample_dict['the']['cat'] += 1

print(sample_dict)

# 1 - probability count
# 2 - count the most common word to follow
# 3 - play around with functions