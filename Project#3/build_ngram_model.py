#!/usr/bin/env python3
#
# build_ngram_model.py - Computational Linguistics Project#3
# Author: Zak Ziiaidin uulu (zalkar@bennington.edu)
# Date Created: 04/01/2019
#

import sys
import math

# input_file = sys.argv[1]
# output_file = sys.argv[2]

input_file = "InputTexts/dickens_training.txt"
output_file = "output_test.txt"


unigrams_type = 0
unigrams_token = 0
bigrams_token = 0
bigrams_type = 0
trigrams_token = 0
trigrams_type = 0


class Ngram:
    def __init__(self, count, probability, ngram):
        self.count = count
        self.probability = probability
        self.ngram = ngram


def count_unigrams(words):
    unigrams = {}

    for line in words:
        for word in line:
            if word in unigrams:
                unigrams[word] += 1
            else:
                unigrams[word] = 1

    unigrams = sorted(unigrams.items(), key=lambda x: (-x[1], x[0]))

    return unigrams


def count_bigrams(words):
    bigrams_nested = {}

    for line in words:
        for i in range(1, len(line)):
            first_word = line[i - 1]
            second_word = line[i]

            if first_word not in bigrams_nested:
                bigrams_nested[first_word] = {}
                bigrams_nested[first_word][second_word] = 1
            else:
                if second_word not in bigrams_nested[first_word]:
                    bigrams_nested[first_word][second_word] = 1
                else:
                    bigrams_nested[first_word][second_word] += 1

    bigrams = {}

    for first in bigrams_nested:
        for second in bigrams_nested[first]:
            current_bigram = first + ' ' + second
            bigrams[current_bigram] = bigrams_nested[first][second]

    bigrams = sorted(bigrams.items(), key=lambda x: (-x[1], x[0]))

    return bigrams


def count_trigrams(words):
    trigrams_nested = {}

    for line in words:
        for i in range(2, len(line)):
            first_word = line[i - 2]
            second_word = line[i - 1]
            third_word = line[i]

            if first_word not in trigrams_nested:
                trigrams_nested[first_word] = {}
                trigrams_nested[first_word][second_word] = {}
                trigrams_nested[first_word][second_word][third_word] = 1
            else:
                if second_word not in trigrams_nested[first_word]:
                    trigrams_nested[first_word][second_word] = {}
                    trigrams_nested[first_word][second_word][third_word] = 1
                else:
                    if third_word not in trigrams_nested[first_word][second_word]:
                        trigrams_nested[first_word][second_word][third_word] = 1
                    else:
                        trigrams_nested[first_word][second_word][third_word] += 1

    trigrams = {}

    for first in trigrams_nested:
        for second in trigrams_nested[first]:
            for third in trigrams_nested[first][second]:
                current_trigram = first + ' ' + second + ' ' + third
                trigrams[current_trigram] = trigrams_nested[first][second][third]

    trigrams = sorted(trigrams.items(), key=lambda x: (-x[1], x[0]))

    return trigrams


def write_results(output_text, header, tuple_list, token):
    output_text.write("\n")
    output_text.write(header)

    for item in tuple_list:
        result = str(item[1]) + " " + str(item[1] / token) + " " + str(math.log10(item[1] / token)) \
                 + " " + str(item[0] + "\n")
        output_text.write(result)


def main():
    with open(input_file, 'r', encoding="utf8") as input_text:
        with open(output_file, 'w', encoding="utf8") as output_text:
            words = input_text.readlines()

            for i in range(len(words)):
                words[i] = words[i].lower()
                words[i] = "<s> " + words[i] + " </s>"
                words[i] = words[i].split()

            # process unigrams
            unigrams = count_unigrams(words)

            # process bigrams
            bigrams = count_bigrams(words)

            # process trigrams
            trigrams = count_trigrams(words)

            # write header data
            output_text.write("\data\\\n")
            output_text.write("ngram 1: type=" + str(unigrams_type) + " token=" + str(unigrams_token) + "\n")
            output_text.write("ngram 2: type=" + str(bigrams_type) + " token=" + str(bigrams_token) + "\n")
            output_text.write("ngram 3: type=" + str(trigrams_type) + " token=" + str(trigrams_token) + "\n")

            # write results
            write_results(output_text, "\\1-grams:\n", unigrams, unigrams_token)
            write_results(output_text, "\\2-grams:\n", bigrams, bigrams_token)
            write_results(output_text, "\\3-grams:\n", trigrams, trigrams_token)


if __name__ == "__main__":
    main()






