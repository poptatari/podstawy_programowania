# Define a function rand_elem(array) that returns a r
# andomly selected array element. Using the function, print 
# a few randomly selected array elements.

import random

def rand_elem(array):
    index = random.randint(0, len(array) - 1)
    return array[index]

elements = [10, 20, 30, 40, 50, 60, 70]

print(f"Array: {' '.join(map(str, elements))}")
print("Randomly selected elements:")
for _ in range(4):
    print(rand_elem(elements))