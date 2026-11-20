# Write a program that checks whether the first array 
# is a subset of the second one (whether all elements of the 
# first array appear in the second array).

array1 = [3, 8, 5]
array2 = [7, 3, 8, 5, 2, 9]

is_subset = True

for item in array1:
    if item not in array2:
        is_subset = False
        break

if is_subset:
    print("Array 1 is a subset of Array 2.")
else:
    print("Array 1 is not a subset of Array 2.")