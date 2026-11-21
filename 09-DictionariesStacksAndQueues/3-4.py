# Write a program that converts any natural number 
# to a binary number.

import queue

number = int(input("Enter a natural number: "))
stack = queue.LifoQueue()

# Divide by 2 and push remainders onto the stack
while number > 0:
    stack.put(number % 2)
    number = number // 2

# Pop and display digits in reverse (LIFO) order
print("Binary number: ", end="")
while not stack.empty():
    digit = stack.get()
    print(digit, end="")