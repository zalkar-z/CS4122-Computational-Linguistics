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

vector_file = "files/smaller_model.txt"

with open(vector_file, 'r') as open_file:
    for line in open_file.readlines():
        print(line)

