#!/usr/bin/env python3
#
# HW2.py - Computational Linguistics HW#2
# Author: Zalkar Ziiaidin uulu (zalkar@bennington.edu)
# Date Created: 03/02/2019
#

import re
import operator

file_name = "test_in.xml"
out_file_name = "test_out.txt"

frequency = {}

with open(file_name, 'r') as open_text:
    with open(out_file_name, 'w') as open_out_text:
        text = open_text.read().lower()

        text = re.sub(r'</.+>|<.+">|<\w+>|<.+/>', '', text)

        # \b[a-z]+\b|\b([a-z]+\'[a-z]+)\b|\b([a-z]+\')|(\'[a-z]+)\b -- for apostrophes

        open_out_text.write(text)

        # # eliminate <tags> before and substitude them with "" empty sting"
        # match_pattern = re.findall(r'\b[a-z]+\b', text) #get the words you need
        #
        # # iterates through the array and writes # of occurrences in a dictionary
        # for word in match_pattern:
        #     if word in frequency:
        #         frequency[word] += 1
        #     else:
        #         frequency[word] = 1
        #
        # # sorts in increasing order based on words frequency, doesn't handle alphabetic comparison
        # sorted_array = sorted(frequency, key=lambda word: frequency[word])
        #
        # # complementary cycle to deal with ties and alphabetic comparison
        # for i in range(len(sorted_array)):
        #     for j in range(i+1, len(sorted_array)):
        #         if frequency[sorted_array[i]] == frequency[sorted_array[j]] and sorted_array[i] < sorted_array[j]:
        #             sorted_array[i], sorted_array[j] = sorted_array[j], sorted_array[i]
        #
        # result = ""
        #
        # # iterates through a reversed array and collects results
        # for i in reversed(range(len(sorted_array))):
        #     result = result + sorted_array[i] + " " + str(frequency[sorted_array[i]]) + "\n"
        #
        # open_out_text.write(result)
