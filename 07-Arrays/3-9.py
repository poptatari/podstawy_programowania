# Define a function compare(array1, array2) 
# that returns True if both arrays are the same 
# or False otherwise. 

def compare(array1, array2):
    if len(array1) == len(array2):
        i = 0
        while i < len(array1):
            if array1[i] != array2[i]:
                return False
            i += 1
        return True
    return False

def comparison(result):
    if result:
        return 'arrays are the same'
    else:
        return 'arrays are not the same'

arr1 = [5, 3, 12, 23]
arr2 = [5, 3, 12, 23]


print(f'Array1: {" ".join(map(str, arr1))}')
print(f'Array2: {" ".join(map(str, arr2))}')
print(f'Comparison: {comparison(compare(arr1, arr2))}')