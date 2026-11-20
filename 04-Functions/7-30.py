def sum_natural(n):
    # This function calculates the sum of the first n natural numbers.
    if n < 1:
        return 0
    else:
        return n + sum_natural(n - 1)

if __name__ == "__main__":
    print(sum_natural(5))