#!/usr/bin/env python3
#
# HW1.py - Computational Linguistics HW#1
# Author: Zalkar Ziiaidin uulu (zalkar@bennington.edu)
# Date Created: 02/23/2019
#

import regex

file_name = "HW1.txt"
out_file_name = "HW1-out.txt"

with open(file_name, 'r') as open_text:
    with open(out_file_name, 'w') as open_out_text:
        text = open_text.read()

        # Matches all alphabetic strings that are at least 4 characters long and start with ‘sh’
        text = regex.sub(r'\bsh[a-zA-Z][a-zA-Z]+\b', r'RIGHT!', text)

        # Matches all strings with two consecutive repeated words
        text = regex.sub(r'(\b\w+\b)(\W+\1\b)', r'RIGHT!', text)

        # Matches the set of strings made up of ‘a’ and ‘b’ where each ‘a’ has a ‘b’ before and after it.
        text = regex.sub(r'\b[b]+a[b]+\b', r'RIGHT!', text)

        # Matches all strings that start at the beginning of a line with an integer, and end the line with a word
        text = regex.sub(r'^[0-9]+.*[a-zA-Z]+$', r'RIGHT!', text)

        # Matches all American phone numbers in many different configurations
        text = regex.sub(r'\b\+?((\d{3}(-|\.).+)|1\s\d{3}\s|1\(\d{3}\).+|\d{10}\b)', r'RIGHT!', text)

        open_out_text.write(text)