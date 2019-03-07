#!/usr/bin/env python3
#
# HW2.py - Computational Linguistics HW#2
# Author: Zalkar Ziiaidin uulu (zalkar@bennington.edu)
# Date Created: 03/02/2019
#

import re

file_name = "test_in.xml"
out_file_name = "test-out.txt"

frequency = {}

with open(file_name, 'r') as open_text:
    with open(out_file_name, 'w') as open_out_text:
        text = open_text.read().lower()

        # eliminate <tags> before and substitude them with "" empty sting"
        match_pattern = re.findall(r'\b[a-z]+\b', text) #get the words you need

        for word in match_pattern:
            count = frequency.get(word, 0)
            frequency[word] = count + 1

        # sort your dictionary by values (decreasing order)
        # transfer integer to string and print it

        frequency_list = frequency.keys()

        for words in frequency_list:
            print(words, frequency[words])
