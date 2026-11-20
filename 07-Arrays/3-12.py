# Create a program that prints all unique elements in an array.

def unique(arr):
    unique_elements = []
    for el in arr:
        if arr.count(el) == 1:
            unique_elements.append(el)

    return unique_elements

array = [2, 3, 2, 5, 8, 1, 9, 8]

print('Array:', ' '.join(map(str, array)))
print('Unique elements:', ' '.join(map(str, unique(array))))