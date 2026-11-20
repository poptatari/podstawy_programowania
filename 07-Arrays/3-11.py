# Create a program that sorts elements of an array 
# containing integer numbers. Apply the Bubble Sort 
# sorting algorithm. Define a function bubblesort(array) 
# that returns the sorted array. Try to sort and print any 
# three arrays.

def bubblesort(array):
    n = len(array)
    
    for i in range(n):
        swapped = False
        # Last i elements are already in their final sorted positions
        for j in range(0, n - i - 1):
            # Swap if the current element is greater than the next
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        
        # If no swaps occurred in this pass, the array is already sorted
        if not swapped:
            break
            
    return array


arr1 = [64, 34, 25, 12, 22, 11, 90]
arr2 = [5, 1, 4, 2, 8]
arr3 = [-3, 19, 0, -15, 7, 4]

print(f"Sorted array 1: {' '.join(map(str, bubblesort(arr1)))}")
print(f"Sorted array 2: {' '.join(map(str, bubblesort(arr2)))}")
print(f"Sorted array 3: {' '.join(map(str, bubblesort(arr3)))}")