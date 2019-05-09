
from itertools import product

first_file = r'C:\Users\User\Desktop\Bennington College\term2\Computational_Linguistics\MyGitHub\Project#5\GoogleTestSet\capital-common-countries.txt'
second_file = r'C:\Users\User\Desktop\Bennington College\term2\Computational_Linguistics\MyGitHub\Project#5\output\capital-common-countries.txt'

with open(first_file, 'r') as first:
    with open(second_file, 'r') as second:
        for line1, line2 in product(first.readlines(), second.readlines()):
            print(line1, '-', line2)