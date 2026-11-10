###
# Program that calculates a dog's age in dog's years. 
# For the first two years, a dog's life is equal to 
# 10.5 human years. After that, each dog year is equal 
# to 4 human years. 
#

age = int(input("Enter the dog's age in human years: "))

if age <= 2:
    dog_age = age * 10.5
else:
    dog_age = 2 * 10.5 + (age - 2) * 4

print(f"The dog's age in dog's years is {dog_age:g} years.")