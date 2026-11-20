def is_binary(string):
    for char in string:
        if char not in ['0', '1']:
            return False
    return True

if __name__ == "__main__":
    print(is_binary("101010"))
    print(is_binary("1311a10100")) 