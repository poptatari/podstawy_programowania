# Create a string of numbers from 1 to n

def f(n):
    str_n = ''
    for i in range(1, n + 1):
        str_n += str(i)
    return str_n

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f(n))