#!/usr/bin/env python3

import nltk


words = nltk.corpus.gutenberg.words('austen-emma.txt')
bigrams = nltk.bigrams(words)

print(bigrams)

