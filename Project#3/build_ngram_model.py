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


class Ngram:
    def __init__(self, count, probability, log_probability, ngram):
        self.count = count
        self.probability = probability
        self.log_probability = log_probability
        self.ngram = ngram


class Unigram:
    def __init__(self, words):
        self.dict = {}
        self.tokens = 0

        # fill the dictionary with unigrams
        for line in words:
            for word in line:
                self.tokens += 1
                if word in self.dict:
                    self.dict[word] += 1
                else:
                    self.dict[word] = 1

        self.types = len(self.dict)
        self.sorted_list = []

        for unigram in self.dict:
            self.sorted_list.append(Ngram(self.dict[unigram], self.dict[unigram] / self.tokens,
                                          math.log10(self.dict[unigram] / self.tokens), unigram))

        self.sorted_list = sorted(self.sorted_list, key=lambda x: (-x.count,
                                                                   -x.probability, x.ngram, -x.log_probability))

    def write_to_file(self, output_text):
        output_text.write("\n")
        output_text.write("\\1-grams:\n")

        for unigram in self.sorted_list:
            output_text.write(str(unigram.count) + ' ' + str(unigram.probability) + ' ' + str(unigram.log_probability) + ' ' + str(unigram.ngram) + '\n')

    def count(self, unigram):
        return self.dict[unigram]


class Bigram:
    def __init__(self, words):
        self.dict = {}
        self.tokens = 0

        # fill the dictionary with unigrams
        for line in words:
            for i in range(1, len(line)):
                first_word = line[i - 1]
                second_word = line[i]

                if first_word not in self.dict:
                    self.dict[first_word] = {}
                    self.dict[first_word][second_word] = 1
                else:
                    if second_word not in self.dict[first_word]:
                        self.dict[first_word][second_word] = 1
                    else:
                        self.dict[first_word][second_word] += 1

        self.types = len(self.dict)
        self.sorted_list = []

        for unigram in self.dict:
            self.sorted_list.append(Ngram(self.dict[unigram], self.dict[unigram] / self.tokens,
                                          math.log10(self.dict[unigram] / self.tokens), unigram))

        self.sorted_list = sorted(self.sorted_list, key=lambda x: (-x.count,
                                                                   -x.probability, x.ngram, -x.log_probability))

    def write_to_file(self, output_text):
        output_text.write("\n")
        output_text.write("\\1-grams:\n")

        for unigram in self.sorted_list:
            output_text.write(str(unigram.count) + ' ' + str(unigram.probability) + ' ' + str(unigram.log_probability) + ' ' + str(unigram.ngram) + '\n')

    def count(self, unigram):
        return self.dict[unigram]

#
# def count_bigrams(words):
#     bigrams_nested = {}
#
#     for line in words:
#         for i in range(1, len(line)):
#             first_word = line[i - 1]
#             second_word = line[i]
#
#             if first_word not in bigrams_nested:
#                 bigrams_nested[first_word] = {}
#                 bigrams_nested[first_word][second_word] = 1
#             else:
#                 if second_word not in bigrams_nested[first_word]:
#                     bigrams_nested[first_word][second_word] = 1
#                 else:
#                     bigrams_nested[first_word][second_word] += 1
#
#     bigrams = {}
#
#     for first in bigrams_nested:
#         for second in bigrams_nested[first]:
#             current_bigram = first + ' ' + second
#             bigrams[current_bigram] = bigrams_nested[first][second]
#
#     bigrams = sorted(bigrams.items(), key=lambda x: (-x[1], x[0]))
#
#     return bigrams
#
#
# def count_trigrams(words):
#     trigrams_nested = {}
#
#     for line in words:
#         for i in range(2, len(line)):
#             first_word = line[i - 2]
#             second_word = line[i - 1]
#             third_word = line[i]
#
#             if first_word not in trigrams_nested:
#                 trigrams_nested[first_word] = {}
#                 trigrams_nested[first_word][second_word] = {}
#                 trigrams_nested[first_word][second_word][third_word] = 1
#             else:
#                 if second_word not in trigrams_nested[first_word]:
#                     trigrams_nested[first_word][second_word] = {}
#                     trigrams_nested[first_word][second_word][third_word] = 1
#                 else:
#                     if third_word not in trigrams_nested[first_word][second_word]:
#                         trigrams_nested[first_word][second_word][third_word] = 1
#                     else:
#                         trigrams_nested[first_word][second_word][third_word] += 1
#
#     trigrams = {}
#
#     for first in trigrams_nested:
#         for second in trigrams_nested[first]:
#             for third in trigrams_nested[first][second]:
#                 current_trigram = first + ' ' + second + ' ' + third
#                 trigrams[current_trigram] = trigrams_nested[first][second][third]
#
#     trigrams = sorted(trigrams.items(), key=lambda x: (-x[1], x[0]))
#
#     return trigrams


def main():
    with open(input_file, 'r', encoding="utf8") as input_text:
        with open(output_file, 'w', encoding="utf8") as output_text:
            words = input_text.readlines()

            for i in range(len(words)):
                words[i] = words[i].lower()
                words[i] = "<s> " + words[i] + " </s>"
                words[i] = words[i].split()

            unigrams = Unigram(words)
            unigrams.write_to_file(output_text)


            # # process unigrams
            # unigrams = count_unigrams(words)
            #
            # # process bigrams
            # bigrams = count_bigrams(words)
            #
            # # process trigrams
            # trigrams = count_trigrams(words)
            #
            # # write header data
            # output_text.write("\data\\\n")
            # output_text.write("ngram 1: type=" + str(unigrams_type) + " token=" + str(unigrams_token) + "\n")
            # output_text.write("ngram 2: type=" + str(bigrams_type) + " token=" + str(bigrams_token) + "\n")
            # output_text.write("ngram 3: type=" + str(trigrams_type) + " token=" + str(trigrams_token) + "\n")
            #
            # # write results
            # write_results(output_text, "\\1-grams:\n", unigrams, unigrams_token)
            # write_results(output_text, "\\2-grams:\n", bigrams, bigrams_token)
            # write_results(output_text, "\\3-grams:\n", trigrams, trigrams_token)


if __name__ == "__main__":
    main()






