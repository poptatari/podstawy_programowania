# Write a program that, for the given array of real numbers, 
# prints the number of elements that are greater than the given 
# value entered from the keyboard.

numbers = [3.5, 12.0, 7.25, 1.8, 19.4, 8.0, 4.6]

threshold = float(input("Enter a value: "))
count = 0

for num in numbers:
    if num > threshold:
        count += 1

print(f"Array: {' '.join(map(str, numbers))}")
print(f"Number of elements greater than {threshold}: {count}")