# Check if a number is within a specified range

import check_range

number = int(input("Enter a number: "))
min_value = int(input("Enter the minimum value: "))
max_value = int(input("Enter the maximum value: "))

if check_range.in_range(number, min_value, max_value):
    print(f"Number {number} in the range <{min_value}, {max_value}>: yes")
else:
    print(f"Number {number} in the range <{min_value}, {max_value}>: no")
