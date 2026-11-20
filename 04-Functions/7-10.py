# Count negative even numbers between two numbers

def f(x, y):
    count = 0
    for i in range(x, y + 1):
        if i < 0 and i % 2 == 0:
            count += 1
    return count

if __name__ == "__main__":
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    print(f"The count of negative even numbers between {x} and {y} is: {f(x, y)}")