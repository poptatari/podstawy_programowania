# The file books.csv contains a list of books. 
# Write a program that copies the book data from a
# given genre to its corresponding file. 
# Use functions to divide the program into logical parts.

import csv

def read_books(filename):
    with open(filename, 'r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        return list(reader)


def save_genre_books(books, target_genre, output_filename):
    with open(output_filename, 'w', encoding='utf-8') as file:
        for book in books:
            # book[2] is the Genre column
            if book[2] == target_genre:
                file.write(f"{book[0]},{book[1]},{book[2]},{book[3]}\n")


all_books = read_books('books.csv')

genres = [
    ['Fantasy', 'books_fantasy.txt'],
    ['Historical', 'books_historical.txt'],
    ['Romance', 'books_romance.txt'],
    ['Classic', 'books_classic.txt']
]

for genre, filename in genres:
    save_genre_books(all_books, genre, filename)