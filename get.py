import re

f = open('a.txt', 'r')
my_pattern = re.compile('(admin@)[\d]{0,3}.+')

for line in f:
    if re.match(my_pattern, line):
        print(line)

