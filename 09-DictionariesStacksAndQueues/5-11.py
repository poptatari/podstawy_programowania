# Write a program to record voting.

import json

try:
    with open('voting.json', 'r') as file:
        votes = json.load(file)
except FileNotFoundError:
    votes = {}

person_name = input('Enter name: ')

if person_name in votes:
    votes[person_name] += 1
else:
    votes[person_name] = 1

with open('voting.json', 'w') as file:
    json.dump(votes, file, indent=4)