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

# temporary-manual reading values
vector_file = "smaller_model.txt"
vector_file_size = 773  # number of words in smaller_model.txt
input_directory = r'C:\Users\User\Desktop\Bennington College\term2\Computational_Linguistics\MyGitHub\Project#5\GoogleTestSet'
output_directory = r'C:\Users\User\Desktop\Bennington College\term2\Computational_Linguistics\MyGitHub\Project#5\output'
should_normalize = 1


vectors = {}  # a global dictionary for vectors


#
# Function: Adds two vectors of the same length
# Return:   Summarized vector.
#
def vector_sum(first, second):
    result = []
    for i in range(len(first)):
        result.append(first[i] + second[i])

    return result


#
# Function: Subtracts two vectors of the same length
# Return:   Subtracted vector.
#
def vector_difference(first, second):
    result = []
    for i in range(len(first)):
        result.append(first[i] - second[i])

    return result

#
# Function: calculates the magnitude of a given vector.
# Return:   A magnitude of a given vector.
#
def magnitude_of_vector(vector):
    magnitude = 0
    for i in range(len(vector)):
        magnitude += vector[i] * vector[i]

    return magnitude


#
# Function: Normalizes vectors of given words in an array.
# Return:   Nothing.
#
def normalize_vectors(words):
    for word in words:
        magnitude = magnitude_of_vector(vectors[word])
        for i in range(len(vectors[word])):
            vectors[word][i] = vectors[word][i] / magnitude


def solve(line):
    # split line by whitespace
    line = line.split()

    # an array for paired words
    first_pair = [line[0], line[1]]
    second_pair = [line[2], '']

    # handling normalization
    if should_normalize:
        normalize_vectors([first_pair[0], first_pair[1], second_pair[0]])

    # handling vector addition and subtraction
    summary_vector = vector_sum(second_pair[0], first_pair[1])
    summary_vector = vector_difference(summary_vector, first_pair[0])

    # handling similarity metrics
    



# # Step:1 - reading vectors
# with open(vector_file, 'r') as open_file:
#     for line in open_file.readlines():
#         # splits a string by whitespaces and converts to a list
#         temp_list = line.split()
#         # save the first one as word
#         vector_word = temp_list[0]
#         # the rest is list of vector
#         vector_list = temp_list[1:]
#         # add to the global dictionary
#         vectors[vector_word] = list(map(float, vector_list))
#
# # Step:2 - read tests
# for filename in os.listdir(input_directory):
#     # skip hidden files
#     if filename.startswith('.'):
#         continue
#     # skip everything NOT .txt
#     if not filename.endswith('.txt'):
#         continue
#     # join directory path with file path to get the whole address
#     input_filepath = os.path.join(input_directory, filename)
#     output_filepath = os.path.join(output_directory, filename)
#
#     # read from file
#     with open(input_filepath, 'r') as input_file:
#         with open(output_filepath, 'w') as output_file:
#             for line in input_file.readlines():
#                 output_file.write(solve(line))
#

def main():



if __name__ == "__main__":
    main()
