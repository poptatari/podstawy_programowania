###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = input('Name: ')
surname = input('Surname: ')

print(f'Your name has {len(name)} characters')
print(f'Your surname has {len(surname)} characters')
print(f'Your full name has {len(name) + len(surname) + 1}') # with a space between name and surname