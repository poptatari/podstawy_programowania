# Define a function star(n) that returns the given 
# number of asterisks as a string.

def star(n):
    return '*' * n

arr = [2, 6, 4, 9, 7]

for el in arr:
    print(f'{el}: {star(el)}')