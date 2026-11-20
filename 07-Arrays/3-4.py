# Create a program that finds and prints the maximum and 
# minimum number. Do not use available functions.

def min_from_arr(arr):
    min_value = arr[0]
    
    for el in arr:
        if el < min_value:
            min_value = el

    return min_value

def max_from_arr(arr):
    max_value = arr[0]

    for el in arr:
            if el > max_value:
                max_value = el

    return max_value


arr = [-15, 8, -31, 47, -2, 19]
print(min_from_arr(arr))
print(max_from_arr(arr))