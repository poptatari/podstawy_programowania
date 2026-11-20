# Create a program that prints the numbers from the first 
# array that do not appear in the second array.


array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36]

for number in array1:
    if number not in array2:
        print(number, end=" ")