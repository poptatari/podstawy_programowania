# This function returns the difference between the largest and smallest of three numbers.

def f(number1, number2, number3):
    numbers = [number1, number2, number3]
    largest = max(numbers)
    smallest = min(numbers)
    return largest - smallest

if __name__ == "__main__":
    print(f(7,4,9))
    print(f(2,12,8))