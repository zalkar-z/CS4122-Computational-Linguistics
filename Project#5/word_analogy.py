#!/usr/bin/env python3
#
# word_analogy.py - Computational Linguistics Project#5
# Author: Zak Ziiaidin uulu (zalkar@bennington.edu)
# Date Created: 05/09/2019
#

import sys
import os
import time
import numpy
from evaluation import evaluate

# command line readings
vector_file = sys.argv[1]
input_directory = sys.argv[2]
output_directory = sys.argv[3]
eval_file = sys.argv[4]
should_normalize = sys.argv[5]
similarity_type = sys.argv[6]

# temporary-manual reading values
# vector_file = "vectormodel.txt"
# vector_file_size = 896  # number of words in vector_file
# # input_directory = r'/Users/zalkar/Desktop/Computational_Linguistics/Project#5/GoogleTestSet' # mac
# input_directory = r'C:\Users\User\Desktop\Bennington College\term2\Computational_Linguistics\MyGitHub\Project#5\GoogleTestSet' # windows
# # input_directory = r'/home/zalkar/Computational_Linguistics/Project#5/GoogleTestSet' # linux
#
# # output_directory = r'/Users/zalkar/Desktop/Computational_Linguistics/Project#5/output' # mac
# output_directory = r'C:\Users\User\Desktop\Bennington College\term2\Computational_Linguistics\MyGitHub\Project#5\output' # windows
# # output_directory = r'/home/zalkar/Computational_Linguistics/Project#5/output' # linux
#
# should_normalize = 1
# similarity_type = 2

vectors = {}  # a global dictionary for vectors


#
# Function: Calculates a magnitude of a given vector.
# Return:   A magnitude of a given vector.
#
def magnitude_of_vector(vector):
    return numpy.linalg.norm(vector, ord=2)


#
# Function: Normalizes vectors of given words in an array.
# Return:   Nothing.
#
def normalize_vectors(words):
    for word in words:
        # counting the magnitude of a given vector
        magnitude = numpy.linalg.norm(vectors[word], ord=2)
        # dividing all value inside the vector by the magnitude, it it is higher than zero
        if magnitude:
            vectors[word] = vectors[word] / magnitude


#
# Function: Returns distance of a given type.
# Return:   Returns distance of a given type.
#
def vector_distance(distance_type, first_vector, second_vector):
    # converting string to int
    distance_type = int(distance_type)

    # handling all distance types
    if distance_type == 0:
        # Euclidean distance
        return numpy.sum(numpy.square(first_vector - second_vector))
    if distance_type == 1:
        # Manhattan distance
        return numpy.sum(numpy.abs(second_vector - first_vector))
    if distance_type == 2:
        # Cosine distance
        return 1 - (numpy.dot(first_vector, second_vector))


def solve(line):
    # split line by whitespace
    words = line.split()

    # handling words that are not in the vector model
    for word in words:
        if word not in vectors:
            # initiate vectors with zeros
            vectors[word] = numpy.zeros(300)

    # handling normalization
    if int(should_normalize):
        normalize_vectors(words)

    # handling vector addition and subtraction
    sum_of_vectors = numpy.add(vectors[words[2]], vectors[words[1]])
    sum_of_vectors = sum_of_vectors - vectors[words[0]]

    # initial values
    best_distance = float('inf')
    result = ''

    # looping through all words in global vectors
    for word in vectors:
        current_distance = vector_distance(similarity_type, sum_of_vectors, vectors[word])
        if current_distance < best_distance:
            best_distance = current_distance
            result = word

    return words[0] + ' ' + words[1] + ' ' + words[2] + ' ' + result + '\n'


def main():

    # timer starts
    start = time.time()

    # Step:1 - reading vectors
    with open(vector_file, 'r') as open_file:
        for line in open_file.readlines():
            # splits a string by whitespaces and converts to a list
            temp_list = line.split()
            # save the first one as word
            vector_word = temp_list[0]
            # the rest is a list of vectors
            vector_list = temp_list[1:]
            # add to the global dictionary
            vectors[vector_word] = numpy.array(vector_list, dtype=float)

    # Step:2 - read tests
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

        # read from file and write a solution to a new file
        with open(input_filepath, 'r') as input_file:
            with open(output_filepath, 'w') as output_file:
                for line in input_file.readlines():
                    output_file.write(solve(line))

    # use external function to write the evaluation of directory
    evaluate(input_directory, output_directory, eval_file)

    # stop timer
    end = time.time()
    print("Runtime: ", end - start)


if __name__ == "__main__":
    main()
