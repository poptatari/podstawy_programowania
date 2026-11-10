###
# Program that asks the user for their age
# and checks which age group they belong to.
#

age = int(input('Enter age: '))

if age < 13:
    print('You are a child.')
elif age <= 19:
    print('You are a teen.')
elif age <= 64:
    print('You are an adult.')
else:
    print('You are a senior.')