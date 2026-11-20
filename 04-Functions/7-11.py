# Check if any of the three numbers is negative

def f(n1, n2, n3):
    if n1 < 0 or n2 < 0 or n3 < 0:
        return True
    else:
        return False

if __name__ == "__main__":
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    n3 = int(input("Enter the third number: "))
    print(f(n1, n2, n3))