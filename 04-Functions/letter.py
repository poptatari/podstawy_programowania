def letter_count(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count

if __name__ == "__main__":
    string = input("Enter a string: ")
    letter = input("Enter a letter to count: ")
    count = letter_count(string, letter)
    print(f"The letter '{letter}' appears {count} times in the string.")