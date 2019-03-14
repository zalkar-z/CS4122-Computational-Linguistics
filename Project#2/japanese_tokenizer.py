#!/usr/bin/env python3
#
# japanese_tokenizer.py - Computational Linguistics Project#2
# Author: Zalkar Ziiaidin uulu (zalkar@bennington.edu)
# Date Created: 03/11/2019
#

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]


# imports "japanese_wordlist.txt" file
japanese_dictionary_file = "japanese_wordlist.txt"

# reads the dictionary and converts it to list
with open(japanese_dictionary_file, 'r', encoding="utf8") as open_dictionary:
    dictionary = open_dictionary.readlines()
    for i in range(len(dictionary)):
        # deletes the "\n" - end of line character
        dictionary[i] = dictionary[i][:len(dictionary[i]) - 1]


# boolean function to check if the word is in the dictionary
def exists_in_dictionary(word):
    return word in dictionary


def tokenize(line):
    start = 0
    result = ""

    # MaxMatch algorithms implementation
    while start < len(line):
        for end in range(len(line), start, -1):
            # if just one char left, makes sure it is not a whitespace and adds to the result
            if end == start + 1:
                if line[start:end] != " " and line[start:end] != "\n":
                    result += line[start:end] + " "
                start = start + 1
                break
            # if a particular substring is in the dictionary, adds it to the result
            elif exists_in_dictionary(line[start:end]):
                result += line[start:end] + " "
                start = end
                break

    # Deletes an end of line symbol or a space
    result = result[0:len(result) - 1]

    return result + "\n"


with open(input_file, 'r', encoding="utf8") as open_in:
    with open(output_file, 'w', encoding="utf8") as open_out:
        for current_line in open_in.readlines():
            spaced_line = tokenize(current_line)
            open_out.write(spaced_line)


