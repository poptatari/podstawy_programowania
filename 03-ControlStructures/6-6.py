###
# Program that asks for the number of hours of parking, 
# then calculates and prints the correct fee.
#

hours = int(input('Enter number of hours of parking: '))

if hours == 0:
    fee = 0 
elif hours <= 2:
    fee = 5
elif hours <= 6:
    fee = 15
else:
    fee = 20

print(f'The fee is {fee} PLN')