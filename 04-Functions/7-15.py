# The + sign means a person entering a room and 
# the -- sign a person leaving a room. Define the 
# function f(detector) that returns True if at least 
# 3 people were in the room at the same time, or 
# False otherwise. 

def f(detector):
    count = 0
    for char in detector:
        if char == '+':
            count += 1
        elif char == '-':
            count -= 1

        if count == 3:
            return True

    return False

if __name__ == "__main__":
    print(f("+-+++-+---"))
    print(f("+-+-+-+-"))
    print(f("+-++-+--"))
    print(f("+-++-++-+---"))