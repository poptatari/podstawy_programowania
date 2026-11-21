# The file dogs.json contains data about dogs. 
# Write a program that prints information about dogs 
# younger than 5 years.

import json

with open('dogs.json', 'r') as file:
    data = json.load(file)

for dog in data:
    if dog['age'] < 5:
        print(dog)