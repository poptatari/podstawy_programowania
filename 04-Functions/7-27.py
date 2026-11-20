# This function checks if the sum of the first three digits 
# of a product code is congruent to the last digit modulo 7. 

def f(product_code):
    three_digits = product_code[0:3]
    last_digit = int(product_code[-1])

    sum_of_digits = sum(int(digit) for digit in three_digits)
    if sum_of_digits % 7 == last_digit:
        return True
    else:
        return False

if __name__ == "__main__":
    print(f("1082"))
    print(f("2035"))
    print(f("1114"))
    print(f("7071"))