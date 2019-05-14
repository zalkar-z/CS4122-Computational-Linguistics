#!/usr/bin/env python3
#
# checker_file.py - Computational Linguistics Project#5
# Author: Zak Ziiaidin uulu (zalkar@bennington.edu)
# Date Created: 05/09/2019
#


first_file = r'/Users/zalkar/Desktop/Computational_Linguistics/Project#5/GoogleTestSet/currency.txt' # mac
# first_file = r'C:\Users\User\Desktop\Bennington College\term2\Computational_Linguistics\MyGitHub\Project#5\GoogleTestSet\currency.txt' # windows
# first_file = r'/home/zalkar/Computational_Linguistics/Project#5/GoogleTestSet/gram6-nationality-adjective.txt' # linux

second_file = r'/Users/zalkar/Desktop/Computational_Linguistics/Project#5/output/currency.txt'
# second_file = r'C:\Users\User\Desktop\Bennington College\term2\Computational_Linguistics\MyGitHub\Project#5\output\currency.txt' # windows
# second_file = r'/home/zalkar/Computational_Linguistics/Project#5/output/gram6-nationality-adjective.txt' # linux


#
# Function: compares two .txt files line by line.
# Return:   Percentage of similarity.
#
def compare_two_files(first_file_address, second_file_address):
    list1 = []
    list2 = []

    with open(first_file_address, 'r') as first:
        for line1 in first.readlines():
            list1.append(line1)

    with open(second_file_address, 'r') as second:
        for line2 in second.readlines():
            list2.append(line2)

    similar = 0

    for i in range(len(list1)):
        if list1[i] == list2[i]:
            similar += 1

    return [similar, len(list1)]


def main():
    print("CHECK")


if __name__ == "__main__":
    main()
