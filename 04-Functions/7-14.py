# Create a function that performs basic arithmetic operations

def f(number1,number2,operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '%':
        if number2 != 0:
            return number1 % number2
        else:
            return "Division by zero"   
    elif operator == '**':
        return number1 ** number2

if __name__ == "__main__":
    print(f(2, 3, '+'))
    print(f(2, 3, '-'))
    print(f(2, 3, '*'))
    print(f(2, 3, '%'))
    print(f(2, 3, '**'))