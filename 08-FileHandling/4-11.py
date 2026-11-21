# Write a program that calculates, prints, and saves to a 
# text file integers from 1 to 100 and their second and 
# third powers. 

with open('powers.txt', 'w') as file:
    for i in range(1, 101):
        file.write(f'{i},{i ** 2},{i**3}\n')