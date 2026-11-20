# Write a program to separate even and odd numbers of 
# a given array of integers. Put all even numbers first, 
# and then odd numbers.

arr = [7, 9, 2, 4, 5, 6]

even_numbers = []
odd_numbers = []

for num in arr:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

arr = even_numbers + odd_numbers

print(f"arr = {arr}")