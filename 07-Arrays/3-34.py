# Create a function identity_matrix(n) that returns an 
# identity matrix(2D array) of size n.
# Then, create a function that prints a 2D array in rows 
# and columns. Finally, create a program that prints three 
# identity matrices with dimensions of 3, 5 and 8. 

def identity_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix


def print_2d_array(array):
    for row in array:
        for value in row:
            print(value, end=" ")
        print()


for size in [3, 5, 8]:
    print(f"Identity matrix ({size}x{size}):")
    matrix = identity_matrix(size)
    print_2d_array(matrix)
    print()