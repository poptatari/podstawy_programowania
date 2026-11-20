# This function returns the acronym of a given string.

def f(name):
    acronym = ""
    for word in name.split():
        acronym += word[0]

    return acronym

if __name__ == "__main__":
    print(f("Internet of Things"))
    print(f("For Your Information"))
    print(f"Python")