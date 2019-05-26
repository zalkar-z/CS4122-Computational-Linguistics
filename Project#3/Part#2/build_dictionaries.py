#!/usr/bin/env python3
#
# build_ngram_model.py - Computational Linguistics Project#3
# Author: Zak Ziiaidin uulu (zalkar@bennington.edu)
# Date Created: 05/25/2019
#


def build_bigram_dict(ngram_list, start, end):
    bigram_dict = {}

    for line in ngram_list[start + 1: end - 1]:
        current_list = line.split()

        first_word = current_list[3]
        second_word = current_list[4]
        probability = current_list[1]

        if first_word not in bigram_dict:
            bigram_dict[first_word] = {second_word: probability}
        else:
            bigram_dict[first_word][second_word] = probability

    return bigram_dict


def build_trigram_dict(ngram_list, start, end):
    trigram_dict = {1: 1}
    return trigram_dict
