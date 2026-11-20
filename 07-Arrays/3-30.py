# Create a program that modifies the array values to 
# create a multiplication table as below. Use loop statements. 
# Print the array.

array = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]


for i in range(len(array)):
    for j in range(len(array[i])):
        array[i][j] = (i + 1) * (j + 1)


for row in array:
    for value in row:
        print(f"{value:2}", end=" ")
    print()