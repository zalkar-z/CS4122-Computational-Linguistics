#!/usr/bin/env python3


dict = {'a': 1, 'b': 2, 'c': 2, 'd': 3}

dict = sorted(dict.items(), key=lambda x: x[1])


for item in dict:
    print(item[0], item[1])
