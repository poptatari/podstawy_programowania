# Create a program that calculates and prints the 
# array and the arithmetic mean of array values.
# Use the “while” loop statement.

arr = [15, 8, 31, 47, 2, 19]
i = 0
arr_sum = 0

while i < len(arr):
    arr_sum += arr[i]
    i += 1

mean = arr_sum / len(arr)
print(mean)