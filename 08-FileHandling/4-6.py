# Write a program that calculates the number of lines, 
# characters and words for any text file. 

file_name = input("File name: ")

try:
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()

    lines = len(content.splitlines())
    characters = len(content)
    words = len(content.split())

    print(f"Number of lines: {lines}")
    print(f"Number of characters: {characters}")
    print(f"Number of words: {words}")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")