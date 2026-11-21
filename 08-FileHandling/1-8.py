# The file pets.txt contains humorous text 
# about animals. Write a program that prints 
# the text and counts the number of words in the text.

def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

file_content = read_from_file('pets.txt')
print(file_content)

words = len(file_content.split())
print(f'Number of words: {words}')