def sort_arr(array):
    """Helper function to return a sorted copy of the array (Bubble Sort)."""
    arr = [x for x in array]
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def second_largest(array):
    # 1. Returns the second largest element in an array.
    sorted_arr = sort_arr(array)
    return sorted_arr[len(sorted_arr) - 2]


def min_max_diff(array):
    # 2. Returns the difference between the largest and smallest values.
    smallest = array[0]
    largest = array[0]
    
    for num in array:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
            
    return largest - smallest


def median(array):
    # 3. Returns the median of numbers in an array.
    sorted_arr = sort_arr(array)
    n = len(sorted_arr)
    mid = n // 2
    
    # If the number of elements is odd, return the middle element
    if n % 2 != 0:
        return sorted_arr[mid]
    # If even, return the average of the two middle elements
    else:
        return (sorted_arr[mid - 1] + sorted_arr[mid]) / 2


def min_max(array):
    # 4. Returns a two-element array [smallest, largest].
    smallest = array[0]
    largest = array[0]
    
    for num in array:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
            
    return [smallest, largest]


def format_minus(array):
    # 5. Returns array elements as a string separated by a minus sign.
    result = ""
    for i in range(len(array)):
        result += str(array[i])
        if i < len(array) - 1:
            result += "-"
    return result

if __name__ == "__main__":
    array = [7,3,8,5,2]
    print(f"Numbers: {' '.join(map(str, array))}")
    print(f"Second largest number: {second_largest(array)}")
    print(f"Median: {median(array)}")
    print(f"Smallest and largest number: {''.join(map(str, min_max(array)))}")
    print(f"Numbers as a string: {format_minus(array)}")
