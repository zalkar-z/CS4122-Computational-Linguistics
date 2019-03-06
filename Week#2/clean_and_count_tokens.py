#!/usr/bin/env python3
#
# HW2.py - Computational Linguistics HW#2
# Author: Zalkar Ziiaidin uulu (zalkar@bennington.edu)
# Date Created: 03/02/2019
#

import re

file_name = "test_in.xml"
out_file_name = "test_out.txt"

with open(file_name, 'r') as open_text:
    with open(out_file_name, 'w') as open_out_text:
        text = open_text.read()

        # Matches all alphabetic strings that are at least 4 characters long and start with ‘sh’
        # text = regex.sub(r'\bsh[a-zA-Z][a-zA-Z]+\b', r'RIGHT!', text)

        p = re.compile(r'\d+')
        p.findall(text)

        print(len(text))

        print(text)
