#!/usr/bin/env python3
#
# HW2.py - Computational Linguistics HW#2
# Author: Zalkar Ziiaidin uulu (zalkar@bennington.edu)
# Date Created: 03/02/2019
#

import re
import operator

first = "test_out.txt"
second = "sample_out.txt"

with open(first, 'r') as first_text:
    with open(second, 'r') as second_text:
        text1 = first_text.read().lower()
        text2 = second_text.read().lower()

        text1 = re.sub(r'\s*', '', text1)
        text2 = re.sub(r'\s*', '', text2)

        if text1 == text2:
            print("The are identical! Great job! Go fucking home now!")
        else:
            print("Some fixes needed")


