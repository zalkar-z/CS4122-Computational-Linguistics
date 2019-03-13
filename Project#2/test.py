#!/usr/bin/env python3

# japanese_tokenizer.py - Computational Linguistics Project#2
# Author: Zalkar Ziiaidin uulu (zalkar@bennington.edu)
# Date Created: 03/11/2019


japanese_dictionary = "japanese_wordlist.txt"
dictionary_out = "dictionary_out.txt"

with open(japanese_dictionary, 'r', encoding="utf8") as open_dictionary:
    with open(dictionary_out, 'w', encoding="utf8") as open_out_dictionary:

        text = open_dictionary.readlines()

        newlist = []

        for line in text:
            newlist.append(line[:len(line) - 1])

        print('ｐＨ調整剤' in (newlist))

        for line in newlist:
            open_out_dictionary.write(line + "\n")
