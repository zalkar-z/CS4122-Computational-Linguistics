#!/usr/bin/env python3
#
# HW2.py - Computational Linguistics Project#1
# Author: Zalkar Ziiaidin uulu (zalkar@bennington.edu)
# Date Created: 03/02/2019
#

import nltk
import re

# nltk.download('punkt')

file_name = "Wikipedia-LexicalAnalysis.xml"
out_file_name = "lexical_analysis_nltk_stemmed_out.txt"

frequency = {}

with open(file_name, 'r') as open_text:
    with open(out_file_name, 'w') as open_out_text:
        text = open_text.read().lower()

        # regex substitute for tags
        text = re.sub(r'</.+>|<.+">|<\w+>|<.+/>', '', text)

        # regex substitute for tags in .xml &lt; and &gt;
        text = re.sub(r'(&lt;|&gt;|<)/.+(&lt;|&gt;|>)|(&lt;|&gt;|<).+"(&lt;|&gt;|>)|(&lt;|&gt;|<)\w+(&lt;|&gt;|>)|(&lt;|&gt;|<).+/(&lt;|&gt;|>)', '', text)

        # regex substitute for double and triple single apostrophes (quotes)
        text = re.sub(r'[\']{2,3}', '', text)

        # regex substitute for end points (full stops at the end or beginning of the word)
        text = re.sub(r'\.\W|\W\.', ' ', text)

        # NLTK tokenization
        text = nltk.word_tokenize(text)

        # Porter Stemmer
        porter = nltk.PorterStemmer()
        for i in range(len(text)):
            text[i] = porter.stem(text[i])

        # converts arrays of strings to a string
        text = ' '.join(text)

        # get all three types of apostrophes and the rest of words
        match_pattern = re.findall(r'[\']?[a-z\.]+[\']?[a-z\.]*[\']?', text)

        # iterates through the array and writes # of occurrences in a dictionary
        for word in match_pattern:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1

        # sorts in increasing order based on words frequency, doesn't handle alphabetic comparison
        sorted_array = sorted(frequency, key=lambda word: frequency[word])

        # complementary cycle to deal with ties and alphabetic comparison
        # O(n^2) sorting used here due to the small input. Could be optimized to O(NlogN) if needed.
        for i in range(len(sorted_array)):
            for j in range(i+1, len(sorted_array)):
                if frequency[sorted_array[i]] == frequency[sorted_array[j]] and sorted_array[i] < sorted_array[j]:
                    sorted_array[i], sorted_array[j] = sorted_array[j], sorted_array[i]

        result = ""

        # iterates through a reversed array and collects results
        for i in reversed(range(len(sorted_array))):
            result = result + sorted_array[i] + "\t" + str(frequency[sorted_array[i]]) + "\n"

        # write the result
        open_out_text.write(result)
