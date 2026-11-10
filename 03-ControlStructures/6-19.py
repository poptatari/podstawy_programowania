###
# Yes-no question are often used in surveys to 
# gauge people's attitudes with regard to specific 
# ideas or beliefs. Write a program that prints a 
# survey consisting of three questions. Save the 
# answers to logical type variables. Then view the 
# survey result.
#

print('SURVEY')
computer_science = input('Are you interested in computer science? (y/n): ')
computer_games = input('Do you like playing computer games? (y/n): ')
instagram = input('Do you have an Instagram account? (y/n): ')

if computer_science == 'y':
    computer_science = 'Yes'
else:
    computer_science = 'No'

if computer_games == 'y':
    computer_games = 'Yes'
else:
    computer_games = 'No'

if instagram == 'y':
    instagram = 'Yes'
else:
    instagram == 'No'

print(f'SURVEY RESULTS Interested in computer science: {computer_science}')
print(f'Playing computer games: {computer_games}')
print(f'Has an Instagram account: {instagram}')