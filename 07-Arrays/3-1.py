# Create a program that calculates and prints the number of 
# even values in the array. Use the ‘while’ loop statement.

arr = [34, 7, 19, 4, 21, 8]

i = 0
even_numbers = 0
while i < len(arr):
    if arr[i] % 2 == 0:
        even_numbers += 1

    i += 1

print(f'Number of even values in an array: {even_numbers}') 