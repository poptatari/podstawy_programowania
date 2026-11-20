# This function sums the digits of a number that appear more than once.

def f(number):
    sum = 0
    for num in str(number):
        count = str(number).count(num)
        if count > 1:
            sum += int(num)
    return sum

if __name__ == "__main__":
    print(f(1027))
    print(f(230335))
    print(f(513553007))