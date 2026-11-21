# The files.txt contains a list of file names. 
# Write a program that prints only those file names 
# whose extensions consist of exactly four characters 
# (e.g. .html).

import re

with open('files.txt', 'r') as file:
    content = file.read().splitlines()


for line in content:
    if re.match(r'.+\.[a-zA-Z0-9]{4}$', line):
        print(line)

