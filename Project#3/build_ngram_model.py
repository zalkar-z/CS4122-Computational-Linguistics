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


def count_unigrams(words):
    unigrams = {}

    for line in words:
        for word in line:
            if word in unigrams:
                unigrams[word] += 1
            else:
                unigrams[word] = 1

    return unigrams


with open(input_file, 'r', encoding="utf8") as input_text:
    with open(output_file, 'w', encoding="utf8") as output_text:
        words = input_text.readlines()

        # words = words[:50]
        for i in range(len(words)):
            words[i] = words[i].lower()
            words[i] = "<s> " + words[i] + " </s>"
            words[i] = words[i].split()

        unigrams = count_unigrams(words)

        unigrams_type = len(unigrams)
        unigrams_token = 0
        for word in unigrams:
            unigrams_token += unigrams[word]

        unigrams = sorted(unigrams.items(), key=lambda x: x[1], reverse=True)

        for item in unigrams:
            result = str(item[1]) + " " + str(item[1] / unigrams_token) + " " + str(math.log10(item[1] / unigrams_token)) + " " + str(item[0] + "\n")
            output_text.write(result)

