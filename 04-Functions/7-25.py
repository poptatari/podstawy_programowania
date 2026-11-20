# Find the sum of all even numbers between x and y (inclusive)
# that are also divisible by 3 but not by 4.

def f(x, y):
    total = 0
    for i in range(x, y + 1):
        if i % 2 == 0 and i % 3 == 0 and i % 4 != 0:
            total += i
    return total

if __name__ == "__main__":
    print(f(1, 20))
    print(f(10, 30))