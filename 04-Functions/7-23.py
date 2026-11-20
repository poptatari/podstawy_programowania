# Check if a password is valid based on the following criteria:
# 1. The password must be at least 6 characters long.
# 2. The password must not contain any repeated characters.

def f(password):
    if len(password) < 6:
        return False

    for char in password:
        if password.count(char) > 1:
            return False

    return True

if __name__ == "__main__":
    print(f("ax15"))
    print(f("book123"))
    print(f("A2water3"))