# Create a program that prints the contents 
# of the array in reverse order.

arr = [15, 8, 31, 47, 2, 19]

reversed_arr = []

for el in reversed(arr):
    reversed_arr.append(el)

print(reversed_arr)