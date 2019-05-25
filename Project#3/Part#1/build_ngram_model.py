#!/usr/bin/env python3
#
# build_ngram_model.py - Computational Linguistics Project#3
# Author: Zak Ziiaidin uulu (zalkar@bennington.edu)
# Date Created: 04/01/2019
#

import sys
import math

input_file = sys.argv[1]
output_file = sys.argv[2]


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

        # count types of unigrams
        self.types = len(self.dict)
        self.sorted_list = []

    # counts probabilities and collects them in a sorted list
    def count_probability(self):

        for unigram in self.dict:
            self.sorted_list.append(Ngram(self.dict[unigram], self.dict[unigram] / self.tokens,
                                          math.log10(self.dict[unigram] / self.tokens), unigram))

        self.sorted_list = sorted(self.sorted_list, key=lambda x: (-x.count,
                                                                   x.ngram, -x.probability, -x.log_probability))

    # prints the sorted_list to the given output file
    def write_to_file(self, output_text):
        output_text.write("\n")
        output_text.write("\\1-grams:\n")

        for unigram in self.sorted_list:
            output_text.write(str(unigram.count) + ' ' + str(unigram.probability) + ' ' + str(unigram.log_probability)
                              + ' ' + str(unigram.ngram) + '\n')

    # returns the count of given unigram
    def count(self, unigram):
        return self.dict[unigram]


class Bigram:
    def __init__(self, words):
        self.dict = {}
        self.tokens = 0

        # fill the dictionary with bigrams
        for line in words:
            for i in range(1, len(line)):
                self.tokens += 1
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

        # count types of bigrams
        self.types = 0

        for first_word in self.dict:
            self.types += len(self.dict[first_word])

        self.sorted_list = []

    # counts probabilities and collects them in a sorted list
    def count_probability(self, unigram):

        for first_word in self.dict:
            for second_word in self.dict[first_word]:
                bigram_count =self.dict[first_word][second_word]
                probability = self.dict[first_word][second_word] / unigram.count(first_word)
                bigram = first_word + ' ' + second_word

                self.sorted_list.append(Ngram(bigram_count, probability, math.log10(probability), bigram))

        self.sorted_list = sorted(self.sorted_list, key=lambda x: (-x.count,
                                                                   x.ngram, -x.probability, -x.log_probability))

    # prints the sorted_list to the given output file
    def write_to_file(self, output_text):
        output_text.write("\n")
        output_text.write("\\2-grams:\n")

        for bigram in self.sorted_list:
            output_text.write(str(bigram.count) + ' ' + str(bigram.probability) + ' ' + str(bigram.log_probability)
                              + ' ' + str(bigram.ngram) + '\n')

    # returns the count of given bigram
    def count(self, first_word, second_word):
        return self.dict[first_word][second_word]


class Trigram:
    def __init__(self, words):
        self.dict = {}
        self.tokens = 0

        # fill the dictionary with trigrams
        for line in words:
            for i in range(2, len(line)):
                self.tokens += 1
                first_word = line[i - 2]
                second_word = line[i - 1]
                third_word = line[i]

                if first_word not in self.dict:
                    self.dict[first_word] = {}
                    self.dict[first_word][second_word] = {}
                    self.dict[first_word][second_word][third_word] = 1
                else:
                    if second_word not in self.dict[first_word]:
                        self.dict[first_word][second_word] = {}
                        self.dict[first_word][second_word][third_word] = 1
                    else:
                        if third_word not in self.dict[first_word][second_word]:
                            self.dict[first_word][second_word][third_word] = 1
                        else:
                            self.dict[first_word][second_word][third_word] += 1

        # count types of trigrams
        self.types = 0
        for first_word in self.dict:
            for second_word in self.dict[first_word]:
                self.types += len(self.dict[first_word][second_word])

        self.sorted_list = []

    # counts probabilities and collects them in a sorted list
    def count_probability(self, bigram):

        for first_word in self.dict:
            for second_word in self.dict[first_word]:
                for third_word in self.dict[first_word][second_word]:

                    trigram_count = self.dict[first_word][second_word][third_word]
                    probability = self.dict[first_word][second_word][third_word] / bigram.count(first_word, second_word)
                    trigram = first_word + ' ' + second_word + ' ' + third_word

                    self.sorted_list.append(Ngram(trigram_count, probability, math.log10(probability), trigram))

        self.sorted_list = sorted(self.sorted_list, key=lambda x: (-x.count,
                                                                   x.ngram, -x.probability, -x.log_probability))

    # prints the sorted_list to the given output file
    def write_to_file(self, output_text):
        output_text.write("\n")
        output_text.write("\\3-grams:\n")

        for trigram in self.sorted_list:
            output_text.write(str(trigram.count) + ' ' + str(trigram.probability) + ' ' + str(trigram.log_probability)
                              + ' ' + str(trigram.ngram) + '\n')

    # returns the count of given trigram
    def count(self, first_word, second_word, third_word):
        return self.dict[first_word][second_word][third_word]


def print_results(output_text, ngram_list):
    # print header file first
    output_text.write("\\data\\")
    output_text.write("\n")
    for i in range(len(ngram_list)):
        output_text.write("ngram " + str(i + 1) + ": type=" + str(ngram_list[i].types)
                          + " token=" + str(ngram_list[i].tokens) + "\n")

    # print full list of ngrams
    for ngram in ngram_list:
        ngram.write_to_file(output_text)


def main():
    with open(input_file, 'r', encoding="utf8") as input_text:
        with open(output_file, 'w', encoding="utf8") as output_text:
            words = input_text.readlines()

            # add <s> and </s> and split by space
            for i in range(len(words)):
                words[i] = words[i].lower()
                words[i] = "<s> " + words[i] + " </s>"
                words[i] = words[i].split()

            # initialize and count unigrams
            unigrams = Unigram(words)
            unigrams.count_probability()

            # initialize and count bigrams
            bigrams = Bigram(words)
            bigrams.count_probability(unigrams)

            # initialize and count trigrams
            trigrams = Trigram(words)
            trigrams.count_probability(bigrams)

            # print all results
            print_results(output_text, [unigrams, bigrams, trigrams])


if __name__ == "__main__":
    main()






