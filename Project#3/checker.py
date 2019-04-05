#!/usr/bin/env python3
#


first = "output_test.txt"
second = "Examples/dickens_model.txt"

with open(first, 'r', encoding="utf8") as first_text:
    with open(second, 'r', encoding="utf8") as second_text:
        text1 = first_text.readlines()
        text2 = second_text.readlines()

        for i in range(len(text1)):
            if text1[i] != text2[i]:
                print(text1[i], " -- ", text2[i])


