#!/usr/bin/env python3

class Ngram:
    def __init__(self, count, probability, ngram):
        self.count = count
        self.probability = probability
        self.ngram = ngram


my_list = []

my_list.append(Ngram(2, 0.7, "C"))
my_list.append(Ngram(2, 0.7, "B"))
my_list.append(Ngram(3, 0.5, "A"))

my_list = sorted(my_list, key=lambda x: (-x.count, -x.probability, x.ngram))

for item in my_list:
    print(item.count, item.probability, item.ngram)
