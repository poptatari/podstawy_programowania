def power(x,n):
    # This function calculates x raised to the power of n using recursion.
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)