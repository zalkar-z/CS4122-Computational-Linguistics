#!/usr/bin/env python3
#
# build_ngram_model.py - Computational Linguistics Project#3
# Author: Zak Ziiaidin uulu (zalkar@bennington.edu)
# Date Created: 05/25/2019
#

import sys
import random
from build_dictionaries import build_bigram_dict, build_trigram_dict, build_unigram_dict

input_f = sys.argv[1]
output_f = sys.argv[2]


def get_random_word(dict):
    sum = 0
    random_number = random.random()

    for word in dict:
        sum += dict[word]

        if sum > random_number:
            return word


def generate_unigrams(unigram_dict, number_of_sentences):
    result = ''

    for i in range(number_of_sentences):
        current_sentence = '<s>'

        while True:
            current_bigram = get_random_word(unigram_dict)

            if current_bigram == '<s>':
                continue

            current_sentence += ' ' + current_bigram

            if current_bigram == '</s>':
                break

        result += (current_sentence + '\n')

    return result


def generate_bigrams(bigram_dict, number_of_sentences):
    result = ''

    for i in range(number_of_sentences):
        current_sentence = '<s>'
        last_word = '<s>'

        while True:
            current_word = get_random_word(bigram_dict[last_word])

            if current_word == '<s>':
                continue

            current_sentence += ' ' + current_word
            last_word = current_word

            if current_word == '</s>':
                break

        result += (current_sentence + '\n')

    return result


def generate_trigrams(trigram_dict, bigram_dict, number_of_sentences):
    result = ''

    for i in range(number_of_sentences):
        current_sentence = '<s>'
        first_word = '<s>'
        second_word = ''

        # initializing the first bigram to start with
        while True:
            current_word = get_random_word(bigram_dict['<s>'])
            if current_word == '<s>' or current_word == '</s>':
                continue
            else:
                current_sentence += ' ' + current_word
                second_word = current_word
                break

        while True:
            current_word = get_random_word(trigram_dict[first_word + ' ' + second_word])

            if current_word == '<s>':
                continue

            current_sentence += ' ' + current_word
            first_word = second_word
            second_word = current_word

            if current_word == '</s>':
                break

        result += (current_sentence + '\n')

    return result


def main():
    # convert an input to a list of strings, line by line
    with open(input_f, 'r', encoding='utf8') as input_file:
        ngrams = input_file.read().splitlines() # reads the whole file and splits it into distinct lines in string form

    # getting the starting positions of each ngram type
    unigram_index = ngrams.index('\\1-grams:')
    bigram_index = ngrams.index('\\2-grams:')
    trigram_index = ngrams.index('\\3-grams:')

    # building dictionaries for all ngrams
    unigram_dict = build_unigram_dict(ngrams, unigram_index, bigram_index)
    bigram_dict = build_bigram_dict(ngrams, bigram_index, trigram_index)
    trigram_dict = build_trigram_dict(ngrams, trigram_index, len(ngrams) - 1)

    with open(output_f, 'w', encoding='utf8') as output_file:
        # writing generated unigrams
        output_file.write('Unigrams - 5 Randomly Generated Sentences \n\n')
        output_file.write(generate_unigrams(unigram_dict, 5))
        output_file.write('\n')

        # writing generated bigrams
        output_file.write('Bigrams - 5 Randomly Generated Sentences \n\n')
        output_file.write(generate_bigrams(bigram_dict, 5))
        output_file.write('\n')

        # writing generated trigrams
        output_file.write('Trigram - 5 Randomly Generated Sentences \n\n')
        output_file.write(generate_trigrams(trigram_dict, bigram_dict, 5))
        output_file.write('\n')


if __name__ == "__main__":
    main()