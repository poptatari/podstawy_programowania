# Create a program that computes the second power 
# of each array element. 

def arr_power(arr):
    new_arr = []

    for el in arr:
        new_arr.append(el ** 2)

    return new_arr

print(arr_power([8, 2, 5, 1, 9]))