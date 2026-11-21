# Create a dictionary that describes your favorite book 
# or movie with at least five key-value pairs. Then, 
# create a program that writes the dictionary data to the 
# favourite.json file.

import json

favourite_book = {
    "title": "The Metamorphosis",
    "author": "Franz Kafka",
    "year_published": 1915,
    "genre": "Absurdist fiction",
    "protagonist": "Gregor Samsa"
}

with open('favourite.json', 'w') as file:
    json.dump(favourite_book, file, indent=4)