###
# There are coins of 1, 2 and 5 Polish Zlotys (PLN). 
# Write a program showing any amount (natural number) 
# read from the keyboard with as few coins as possible.
#

amount = int(input('Enter the amount in PLN: '))

one_pln = 0
two_pln = 0
five_pln = 0

while amount >= 5:
    amount -= 5
    five_pln += 1

while amount >= 2:
    amount -= 2
    two_pln += 1

if amount == 1:
    amount -= 1
    one_pln += 1

print(f'5 PLN coins: {five_pln}')
print(f'2 PLN coins: {two_pln}')
print(f'1 PLN coins: {one_pln}')