#!/usr/bin/env python3
#


first = "ngram_output.txt"
second = "Examples/dickens_model.txt"

out = "check_out.txt"

with open(first, 'r', encoding="utf8") as first_text:
    with open(second, 'r', encoding="utf8") as second_text:
        with open(out, 'w', encoding="utf8") as out_text:
            text1 = first_text.readlines()
            text2 = second_text.readlines()

            identical = True

            for i in range(len(text1)):
                if text1[i] != text2[i]:
                    identical = False
                    out_text.write(text1[i] + text2[i] + "----\n")

            if identical:
                print("100% identical")
