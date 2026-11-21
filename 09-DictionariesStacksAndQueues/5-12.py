# Define a function that takes a string as input 
# and uses a stack to reverse it. Then, write a 
# program to reverse any text entered from the keyboard.

import queue

str = input('Enter a string: ')
stack = queue.LifoQueue()

for char in str:
    stack.put(char)

while not stack.empty():
    print(stack.get(), end="")


