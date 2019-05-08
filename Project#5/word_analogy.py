#!/usr/bin/env python3

import sys
import os
#
# This is an examples of reading files from directory using sys and Python
#
# dir_name = sys.arg[1]
#
# for filename in os.listdir(dir_name):
#     # skip hidden files
#     if filename.startswith('.'):
#         continue
#     # skip everything NOT .txt
#     if not filename.endswith('.txt'):
#         continue
#
#     # join directory path with file path to get the whole address
#     file_path = os.path.join(dir_name, filename)
#
#     # read from file
#     with open(file_path, 'r') as open_file:
#         for line in open_file.readlines():
#             print(line)

# command line readings
# vector_file = sys.argv[1]
# input_directory = sys.argv[2]
# output_directory = sys.argv[3]
# eval_file = sys.argv[4]
# should_normalize = sys.argv[5]
# similarity_type = sys.argv[6]

vector_file = "smaller_model.txt"
vector_file_size = 773  # number of words in smaller_model.txt

vectors = []

with open(vector_file, 'r') as open_file:
    for line in open_file.readlines():
        # splits a string by whitespaces and converts to a list
        temp_list = line.split()
        # save the first one as word
        vector_word = temp_list[0]
        # the rest is list of vector
        vector_list = temp_list[1:]
        # append to a global list of vector dictionaries
        vectors.append({vector_word: vector_list})
        break


