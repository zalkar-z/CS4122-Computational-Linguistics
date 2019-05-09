
from itertools import product

first_file = r'C:\Users\User\Desktop\Bennington College\term2\Computational_Linguistics\MyGitHub\Project#5\GoogleTestSet\capital-common-countries.txt'
second_file = r'C:\Users\User\Desktop\Bennington College\term2\Computational_Linguistics\MyGitHub\Project#5\output\capital-common-countries.txt'

list1 = []
list2 = []

with open(first_file, 'r') as first:
    for line1 in first.readlines():
        list1.append(line1)

with open(second_file, 'r') as second:
    for line2 in second.readlines():
        list2.append(line2)

count = 0

for i in range(len(list1)):
    if list1[i] == list2[i]:
        count += 1

print(count)
print(count / len(list1) * 100, '%')