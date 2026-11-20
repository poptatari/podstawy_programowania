# Create a function transpose_matrix(m) that returns 
# transposed matrix m

def transpose_matrix(m):
    rows = len(m)
    cols = len(m[0])
    transposed = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(m[i][j])
        transposed.append(new_row)

    return transposed


def print_matrix(m):
    for row in m:
        for value in row:
            print(value, end=" ")
        print()


matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

matrix3 = [
    [5, 6, 7, 8]
]

matrix1_transposed = transpose_matrix(matrix1)
print_matrix(matrix1_transposed)
print()

matrix2_transposed = transpose_matrix(matrix2)
print_matrix(matrix2_transposed)
print()

matrix3_transposed = transpose_matrix(matrix3)
print_matrix(matrix3_transposed)
print()