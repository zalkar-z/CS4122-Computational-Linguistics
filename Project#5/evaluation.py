#!/usr/bin/env python3
#
# checker_directory.py - Computational Linguistics Project#5
# Author: Zak Ziiaidin uulu (zalkar@bennington.edu)
# Date Created: 05/09/2019
#

import os
from checker_file import compare_two_files

# input_directory = r'/Users/zalkar/Desktop/Computational_Linguistics/Project#5/GoogleTestSet' # mac
# input_directory = r'C:\Users\User\Desktop\Bennington College\term2\Computational_Linguistics\MyGitHub\Project#5\GoogleTestSet' # windows
# input_directory = r'/home/zalkar/Computational_Linguistics/Project#5/GoogleTestSet' # linux

# output_directory = r'/Users/zalkar/Desktop/Computational_Linguistics/Project#5/output' # mac
# output_directory = r'C:\Users\User\Desktop\Bennington College\term2\Computational_Linguistics\MyGitHub\Project#5\output' # windows
# output_directory = r'/home/zalkar/Computational_Linguistics/Project#5/output' # linux


def evaluate(input_directory, output_directory, eval_file):
    total = 0
    similar = 0

    with open(eval_file, 'w') as eval_file:
        for filename in os.listdir(input_directory):
            # skip hidden files
            if filename.startswith('.'):
                continue
            # skip everything NOT .txt
            if not filename.endswith('.txt'):
                continue

            # join directory path with file path to get the whole address
            input_filepath = os.path.join(input_directory, filename)
            output_filepath = os.path.join(output_directory, filename)

            # percentage of similarities between two files
            similarity = compare_two_files(input_filepath, output_filepath)

            # counting average
            total += similarity[1]
            similar += similarity[0]

            print(similarity)

            eval_file.write(filename + '\n')
            eval_file.write("ACCURACY TOP1: " + str(similarity[0] / similarity[1] * 100) + "%" + " (" + str(similarity[0]) + "/" + str(similarity[1]) + ")" + '\n')

        eval_file.write("Total accuracy: " + str(similar / total * 100) + "%" + " (" + str(similar) + "/" + str(total) + ")")

