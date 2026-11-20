# This function returns the nth prime number.

def f(n):
    primes = []
    number = 2
    while len(primes) < n:
        if number > 1:
            for i in range(2, int(number**0.5) + 1):
                if (number % i) == 0:
                    break
            else:
                primes.append(number)
        number += 1
    return primes[-1]

if __name__ == "__main__":
    print(f(1))
    print(f(5))