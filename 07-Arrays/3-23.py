def word_count(text):
    # 1. Returns the number of words in the text.
    words = text.split()
    return len(words)


def longest_to_shortest(text):
    # 2. Returns an ordered array of words, from longest to shortest.
    words = text.split()
    return sorted(words, key=len, reverse=True)


def alphabetical_order(text):
    # 3. Returns an alphabetically ordered array of words.
    words = text.split()
    return sorted(words, key=str.lower)

if __name__ == "__main__":
    text = "An apple a day keeps the doctor away"

    print(f"Text: {text}")
    print(f"Number of words: {word_count(text)}")
    print(f"Words from the longest: {', '.join(longest_to_shortest(text))}")
    print(f"Words ordered alphabetically: {', '.join(alphabetical_order(text))}")