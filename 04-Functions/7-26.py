# A function that returns the given text with all 
# characters separated by a dash sign.

def f(text):
    result = list(text)
    return "-".join(result)

if __name__ == "__main__":
    print(f("University"))
    print(f("UE"))
    print(f("x"))
    print(f(""))