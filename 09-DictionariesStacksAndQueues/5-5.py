# Write a program that counts how many times each 
# word appears in a paragraph.

paragraph = "cat dog mouse cat rat cat mouse"

# Split the paragraph into a list of individual words
words = paragraph.split()

# Dictionary to store each word and its count
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display the results
for word, count in word_count.items():
    print(f"{word}: {count}")