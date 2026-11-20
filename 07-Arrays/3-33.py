# A two-dimensional array of the size 3 by 5 contains integer 
# numbers. Create a program that swaps the first and the last 
# column. Print array values in rows and columns before and 
# after changes.

def print_array(arr):
    for row in arr:
        for value in row:
            print(f"{value:2}", end=" ")
        print()

array = [
    [1,  2,  3,  4,  5],
    [6,  7,  8,  9,  10],
    [11, 12, 13, 14, 15]
]

print("Before swap:")
print_array(array)

for row in array:
    row[0], row[-1] = row[-1], row[0]

print("\nAfter swap:")
print_array(array)