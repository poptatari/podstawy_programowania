import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # brackets ok
expression2 = "[(2+3]/4)"                  # brackets not correct
expression3 = "(2-3*4+(5/6)"               # brackets not correct


def brackets_ok(expression):
    # Create a LIFO stack to store opening brackets
    brackets = queue.LifoQueue()

    # Map each closing bracket to its matching opening bracket
    pairs = {')': '(', ']': '[', '}': '{'}

    # Read the expression one character at a time
    for char in expression:
        # Push opening brackets onto the stack
        if char in ['[', '{', '(']:
            brackets.put(char)

        # Validate closing brackets against the top of the stack
        elif char in [']', '}', ')']:
            # If the stack is empty, there is no matching opening bracket
            if brackets.empty():
                return False

            # Pop the most recent opening bracket and check if it matches
            top = brackets.get()
            if top != pairs[char]:
                return False

    # Return True only if all opening brackets were closed (stack is empty)
    return brackets.empty()


# Test the three expressions
if brackets_ok(expression1):
    print("Expression 1: Brackets are OK")
else:
    print("Expression 1: Brackets are NOT correct")

if brackets_ok(expression2):
    print("Expression 2: Brackets are OK")
else:
    print("Expression 2: Brackets are NOT correct")

if brackets_ok(expression3):
    print("Expression 3: Brackets are OK")
else:
    print("Expression 3: Brackets are NOT correct")