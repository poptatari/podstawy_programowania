# Write a program that modifies the array values. 
# Print the array after each change.

arr = [1, 2, 3, 4, 5]
print(arr)

# Decrease the first value by 1
arr[0] -= 1
print(arr)

# Increase the last value by 4
arr[-1] += 4
print(arr)

# Multiply the middle value by 2
arr[len(arr) // 2] *= 2
print(arr)