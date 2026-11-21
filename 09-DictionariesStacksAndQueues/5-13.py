import queue

stack = queue.LifoQueue()

while True:
    item = input("Enter number, operator (+, -, *, /), or =: ")

    if item == "=":
        result = stack.get()
        print(f"Result: {result}")
        break

    elif item in ["+", "-", "*", "/"]:
        second = stack.get()  # Right-hand operand
        first = stack.get()   # Left-hand operand

        if item == "+":
            stack.put(first + second)
        elif item == "-":
            stack.put(first - second)
        elif item == "*":
            stack.put(first * second)
        elif item == "/":
            stack.put(first / second)

    else:
        stack.put(float(item))