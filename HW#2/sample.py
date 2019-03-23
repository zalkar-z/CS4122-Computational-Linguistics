#!/usr/bin/env python3

import nltk

words = nltk.corpus.gutenberg.words('austen-emma.txt')
bigrams = nltk.bigrams(words)


def count_bigrams(bigrams_list):

    word_dictionary = {}

    for current_tuple in bigrams_list:
        first_word = current_tuple[0]
        second_word = current_tuple[1]

        if first_word not in word_dictionary:
            word_dictionary[first_word] = {}
            word_dictionary[first_word][second_word] = 1
        else:
            if second_word not in word_dictionary[first_word]:
                word_dictionary[first_word][second_word] = 1
            else:
                word_dictionary[first_word][second_word] += 1

    return word_dictionary


if __name__ == "__main__":
    # sample_list = [('The', 'cat'), ('The', 'cat'), ('The', 'cat'), ('cat', 'The'), ('car', 'car'), ('The', 'car')]
    # result = count_bigrams(sample_list)
    #
    # print(result)
    #
    # for first in result:
    #     for second in result[first]:
    #         print(first, " ", second)

    cfd = nltk.ConditionalFreqDist(bigrams)

    my_list = ['a', 'the', 'she', 'he', 'they']

    for word in my_list:
        print(word, ' ', cfd[word].max())


    # 1 - probability count
    # 2 - count the most common word to follow
    # 3 - play around with functions

    # 0.0085
    # 0.107
