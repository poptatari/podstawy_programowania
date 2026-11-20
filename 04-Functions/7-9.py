# Function to calculate the sum of even or odd digits in a number

def f(number, even):
    sum = 0
    for num in str(number):
        if even and int(num) % 2 == 0:
            sum += int(num)
        elif not even and int(num) % 2 != 0:
            sum += int(num)
    return sum

if __name__ == "__main__":
    print(f(3124, True))
    print(f(3124, False))