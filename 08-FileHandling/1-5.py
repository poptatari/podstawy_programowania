###
# Reads from file, line by line
#

with open('countries.txt', 'r') as file:
    count = 1
    for line in file:
        print(f"{count}. {line}", end="")
        count += 1