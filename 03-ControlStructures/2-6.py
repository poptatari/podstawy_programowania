###
# A program that checks if a given number
# is positive, negative or 0.
#

number = int(input('Enter a number: '))

if number > 0:
    print(f'Number {number} is positive')
elif number < 0:
    print(f'Number {number} is negative')
else:
    print('Number is 0')