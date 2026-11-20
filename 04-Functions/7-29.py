def factorial(n):
    # BASE CASE: Stop the recursion when n reaches 0 or 1.
    # By mathematical definition, both 0! and 1! equal 1.
    if n == 0 or n == 1:
        return 1

    # RECURSIVE STEP: For numbers greater than 1, break the problem
    # into a smaller version of itself: n! = n * (n - 1)!
    # The function pauses here and calls itself with (n - 1).
    if n > 1:
        return n * factorial(n - 1)

if __name__ == "__main__":
    print(factorial(5))