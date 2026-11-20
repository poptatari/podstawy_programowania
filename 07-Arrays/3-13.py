# Define a function occurs(number, array) that returns True if 
# a given number is present in an array. Then create a program 
# that checks whether the number entered from the keyboard is 
# present in the array [15, 38, 7, 23, 14]. 

def occurs(number, arr):
    if number in arr:
        return True
    else:
        return False

array = [15, 38, 7, 23, 14]

num = int(input('Number: '))
print('Array', ' '.join(map(str, array)))

if occurs(num, array):
    print(f'Number {num} appears in the array')
else:
    print(f'Number {num} does not appear in the array')