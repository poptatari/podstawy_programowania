# Write a program that calculates the number of vowels in the text entered from the keyboard. 
# Use regular expressions.

import re

text = input("Enter text: ")

vowels = re.findall(r'[aeiouAEIOU]', text)
count = len(vowels)

print(f"Number of vowels: {count}")