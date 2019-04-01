#!/usr/bin/env python3
#
# build_ngram_model.py - Computational Linguistics Project#3
# Author: Zak Ziiaidin uulu (zalkar@bennington.edu)
# Date Created: 04/01/2019
#

import sys
import nltk

# input_file = sys.argv[1]
# output_file = sys.argv[2]

input_file = "InputTexts/dickens_training.txt"
output_file = "output_test.txt"

with open(input_file, 'r') as input_file:
    with open(output_file, 'w') as output_file:
        words = input_file.read()
        words = nltk.word_tokenize(words)
        words = [word.lower() for word in words]

        frequency = nltk.FreqDist(words)

        output_file.write(str(frequency.most_common(50)))





# bigrams = nltk.bigrams(words)
# for tuple in bigrams:
#     output_file.write(str(tuple))