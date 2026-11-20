def flatten_2d(array_2d):
    array_1d = []
    for row in array_2d:
        for item in row:
            array_1d.append(item)
    return array_1d

def print_1dmatrix(m):
    for el in m:
        print(el, end=" ")

matrix1 = [
    [2, 3],
    [1, 5]
]

matrix2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]

matrix3 = [
   [2, 1],
   [3, 5], 
   [7, 4], 
   [2, 6]
] 

print_1dmatrix(flatten_2d(matrix1))
print()
print_1dmatrix(flatten_2d(matrix2))
print()
print_1dmatrix(flatten_2d(matrix3))
