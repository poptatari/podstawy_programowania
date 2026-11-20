# Create a string of asterisks from 1 to n separated by slashes

def f(n):
    asterisks = []
    if n > 0:
        asterisks = ['*'] * n
    return "/".join(asterisks)

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f(n))