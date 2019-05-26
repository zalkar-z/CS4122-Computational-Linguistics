#!/usr/bin/env python3
#
# build_ngram_model.py - Computational Linguistics Project#3
# Author: Zak Ziiaidin uulu (zalkar@bennington.edu)
# Date Created: 05/25/2019
#

import sys
import random
from build_dictionaries import build_bigram_dict, build_trigram_dict

# input_file = sys.argv[1]
# output_file = sys.argv[2]

# temporary alternative
input_f = "input.txt"
output_f = "output.txt"


def main():
    # convert an input to a list of strings, line by line
    with open(input_f, 'r', encoding="utf8") as input_file:
        ngrams = input_file.read().splitlines() # reads the whole file and splits it into distinct lines in string form

    # getting the starting positions of each ngram type
    unigram_index = ngrams.index('\\1-grams:')
    bigram_index = ngrams.index('\\2-grams:')
    trigram_index = ngrams.index('\\3-grams:')

    # building bigram and trigram dictionaries
    bigram_dict = build_bigram_dict(ngrams, unigram_index, bigram_index)
    trigram_dict = build_trigram_dict(ngrams, bigram_index, trigram_index)


if __name__ == "__main__":
    main()