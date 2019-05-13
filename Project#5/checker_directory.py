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
input_directory = r'/home/zalkar/Computational_Linguistics/Project#5/GoogleTestSet' # linux

# output_directory = r'/Users/zalkar/Desktop/Computational_Linguistics/Project#5/output' # mac
# output_directory = r'C:\Users\User\Desktop\Bennington College\term2\Computational_Linguistics\MyGitHub\Project#5\output' # windows
output_directory = r'/home/zalkar/Computational_Linguistics/Project#5/output' # linux


def compare_two_directories(input_directory, output_directory):
    counter = 0
    sum = 0

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
        percentage = compare_two_files(input_filepath, output_filepath)

        # counting average
        sum += percentage
        counter += 1

        print(filename, percentage)

    return sum / counter


def main():
    print(compare_two_directories(input_directory, output_directory))


if __name__ == "__main__":
    main()
