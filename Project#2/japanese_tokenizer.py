#!/usr/bin/env python3
#
# japanese_tokenizer.py - Computational Linguistics Project#2
# Author: Zalkar Ziiaidin uulu (zalkar@bennington.edu)
# Date Created: 03/11/2019
#

# import sys
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
#
#
# def tokenize(line):
#
#
#
# with open(input_file, 'r') as open_in:
#     with open(output_file, 'w') as open_out:
#         for line in open_in.readlines():
#             spaced_line = tokenize(line)
#             open_out.write(spaced_line)


japanese_dictionary = "japanese_wordlist.txt"

with open(japanese_dictionary, 'r') as open_dictionary:

    dictionary = open_dictionary.readlines()

    print(dictionary)


# Notes
#
# In the input file, treat each line as a seperate input
#
# Print different lines to the output file
#
# in the japanese dictionary, each lines is a unique word


# Preliminary Solution:
#
# 1) Read the input file line by line (remember that each line is seperate)
# 2) Using the greedy MaxMatch algorithm try to find the longest existing word
# (check from japanese_wordlist.txt, you can just import it as a variable)
# and keep seperating words by black line as needed
# 3) Print everything out
# 4) Make a tester to analyze the effectiveness of the tokenizer
# (hom many lines match, what is the difference in characters, etc)
# string_looking_for.in(dictionary)

# the program should be able to run on the Python console "./nameof_file in.txt out.txt"
# library sys
# sys.arg[1] - in
# sys.artv[2] - out
# check out the Thai sample code

