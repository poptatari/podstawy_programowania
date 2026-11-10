# Write a program that prints a lottery coupon 
# (numbers from 1 to 49) in the format as below.
# 1 8 15 22 29 36 43
# 2 9 16 23 30 37 44
# 3 10 17 24 31 38 45
# 4 11 18 25 32 39 46
# 5 12 19 26 33 40 47
# 6 13 20 27 34 41 48
# 7 14 21 28 35 42 49

row_number = 1
current_number = 0
row = ''

for i in range(1, 8):
    current_number = row_number
    for j in range(1,8):
        row += str(current_number) + ' '
        current_number += 7

    print(row)
    row_number += 1
    row = ''

        