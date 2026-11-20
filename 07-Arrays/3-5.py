# Create a program that calculates and prints the array 
# and the arithmetic mean of array values. Use the “for” 
# loop statement.

def arithmetic_mean(arr):
    arr_sum = 0
    for el in arr:
        arr_sum += el

    return arr_sum / len(arr)

arr = [15, 8, 31, 47, 2, 19]
print(arithmetic_mean(arr))
print(sum(arr) / len(arr))
