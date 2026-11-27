import ebook

book = ebook.Ebook('The Trial', 'Franz Kafka', 300)

def main():
    book.open()
    book.status()
    for _ in range(5):
        book.go_forward()
    book.status()
    book.close()
    book.go_backward()

if __name__ == '__main__':
    main()