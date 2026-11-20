def find_min_max(arr):
    min_val = arr[0][0]
    min_row, min_col = 0, 0
    
    max_val = arr[0][0]
    max_row, max_col = 0, 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] < min_val:
                min_val = arr[i][j]
                min_row, min_col = i, j
            if arr[i][j] > max_val:
                max_val = arr[i][j]
                max_row, max_col = i, j

    return (
        f"Smallest value: {min_val}, Location: row {min_row}, column {min_col} ([{min_row}][{min_col}])\n"
        f"Largest value: {max_val}, Location: row {max_row}, column {max_col} ([{max_row}][{max_col}])"
    )

array = [[-38, 19], [5, 40], [-7, 11], [29, 16]]
print(find_min_max(array))