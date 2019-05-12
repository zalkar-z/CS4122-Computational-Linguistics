
from itertools import product

first_file = r'C:\Users\User\Desktop\Bennington College\term2\Computational_Linguistics\MyGitHub\Project#5\GoogleTestSet\currency.txt'
# first_file = r'/home/zalkar/Computational_Linguistics/Project#5/GoogleTestSet/gram6-nationality-adjective.txt'
second_file = r'C:\Users\User\Desktop\Bennington College\term2\Computational_Linguistics\MyGitHub\Project#5\output\currency.txt'
# second_file = r'/home/zalkar/Computational_Linguistics/Project#5/output/gram6-nationality-adjective.txt'

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
